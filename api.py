import requests
import pandas as pd
import time
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

API_KEY = "your api key"

# Bengaluru South boundaries
LAT_START = 12.8800
LAT_END = 12.9500
LNG_START = 77.5800
LNG_END = 77.6400
RADIUS = 1000
LAT_STEP = 0.009
LNG_STEP = 0.009
NEARBY_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json"

PLACE_TYPES = {
    "restaurant": "restaurant",
    "supermarket": "supermarket",
    "college": "university",
    "school": "school",
    "hospital": "hospital"
}

# Functions
def get_places(api_key, location, radius, place_type):
    places = []
    url = f"{NEARBY_URL}?location={location}&radius={radius}&type={place_type}&key={api_key}"
    while True:
        response = requests.get(url)
        data = response.json()
        if "results" in data:
            places.extend(data["results"])
        if "next_page_token" in data:
            next_page_token = data["next_page_token"]
            time.sleep(2)
            url = f"{NEARBY_URL}?pagetoken={next_page_token}&key={api_key}"
        else:
            break
    return places

def get_place_details(place_id):
    try:
        url = f"{DETAILS_URL}?place_id={place_id}&fields=website,formatted_phone_number,reviews&key={API_KEY}"
        response = requests.get(url)
        data = response.json()
        result = data.get("result", {})
        return {
            "website": result.get("website"),
            "phone_number": result.get("formatted_phone_number"),
            "reviews": "; ".join([r.get("text","") for r in result.get("reviews", [])[:3]])  # first 3 reviews
        }
    except:
        return {"website": None, "phone_number": None, "reviews": None}

def extract_pincode(address):
    match = re.search(r'\b\d{6}\b', address)
    return match.group(0) if match else None

# Main script
all_data = []

for category, place_type in PLACE_TYPES.items():
    print(f"\nFetching {category}...")
    all_places = []
    lat = LAT_START
    while lat <= LAT_END:
        lng = LNG_START
        while lng <= LNG_END:
            location = f"{lat},{lng}"
            print(f"Fetching {category} at {location}")
            places = get_places(API_KEY, location, RADIUS, place_type)
            all_places.extend(places)
            lng += LNG_STEP
            time.sleep(0.2)  # small delay
        lat += LAT_STEP

    # Remove duplicates
    unique_places = {place['place_id']: place for place in all_places}.values()

    # Multi-threaded Place Details fetching
    print(f"Fetching Place Details for {len(unique_places)} {category} places...")
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_place = {executor.submit(get_place_details, p['place_id']): p for p in unique_places}
        for future in as_completed(future_to_place):
            p = future_to_place[future]
            details = future.result()
            address = p.get("vicinity", "")
            all_data.append({
                "place_id": p.get("place_id"),
                "name": p.get("name"),
                "address": address,
                "pincode": extract_pincode(address),
                "category": category,
                "lat": p["geometry"]["location"]["lat"],
                "lng": p["geometry"]["location"]["lng"],
                "rating": p.get("rating"),
                "user_ratings_total": p.get("user_ratings_total"),
                "price_level": p.get("price_level"),
                "business_status": p.get("business_status"),
                "opening_now": p.get("opening_hours", {}).get("open_now") if p.get("opening_hours") else None,
                "types": ", ".join(p.get("types", [])),
                "plus_code": p.get("plus_code", {}).get("compound_code"),
                "website": details.get("website"),
                "phone_number": details.get("phone_number"),
                "reviews": details.get("reviews")
            })

# Save to Excel
df = pd.DataFrame(all_data)
df.to_excel("Bengaluru_South_Complete_Places_Fast22.xlsx", index=False)
print("\nAll data saved to Bengaluru_South_Complete_Places_Fast22.xlsx")

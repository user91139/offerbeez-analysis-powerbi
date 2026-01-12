# 📊 Offerbeez Business Data Analysis

## 📌 Project Overview

This repository showcases a **live business data analysis project** completed while working as a **Data Analyst Trainee at VentureBiz Promotion Private Limited**. The project was executed for **Offerbeez**, a business discovery platform, where I performed **end-to-end data collection, analysis, and visualization** to deliver **actionable business insights** to the internal business team.

The solution leverages **API-driven data extraction**, **Python-based analytics**, and **Power BI dashboards** to support **strategic planning, market understanding, and data-driven decision-making**.

---

## 🏢 Business Context

Offerbeez required a centralized analytics solution to:

* Understand **zone-wise business distribution**
* Identify **sector dominance and market opportunities**
* Analyze **customer ratings and service quality**
* Support **business expansion and targeting strategies**

The challenge was converting large volumes of unstructured business listing data into **clear, decision-ready insights**.

---

## 🔗 Data Collection (API Integration)

### API Used

* Google Places API (Nearby Search & Place Details)

### Purpose

* Programmatically collect live business listings
* Extract detailed attributes such as:

  * Business name and address
  * Category / sector
  * Ratings and review counts
  * Business status and opening status
  * Contact details (website, phone)
  * Latitude and longitude

### Implementation Highlights

* Grid-based latitude–longitude scanning for complete geographic coverage
* Category-based extraction:

  * Restaurants
  * Supermarkets
  * Schools and Colleges
  * Hospitals
* Pagination handling using `next_page_token`
* Multi-threaded API calls for faster execution
* Deduplication using unique `place_id`
* Pincode extraction using regex
* Exported structured data to Excel for analytics

**Final API Output File:**
`Bengaluru_South_Complete_Places_Fast22.xlsx`

This file served as the **foundation dataset** for all analysis and dashboards.

---

## 🗂️ Project Structure

```
Offerbeez-Business-Data-Analysis/
│
├── api/
│   └── api.py                     # Google Places API data collection script
│
├── data/
│   ├── zone_counts.csv             # Zone-wise business distribution
│   ├── sector_counts.csv           # Sector-wise contribution
│   ├── category_counts.csv         # Category-level insights
│   ├── top_rated_20.csv            # Top-rated businesses
│   ├── low_rated_20.csv            # Low-rated businesses
│   ├── pin_counts.csv              # Pincode density analysis
│   └── zone_clusters.csv           # Zone clustering insights
│
├── notebooks/
│   └── Offerbeez Analysis.ipynb    # Data cleaning & EDA
│
├── dashboard/
│   └── offerbeez_dashboard.pdf     # Power BI dashboard export
│
├── reports/
│   └── offerbeez_dashboard.png     # Dashboard preview image
│
└── README.md
```

---

## 📂 Dataset Overview

* Approximately **26,000 business records**
* Region covered: **Bengaluru South**
* Key attributes include:

  * Zone and pincode
  * Sector / category
  * Ratings and user rating count
  * Business status
  * Geographic coordinates

### Processed Data Files

* `zone_counts.csv` – zone-wise business distribution
* `sector_counts.csv` – sector-wise contribution
* `category_counts.csv` – category-level insights
* `top_rated_20.csv` – top-rated businesses
* `low_rated_20.csv` – low-rated businesses
* `pin_counts.csv` – pincode density analysis
* `zone_clusters.csv` – zone clustering insights

---

## 🛠️ Tools & Technologies

* **Python** – API integration, data cleaning, EDA
* **Pandas & NumPy** – data transformation and aggregation
* **Jupyter Notebook** – analysis workflow
* **Power BI** – interactive dashboards and visualization
* **DAX** – KPI and metric calculations
* **Microsoft Excel** – data validation

---

## 🔄 Analytics Workflow

1. Live data extraction using Google Places API
2. Raw dataset generation
3. Data cleaning and normalization
4. Exploratory Data Analysis (EDA)
5. Insight-driven CSV creation
6. Power BI dashboard development
7. Business insight delivery to Offerbeez team

---

## 🔍 Exploratory Data Analysis (EDA)

* Zone-wise business concentration analysis
* Sector dominance and contribution analysis
* Customer rating comparison across categories
* Identification of high-performing and underperforming sectors
* Trend and pattern discovery for business growth

---

## 📈 Key Business Insights Delivered

* North and South zones identified as high-density business regions
* Food & Beverages and Retail sectors dominate overall listings
* Personal Services category shows the highest average customer ratings
* Overall customer satisfaction trends remain strong across most sectors

These insights were delivered to the **Offerbeez business team** to support **strategic planning and decision-making**.

---

## 📊 Dashboard (Power BI)

* Interactive Power BI dashboard designed for business stakeholders
* Key KPIs:

  * Total Businesses
  * Average Rating
  * Total Zones Covered
* Dynamic slicers for zone and sector filtering
* Clear visual storytelling for faster insights
* Reset Filters option for improved usability

---

## ▶️ How to Run This Project

1. Clone this repository
2. Add your **Google Places API key** in `api.py`
3. Run the API script to generate raw business data
4. Open the Jupyter Notebook for analysis
5. Install dependencies:

   ```bash
   pip install pandas numpy requests
   ```
6. Load processed CSV files into Power BI
7. Explore insights using the dashboard

---

## ⚠️ Limitations

* Analysis is based on snapshot data, not real-time feeds
* Revenue and transaction-level metrics are not included
* Ratings may not fully capture customer sentiment
* Seasonal and external market factors are not considered

---

## 🚀 Future Enhancements

* Automated and scheduled API data refresh
* Sentiment analysis on customer reviews
* Predictive analytics for business growth trends
* Multi-city expansion analysis
* Automated Power BI refresh pipeline

---
## 👤 Author & Contact
- **Name:** Rehman Khan k
- **Degree:** Master of Computer Applications (MCA)  
- **Role:** Aspiring Data Analyst | Business Analyst 
- **Email:** rehman020219@gmail.com  
- **LinkedIn:** https://www.linkedin.com/in/rehman-khan1919

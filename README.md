# 📦 Same-Day Delivery Decision Support System

> **An end-to-end business analytics project evaluating the feasibility of launching Same-Day Delivery using real-world supply chain data.**

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75?logo=plotly)

---

## 🚀 Live Demo

**Streamlit Dashboard:**  
https://same-daydel.streamlit.app/

**GitHub Repository:**  
<YOUR_GITHUB_REPO_LINK>

---

# 📌 Project Overview

With increasing customer expectations for faster deliveries, e-commerce companies are continuously exploring Same-Day Delivery services.

However, expanding this feature without understanding operational readiness can lead to:

- Increased logistics costs
- Higher late delivery rates
- Poor customer experience
- Reduced profitability

This project analyzes historical supply chain transactions to determine **whether Same-Day Delivery is operationally feasible**, **where it should be introduced first**, and **what trade-offs management should consider**.

Rather than focusing only on data analysis or machine learning, the project is designed as a **business decision-support system** for Product Managers and Supply Chain teams.

---

# 🎯 Business Objectives

The project aims to answer the following business questions:

- Which regions are operationally ready for Same-Day Delivery?
- Which markets experience the highest delivery delays?
- Which customer segments should receive the feature first?
- Which product categories generate maximum business value?
- Which shipping modes perform most efficiently?
- How should management prioritize rollout while minimizing operational risk?

---

# 📊 Dataset

**Dataset:** DataCo Smart Supply Chain Dataset (Kaggle)

The dataset contains:

- 180,000+ supply chain transactions
- Customer information
- Product details
- Shipping information
- Delivery timelines
- Geographic information
- Revenue and profit metrics

---

# 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- Jupyter Notebook

---

# 🔍 Project Workflow

```
Business Problem
        │
        ▼
Data Understanding
        │
        ▼
Data Cleaning
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Business Insights
        │
        ▼
Same-Day Delivery Readiness Framework
        │
        ▼
Interactive Dashboard
        │
        ▼
Management Recommendations
```

---

# 📈 Exploratory Data Analysis

The analysis focuses on multiple business perspectives.

### Executive Analysis

- Revenue
- Profit
- Orders
- Customers

### Logistics Analysis

- Shipping Modes
- Delivery Status
- Delivery Delays
- Average Shipping Time

### Customer Analysis

- Customer Segments
- Revenue by Segment

### Product Analysis

- Revenue by Category
- Profit by Category

### Geographic Analysis

- Revenue by Region
- Late Delivery Rate
- Regional Performance

---

# 📊 Interactive Dashboard

The Streamlit dashboard acts as a decision-support system for management.

### Executive Dashboard

- Total Orders
- Revenue
- Profit
- Customers
- Late Delivery %

### Logistics Dashboard

- Shipping Mode Distribution
- Delivery Status
- Average Delivery Time

### Customer & Product Dashboard

- Revenue by Customer Segment
- Top Product Categories

### Geographic Dashboard

- Revenue by Region
- Late Delivery Rate

### Recommendation Dashboard

- Same-Day Delivery Readiness Score
- Region-wise Rollout Recommendation

---

# 💡 Key Business Insights

- High-revenue markets do not always demonstrate the best logistics performance.
- Standard Class accounts for the largest share of deliveries and therefore has the greatest impact on customer experience.
- Regions with consistently lower late-delivery rates are better candidates for Same-Day Delivery expansion.
- Customer and product prioritization can improve rollout efficiency while minimizing operational risks.
- Revenue and delivery performance should be jointly considered when selecting rollout regions.

---

# 🎯 Final Recommendations

Based on the analysis:

✅ Prioritize rollout in regions with:

- High revenue contribution
- Lower late delivery percentages
- Strong operational performance

✅ Launch in phases instead of a company-wide rollout.

✅ Monitor operational KPIs after deployment:

- Late Delivery %
- Average Delivery Time
- Order Volume
- Revenue
- Customer Satisfaction

✅ Improve logistics performance in underperforming regions before introducing Same-Day Delivery.

---

# 📂 Repository Structure

```
same-day-delivery-strategy
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── Notebooks
    └── Understanding
        ├── EDA.ipynb
        ├── Data_cleaning.ipynb
        └── data
            └── raw
                ├── DataCoSupplyChainDataset.csv
                └── DescriptionDataCoSupplyChain.csv
```

---

# ▶️ Running the Project

Clone the repository

```bash
git clone <YOUR_GITHUB_REPO_LINK>
```

Navigate to the project

```bash
cd same-day-delivery-strategy
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit

```bash
streamlit run app.py
```

---

# 🚀 Future Improvements

Potential extensions include:

- Delivery delay prediction using Machine Learning
- Demand forecasting
- Warehouse capacity optimization
- Route optimization
- Cost-benefit simulation for Same-Day Delivery
- Inventory allocation optimization

---

# Author

**Kavya Jain**

B.Tech, IIT Kharagpur

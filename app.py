import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="Same-Day Delivery Decision Support System",
    layout="wide"
)

# -------------------------------
# Load Data
# -------------------------------

@st.cache_data
def load_data():
    return pd.read_csv(
        "Notebooks/Understanding/data/raw/DataCoSupplyChainDataset.csv",
        encoding="latin1"
    )

df = load_data()

# -------------------------------
# Sidebar Filters
# -------------------------------

st.sidebar.header("Filters")

market = st.sidebar.multiselect(
    "Market",
    sorted(df["Market"].unique()),
    default=sorted(df["Market"].unique())
)

shipping = st.sidebar.multiselect(
    "Shipping Mode",
    sorted(df["Shipping Mode"].unique()),
    default=sorted(df["Shipping Mode"].unique())
)

segment = st.sidebar.multiselect(
    "Customer Segment",
    sorted(df["Customer Segment"].unique()),
    default=sorted(df["Customer Segment"].unique())
)

df = df[
    (df["Market"].isin(market)) &
    (df["Shipping Mode"].isin(shipping)) &
    (df["Customer Segment"].isin(segment))
]

# -------------------------------
# Tabs
# -------------------------------

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Executive",
    "🚚 Logistics",
    "👥 Customers & Products",
    "🌍 Geography",
    "🎯 Recommendation"
])

# ===========================================================
# EXECUTIVE
# ===========================================================

with tab1:

    st.title("📦 Same-Day Delivery Decision Support System")

    st.markdown(
        """
        Interactive dashboard to evaluate the feasibility of
        expanding Same-Day Delivery using historical supply chain data.
        """
    )

    orders = df["Order Id"].nunique()
    customers = df["Customer Id"].nunique()
    revenue = df["Sales"].sum()
    profit = df["Benefit per order"].sum()
    late = df["Late_delivery_risk"].mean() * 100

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("Orders", f"{orders:,}")
    c2.metric("Customers", f"{customers:,}")
    c3.metric("Revenue", f"${revenue:,.0f}")
    c4.metric("Profit", f"${profit:,.0f}")
    c5.metric("Late Delivery %", f"{late:.1f}%")

    st.subheader("🌍 Revenue by Market")

    market_sales = (
        df.groupby("Market")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        market_sales,
        x="Market",
        y="Sales",
        color="Market"
    )

    st.plotly_chart(fig, use_container_width=True)

# ===========================================================
# LOGISTICS
# ===========================================================

with tab2:

    st.header("🚚 Logistics Performance")

    shipping_counts = (
        df["Shipping Mode"]
        .value_counts()
        .reset_index()
    )

    shipping_counts.columns = ["Shipping Mode", "Orders"]

    fig = px.pie(
        shipping_counts,
        values="Orders",
        names="Shipping Mode",
        title="Shipping Mode Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    delivery = (
        df["Delivery Status"]
        .value_counts()
        .reset_index()
    )

    delivery.columns = ["Status", "Orders"]

    fig = px.bar(
        delivery,
        x="Status",
        y="Orders",
        color="Status",
        title="Delivery Status"
    )

    st.plotly_chart(fig, use_container_width=True)

    avg_ship = (
        df.groupby("Shipping Mode")["Days for shipping (real)"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        avg_ship,
        x="Shipping Mode",
        y="Days for shipping (real)",
        color="Shipping Mode",
        title="Average Delivery Time"
    )

    st.plotly_chart(fig, use_container_width=True)

# ===========================================================
# CUSTOMERS & PRODUCTS
# ===========================================================

with tab3:

    st.header("👥 Customer & Product Insights")

    segment_sales = (
        df.groupby("Customer Segment")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        segment_sales,
        x="Customer Segment",
        y="Sales",
        color="Customer Segment",
        title="Revenue by Customer Segment"
    )

    st.plotly_chart(fig, use_container_width=True)

    category_sales = (
        df.groupby("Category Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        category_sales,
        x="Category Name",
        y="Sales",
        color="Category Name",
        title="Top Product Categories"
    )

    st.plotly_chart(fig, use_container_width=True)

# ===========================================================
# GEOGRAPHY
# ===========================================================

with tab4:

    st.header("🌍 Geographic Analysis")

    region_sales = (
        df.groupby("Order Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        region_sales,
        x="Order Region",
        y="Sales",
        color="Order Region",
        title="Revenue by Region"
    )

    st.plotly_chart(fig, use_container_width=True)

    region_delay = (
        df.groupby("Order Region")["Late_delivery_risk"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    region_delay["Late_delivery_risk"] *= 100

    fig = px.bar(
        region_delay,
        x="Order Region",
        y="Late_delivery_risk",
        color="Order Region",
        title="Late Delivery Rate (%)"
    )

    st.plotly_chart(fig, use_container_width=True)

# ===========================================================
# RECOMMENDATION
# ===========================================================

with tab5:

    st.header("🎯 Same-Day Delivery Recommendation")

    summary = (
        df.groupby("Order Region")
        .agg(
            Orders=("Order Id", "nunique"),
            Revenue=("Sales", "sum"),
            Avg_Delivery=("Days for shipping (real)", "mean"),
            Late_Rate=("Late_delivery_risk", "mean")
        )
    )

    summary["Late_Rate"] *= 100

    summary["Revenue Score"] = (
        summary["Revenue"] /
        summary["Revenue"].max()
    )

    summary["Delivery Score"] = (
        1 - summary["Late_Rate"] / 100
    )

    summary["Readiness Score"] = (
        0.6 * summary["Revenue Score"] +
        0.4 * summary["Delivery Score"]
    )

    summary = summary.sort_values(
        "Readiness Score",
        ascending=False
    )

    st.subheader("Top Regions for Same-Day Delivery")

    st.dataframe(summary.round(2))

    st.success(
        """
        Recommendation:
        
        • Launch Same-Day Delivery in the top-ranked regions.
        • Prioritize high-revenue markets with consistently low late-delivery rates.
        • Begin with high-demand customer segments before scaling network-wide.
        """
    )
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales & Revenue Dashboard", page_icon="📊", layout="wide")
st.title("📊 Sales & Revenue Analysis Dashboard")

uploaded_file = st.file_uploader("Upload CSV or Excel File", type=["csv","xlsx"])

if uploaded_file:
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)

    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])

    st.sidebar.header("Filters")

    if "Region" in df.columns:
        regions = st.sidebar.multiselect("Region", df["Region"].unique(), default=df["Region"].unique())
        df = df[df["Region"].isin(regions)]

    if "Product" in df.columns:
        products = st.sidebar.multiselect("Product", df["Product"].unique(), default=df["Product"].unique())
        df = df[df["Product"].isin(products)]

    c1,c2,c3 = st.columns(3)
    c1.metric("Total Sales", f"{df['Sales'].sum():,.0f}")
    c2.metric("Total Revenue", f"₹{df['Revenue'].sum():,.0f}")
    c3.metric("Average Revenue", f"₹{df['Revenue'].mean():,.0f}")

    if "Date" in df.columns:
        trend = df.groupby("Date")["Revenue"].sum().reset_index()
        st.plotly_chart(px.line(trend, x="Date", y="Revenue", title="Revenue Trend"), use_container_width=True)

    top = df.groupby("Product")["Revenue"].sum().reset_index().sort_values("Revenue", ascending=False)
    st.plotly_chart(px.bar(top, x="Product", y="Revenue", title="Top Products"), use_container_width=True)

    region = df.groupby("Region")["Revenue"].sum().reset_index()
    st.plotly_chart(px.pie(region, names="Region", values="Revenue", title="Revenue by Region"), use_container_width=True)

    st.dataframe(df, use_container_width=True)
else:
    st.info("Upload a CSV or Excel file.")

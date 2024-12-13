import streamlit as st
import pandas as pd
import plotly.express as px

# Example data
data = {
    "Date": ["2023-Q1", "2023-Q2", "2023-Q3", "2023-Q4"],
    "Singapore GDP Growth (%)": [3.1, 2.9, 2.8, 3.0],
    "US GDP Growth (%)": [2.0, 2.3, 2.2, 2.4],
    "Singapore Inflation (%)": [2.5, 2.3, 2.2, 2.1],
    "US Inflation (%)": [3.0, 3.2, 3.1, 3.0]
}
df = pd.DataFrame(data)

# Streamlit App Title
st.title("Economic Indicators Dashboard")
st.write("Interactive dashboard for monitoring GDP growth and inflation trends.")

# Sidebar for user input
indicator = st.sidebar.selectbox("Select an indicator to display:", ["GDP Growth", "Inflation Rate"])

# Conditional Display based on selection
if indicator == "GDP Growth":
    st.subheader("GDP Growth Comparison")
    fig = px.line(df, x="Date", y=["Singapore GDP Growth (%)", "US GDP Growth (%)"], 
                  title="GDP Growth Trends (Singapore vs USA)", markers=True)
    st.plotly_chart(fig)
elif indicator == "Inflation Rate":
    st.subheader("Inflation Rate Comparison")
    fig = px.line(df, x="Date", y=["Singapore Inflation (%)", "US Inflation (%)"], 
                  title="Inflation Rate Trends (Singapore vs USA)", markers=True)
    st.plotly_chart(fig)

# Data Table
st.subheader("Raw Data")
st.write(df)

import streamlit as st
import pandas as pd
import plotly.express as px

# Example Data
data = {
    "Date": ["2023-Q1", "2023-Q2", "2023-Q3", "2023-Q4"],
    "Singapore GDP Growth (%)": [3.1, 2.9, 2.8, 3.0],
    "US GDP Growth (%)": [2.0, 2.3, 2.2, 2.4]
}
df = pd.DataFrame(data)

# Streamlit App
st.title("Economic Indicators Dashboard")
st.write("Interactive dashboard for monitoring GDP growth trends.")

# Plot
fig = px.line(df, x="Date", y=["Singapore GDP Growth (%)", "US GDP Growth (%)"], title="GDP Growth Trends")
st.plotly_chart(fig)


import streamlit as st
import plotly.express as px
import pandas as pd
from plotly.offline import iplot

# Retrieved data
retrieved_data = {'Category': ['A', 'B', 'C', 'D'], 
                 'Value': [10, 20, 30, 40], 
                 'Percentage': [0.1, 0.2, 0.3, 0.4]}

# Convert data to DataFrame
df = pd.DataFrame(retrieved_data)

# Create Streamlit app
st.title("Interactive Dashboard")

# Select best chart type
if len(df.columns) == 2:
    chart_type = 'bar'
elif 'Percentage' in df.columns:
    chart_type = 'pie'
else:
    chart_type = 'line'

# Create Plotly figure
if chart_type == 'bar':
    fig = px.bar(df, x='Category', y='Value')
elif chart_type == 'pie':
    fig = px.pie(df, names='Category', values='Value')
else:
    fig = px.line(df, x='Category', y='Value')

# Display chart
st.plotly_chart(fig, use_container_width=True)

# Display insights
st.write("Insights:")
st.write(df.describe())

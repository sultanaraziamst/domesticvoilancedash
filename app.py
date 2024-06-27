# app.py

import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# Function to load data from SQLite database
@st.cache_data
def load_data():
    conn = sqlite3.connect('voilance.db')
    query = 'SELECT * FROM voilance'  # Replace with your actual table name
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def main():
    st.title('Women\'s Violence Data Dashboard')
    st.sidebar.title('Dashboard Menu')

    # Load data
    df = load_data()

    # Display raw data option
    if st.sidebar.checkbox('Show Raw Data'):
        st.subheader('Raw Data')
        st.write(df)

    # Example plot using Plotly
    st.sidebar.subheader('Data Visualization Options')
    plot_type = st.sidebar.selectbox('Select a plot type', ['Bar Chart', 'Pie Chart', 'Histogram'])

  

if __name__ == '__main__':
    main()

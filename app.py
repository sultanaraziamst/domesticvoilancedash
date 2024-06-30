# Import libraries
import streamlit as st
import pandas as pd
import sqlite3
import altair as alt
import plotly.express as px
import numpy as np 


# Function to load data from SQLite database

# Page configuration
def main():
    st.title('Women\'s Violence Data Dashboard')
    st.sidebar.title('Dashboard Menu')

alt.themes.enable("dark")

@st.cache_data
def load_data():
    conn = sqlite3.connect('voilance.db')
    query = 'SELECT * FROM voilance'  # Replace with your actual table name
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
selected_color_theme = st.selectbox('Select a color theme', color_theme_list)

# Load data
df = load_data()


#column 

#( SL., No", Age, Education, Employment, Income, "Marital status", Violence)

# Display raw data option
if st.sidebar.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    st.write(df)


# Example plot using Plotly
st.sidebar.subheader('Data Visualization Options')
plot_type = st.sidebar.selectbox('Select a plot type', ['Bar Chart', 'Pie Chart', 'Histogram', 'Scatter Plot'])


if plot_type == 'Bar Chart':
        st.subheader('Bar Chart')
        fig = px.bar(df, x='Age', y='Education')  # Replace with your columns from your DataFrame
        st.plotly_chart(fig)

elif plot_type == 'Pie Chart':
        st.subheader('Pie Chart')
        fig = px.pie(df, values='Violence', names='Marital status')
        st.plotly_chart(fig)

elif plot_type == 'Histogram':
        st.subheader('Histogram')
        fig = px.histogram(df, x='Income')
        st.plotly_chart(fig)

elif plot_type == 'Scatter Plot':
        st.subheader('Scatter Plot')
        fig = px.scatter(df, x='Age', y='Violence')
        st.plotly_chart(fig)


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Marrital status", "Income", "Eucation", ])

st.line_chart(chart_data)











if __name__ == '__main__':
    main()

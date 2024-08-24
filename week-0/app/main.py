import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('../data/benin-malanville.csv')

df = load_data()

# Streamlit Dashboard
st.title('Solar Radiation Dashboard')

# Sidebar
st.sidebar.header('User Input Parameters')

# Start date
start_date = st.sidebar.date_input('Start Date', value=df['Timestamp'].min())

# End date
end_date = st.sidebar.date_input('End Date', value=df['Timestamp'].max())

# Filter data

filtered_df = df[(df['Timestamp'] >= start_date) & (df['Timestamp'] <= end_date)]

# Display filtered data
st.subheader('Filtered Data')
    
# Display raw data
if st.checkbox('Show Raw Data'):
    st.write(df.head())

# Simple line plot
st.subheader('GHI Over Time')
fig, ax = plt.subplots()
ax.plot(df['Timestamp'], df['GHI'])
ax.set_xlabel('Timestamp')
ax.set_ylabel('GHI (W/m²)')
plt.xticks(rotation=45)
st.pyplot(fig)

# Histogram
st.subheader('Distribution of GHI')
fig, ax = plt.subplots()
ax.hist(df['GHI'], bins=30)
ax.set_xlabel('GHI (W/m²)')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# Correlation heatmap
st.subheader('Correlation Heatmap')
fig, ax = plt.subplots()

corr = df.corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')

st.pyplot(fig)

# Simple line plot

st.subheader('Temperature Over Time')
fig, ax = plt.subplots()
ax.plot(df['Timestamp'], df['Tamb'])
ax.set_xlabel('Timestamp')
ax.set_ylabel('Temperature (°C)')
plt.xticks(rotation=45)
st.pyplot(fig)

# Humidity Over Time    
st.subheader('Humidity Over Time')
fig, ax = plt.subplots()
ax.plot(df['Timestamp'], df['RH'])
ax.set_xlabel('Timestamp')
ax.set_ylabel('Humidity (%)')
plt.xticks(rotation=45)
st.pyplot(fig)

# Wind Speed Over Time
st.subheader('Wind Speed Over Time')


# Wind Direction Over Time
st.subheader('Wind Direction Over Time')

# Atmospheric Pressure Over Time
st.subheader('Atmospheric Pressure Over Time')

# Dew Point Temperature Over Time
st.subheader('Dew Point Temperature Over Time')

# Solar Radiation Over Time
st.subheader('Solar Radiation Over Time')

# Global Horizontal Irradiance Over Time
st.subheader('Global Horizontal Irradiance (GHI) Over Time')
st.line_chart(df[['Timestamp', 'GHI']].set_index('Timestamp'))

# Temperature vs Relative Humidity
st.subheader('Temperature vs Relative Humidity')
fig, ax = plt.subplots()
ax.scatter(df['RH'], df['Tamb'])
ax.set_xlabel('Relative Humidity (%)')
ax.set_ylabel('Temperature (°C)')
st.pyplot(fig)
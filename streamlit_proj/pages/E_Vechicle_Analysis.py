import streamlit as st
import pandas as pd
import numpy as np
import os

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "..", "..", "Dataset", "Electric_Vehicle_Population_Data.csv") 

st.title("📈 Electric Vehicle Population Data Analysis Page")

@st.cache_data
def load_data():
    data=pd.read_csv(file_path)
    return data

data_load_state=st.text('Loading data....')
data=load_data()
data_load_state.text("Done! (using st.cache data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Based on Year sell E-vechile')
st.scatter_chart(data=data,x="Model Year",y="County",x_label="Year",y_label="Country")

st.write("This is Analysis Page")
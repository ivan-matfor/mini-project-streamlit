import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df

# First some dogs Data Exploration
df_dogs = load_data(path="./data/raw/20200306_hundehalter.csv")
df_dogs = deepcopy(df_dogs)

# Add title and header
st.title("Welcome to my Mini Project with Streamlit")
st.header("Dogs in Zurich Data Exploration")

#st.table(data=df_dogs)
if st.checkbox("Let's see the Dataframe (click to expand)"):

    st.subheader("This dataset describes all the dogs registered in the city of Zurich:")
    st.dataframe(data=df_dogs)
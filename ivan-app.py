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

# loading json spatial data
with open("data/raw/stzh.adm_stadtkreise_a.json", "r", encoding="utf-8") as f:
    geojson_dogs = json.load(f)

# Format column to match json file
df_dogs["STADTKREIS"] = "Kreis " + df_dogs["STADTKREIS"].astype(str)

# Creating df to calculate density of dogs by Kreis
df_dogs_by_kreis = df_dogs.groupby("STADTKREIS", as_index=False).size().rename(columns={"size": "NUM DOG OWNERS"})


st.subheader("Number of dog owners by Kreis - Zurich")

# Constructing Map of Zurich with density of Dogs by Kreis
fig = px.choropleth_map(df_dogs_by_kreis, geojson=geojson_dogs, color="NUM DOG OWNERS",
                        locations="STADTKREIS", featureidkey="properties.bezeichnung",
                        center={"lat": 47.3769, "lon": 8.5417},
                        map_style="carto-positron", zoom=10, opacity=0.5,
                        hover_data={"STADTKREIS": True, "NUM DOGS": True},
                        color_continuous_scale="YlOrRd")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Showing on Streamlite
st.plotly_chart(fig, use_container_width=True)


# Top 15 Most popular Dog Breeds among owners

# Starting with a total

df_top_breeds = df_dogs.groupby("RASSE1").size().sort_values(ascending=False)

# then we pick the 15 of the previously sorted ones 

top15_breeds = df_top_breeds.head(15)

# now that we know the breeds, we can see the original dataframe by gender

top_breeds_gender = df_dogs[df_dogs["RASSE1"].isin(top15_breeds.index)]

#we build a df for the barchart with a column for gender

df_top_breeds_summary = top_breeds_gender.groupby(["RASSE1","GESCHLECHT"]).size().reset_index(name="count").sort_values("count",ascending=False)



st.subheader("Distribution of Popular Breeds by Owner's Gender in Zurich")

# distribution of top 15 breeds by owner's gender

fig_bar = px.bar(df_top_breeds_summary, 
                 x="RASSE1", 
                 y="count", 
                 color="GESCHLECHT", 
                 barmode="group",
                 labels={
                     "RASSE1": "Breed",
                     "count": "Number of Owners",
                     "GESCHLECHT": "Owner Gender"
                     })
fig_bar.update_layout(xaxis_title="Breed",yaxis_title="# Owners", legend_title_text="Owner Gender")

# showing second plot

st.plotly_chart(fig_bar, use_container_width=True)

# Zurich Dog Owners Dashboard

An interactive Streamlit dashboard to explore dog ownership patterns across Zurich's districts using open city data.

**Live app:** https://dog-density-zurich-ivan.streamlit.app

#### -- Project Status: Completed

## Overview

This project visualizes data from the City of Zurich's open data portal on registered dog owners. The app allows users to explore:

- **Dog density by district** — a choropleth map showing how many dogs are registered per Zurich Stadtkreis (district 1–12)
- **Popular breeds by gender** — a bar chart of the top 15 most common dog breeds filtered by the owner's gender

## Technologies

- Python
- Streamlit
- Pandas
- Plotly

## Data Source

- **Dataset:** [Hundehalter der Stadt Zürich](https://data.stadt-zuerich.ch) — 7,800+ records of registered dog owners with demographic info and dog characteristics
- **GeoJSON:** Administrative boundaries of Zurich's Stadtkreise for choropleth mapping

## Getting Started

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/mini-project-streamlit.git
   cd mini-project-streamlit
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run ivan-app.py
   ```

## Project Structure

```
mini-project-streamlit/
├── ivan-app.py               # Main Streamlit app
├── requirements.txt
└── data/
    └── raw/
        ├── 20200306_hundehalter.csv      # Dog owner records
        └── stzh.adm_stadtkreise_a.json  # Zurich district boundaries (GeoJSON)
```

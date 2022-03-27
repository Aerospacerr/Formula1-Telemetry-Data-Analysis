import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px
import fastf1
import matplotlib.pyplot as plt
import fastf1.plotting


##### Function Definitions ####

@st.cache(persist=True)
def load_data(select_year, select_race, select_session):

    selected_session = fastf1.get_session(select_year, select_race, select_session)

    return selected_session



##### Fast F1 Setup ####

# enable some matplotlib patches for plotting timedelta values and load
# FastF1's default color scheme
fastf1.plotting.setup_mpl()

st.set_page_config(page_title="Formula 1 Telemetry Analysis", page_icon='🚓',
                   layout='centered', initial_sidebar_state='collapsed')
st.title("F1 Telemetry Analysis")
st.markdown(
    "This application is a Streamlit dashboard that can be used to analyze F1 Telemetry Data")


# select necessary details for each race
st.header("Select Year")
values_year = [2020, 2021, 2022]
default_ix_year = values_year.index(2020)
select_year = st.selectbox('Championship Year', values_year, index=default_ix_year)
st.write(select_year)


st.header("Select Race Place")
values_place = ['Bahrain', 'Saudi Arabia']
default_ix_race = values_place.index('Bahrain')
select_race = st.selectbox('Race Places', values_place, index=default_ix_race)
st.write(select_race)

st.header("Select Session")
values_session = ['Q', 'R']
default_ix_session = values_session.index('Q')
select_session = st.selectbox('Sessions', values_session, index=default_ix_session)
st.write(select_session)

# load a session and its telemetry data
with st.spinner("Loading data..."):
    selected_session = load_data(select_year, select_race, select_session)
    st.write(selected_session)




### with st.spinner("Loading data..."):
###    selected_session = load_data(2022, 2, 'Q')

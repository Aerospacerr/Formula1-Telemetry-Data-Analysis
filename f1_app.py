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
select_year = st.selectbox('Championship Year', ['2020', '2021', '2022'], 2020)

st.header("Select Race")
select_race = st.selectbox('Race Places', ['Bahrain', '2'], 0)

st.header("Select Session")
select_session = st.selectbox('Sessions', ['Q', 'R'], 0)

# load a session and its telemetry data
with st.spinner("Loading data..."):
    selected_session = load_data(select_year, 2, 4)

st.write(selected_session)



### with st.spinner("Loading data..."):
###    selected_session = load_data(2022, 2, 'Q')

"""
query_persons_string = f'number_of_{select.lower().split()[0]}_{select.lower().split()[1]}'
st.write(filter_data_by_type_of_people(data, query_persons_string))

st.header("Select Race")
select_race = st.selectbox('Championship Year',['2020', '2021', '2022',])

@st.cache(persist=True)
def load_data():
    data = pd.read_parquet('crashes.parquet', engine='pyarrow')
    # drop rows with no lat/long values:
    data.dropna(subset=['latitude', 'longitude'], inplace=True)
    # drop rows outside bounding box of NYC:
    data = data[(data['latitude'] > 40.0) & (data['latitude'] < 42.0) &
                (data['longitude'] > -76.0) & (data['longitude'] < -70.0)]
    return data


@st.experimental_memo
def query_data_by_persons_injured(data, injured_people):
    return data.query(f'number_of_persons_injured >= {injured_people}')[["latitude", "longitude"]].dropna(how="any")


@st.experimental_memo
def filter_data_by_hour(data, year):
    return data[data['timestamp'].dt.hour == year]


@st.experimental_memo
def filter_data_by_type_of_people(data, type_of_people, amount=8):
    return data[(data[type_of_people] > 0)][['on_street_name', 'off_street_name', type_of_people]].sort_values(
        by=[type_of_people], ascending=False).dropna(thresh=2).fillna('')[:amount]


@st.experimental_memo
def filter_data_by_year(data, year):
    return data[data['timestamp'].dt.year == year]


with st.spinner("Loading data..."):
    data = load_data()

# select_year = st.selectbox('Please Select The Year',
#            ['2020', '2021', '2022'])
# data = filter_data_by_year(data, select_year)


st.header("Where are the most people injured in NYC")
max_injured_people = int(data['number_of_persons_injured'].max())
injured_people = st.slider("Number of persons injured in vehicle collisions", 0, max_injured_people)
data_by_persons_injured = query_data_by_persons_injured(data, injured_people)
st.map(data=data_by_persons_injured)

st.header("How many collisions occur during a given time of day?")
hour = st.slider("Hour to look at", 0, 23)
filtered_by_hour = filter_data_by_hour(data, hour)

st.markdown("Vehicle collisions between %i:00 and %i:00" % (hour, (hour + 1) % 24))
midpoint = (filtered_by_hour['latitude'].median(), filtered_by_hour['longitude'].median())
st.write(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state={
        "latitude": midpoint[0],
        "longitude": midpoint[1],
        "zoom": 11,
        "pitch": 50,
    },
    layers=[
        pdk.Layer(
            "HexagonLayer",
            data=filtered_by_hour[['timestamp', 'latitude', 'longitude']],
            get_position=['longitude', 'latitude'],
            radius=100,
            extruded=True,
            pickable=True,
            elevation_scale=4,
            elevation_range=[0, 1000],

        ),
    ],
))

st.subheader("Breakdown by minute between %i:00 and %i:00" % (hour, (hour + 1) % 24))

hist = np.histogram(filtered_by_hour['timestamp'].dt.minute, bins=60, range=(0, 60))[0]
chart_data = pd.DataFrame({'minute': range(60), 'crashes': hist})
fig = px.bar(chart_data, x='minute', y='crashes', hover_data=['minute', 'crashes'], height=400)
st.write(fig)

st.header("Top 5 dangerous streets by affected type")
select = st.selectbox('Affected type of people injured or killed',
                      ['Persons Injured', 'Persons Killed', 'Pedestrians Injured', 'Pedestrians Killed',
                       'Cyclist Injured', 'Cyclist Killed', 'Motorist Injured', 'Motorist Killed', ])

query_persons_string = f'number_of_{select.lower().split()[0]}_{select.lower().split()[1]}'
st.write(filter_data_by_type_of_people(data, query_persons_string))
"""


if st.checkbox("Show Raw Data", False):
    st.subheader('Raw Data')
    st.write(selected_session.head(100))  # limit to first 100 rows
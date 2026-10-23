# This creates the page for displaying data visualizations.

import json
import pandas as pd
import plotly.express as px
import streamlit as st

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visuals",
    page_icon="📈",
)

# PAGE TITLE
st.title("Data Visualizations 📈")


# PART 1: GRAPHS FROM data.json
# --- YOUR CODE GOES HERE ---
with open("data.json") as f:
    data = json.load(f)

df = pd.DataFrame(data["data_points"])
st.header(data["chart_title"])

# Static chart (advanced, Plotly bar)
totals = df.groupby("label")["value"].sum().reset_index()

fig = px.bar(
    totals, x="label", y="value",
    title="Total Wins, 2021-2025",
    labels={"label": "Team", "value": "Total Wins"},
)
st.plotly_chart(fig)

# Dynamic chart (line)
st.subheader("Wins Per Season")
st.selectbox("Choose a team", df["label"].unique(), key="team")
st.slider("Start season", 2021, 2025, 2021, key="start")

filtered = df[
    (df["label"] == st.session_state.team)
    & (df["season"] >= st.session_state.start)
]
logos = {
    "Bears": "images/bearslogo.png",
    "49ers": "images/49erslogo.png",
    "Texans": "images/texanslogo.png",
}
st.image(logos[st.session_state.team], width=100)
st.line_chart(filtered.set_index("season")["value"])


# PART 2: GRAPHS FROM data.csv
# --- YOUR CODE GOES HERE ---

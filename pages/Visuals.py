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
st.header("Survey Results")

try:
    survey = pd.read_csv("data.csv")
except (FileNotFoundError, pd.errors.EmptyDataError):
    survey = pd.DataFrame(columns=["team", "player", "games_watched"])

if survey.empty:
    st.info("No survey responses yet. Fill out the Survey page first.")
else:
    # Static chart (advanced, Plotly pie)
    fan_counts = survey["team"].value_counts().reset_index()
    fan_counts.columns = ["team", "fans"]

    pie = px.pie(
        fan_counts, names="team", values="fans",
        title="Favorite Teams Among Survey Respondents",
    )
    st.plotly_chart(pie)

    # Dynamic chart (bar)
    st.subheader("Games Watched Last Season")
    team_options = ["All"] + sorted(survey["team"].unique())
    st.selectbox("Show fans of:", team_options, key="p2_team")
    st.slider("Minimum games watched", 0, 17, 0, key="p2_min")

    filtered = survey[survey["games_watched"] >= st.session_state.p2_min]
    if st.session_state.p2_team != "All":
        filtered = filtered[filtered["team"] == st.session_state.p2_team]

    if filtered.empty:
        st.warning("No responses match those filters.")
    else:
        col1, col2 = st.columns(2)
        col1.metric("Mean games watched", round(filtered["games_watched"].mean(), 1))
        col2.metric("Median games watched", filtered["games_watched"].median())
        st.bar_chart(filtered, x="player", y="games_watched")

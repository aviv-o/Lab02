# This creates the main landing page for the Streamlit application.
# Contains an introduction to the project and guide users to other pages.

import streamlit as st

st.set_page_config(
    page_title="Homepage",
    page_icon="🏈",
)

# WELCOME PAGE TITLE
st.title("🏈 Web Development Lab02")

# INTRODUCTORY TEXT
st.write("""
CS 1301 - Web Development - Section C

Aviv Oshri

Welcome to my Streamlit Web Development Lab02 app! You can navigate
between the pages using the sidebar on the left. The pages are:

1. **Visuals**: Explore NFL wins per season (2021-2025) for the Bears,
   49ers, and Texans, with a bar chart of total wins and a line chart
   where you pick a team and a starting season. Below that, see charts
   of the survey responses: a pie chart of favorite teams and a bar chart
   of games watched, with the mean and median updating as you filter.
2. **Survey**: Tell me your favorite NFL team, your favorite player, and
   how many games you watched last season. Your answers are saved and show
   up on the Visuals page.
""")

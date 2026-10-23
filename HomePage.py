# This creates the main landing page for the Streamlit application.
# Contains an introduction to the project and guide users to other pages.

# Import Streamlit
import streamlit as st

# st.set_page_config() is used to configure the page's appearance in the browser tab.
# It's good practice to set this as the first Streamlit command in your script.
# Import Streamlit
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
   49ers, and Texans. A bar chart shows each team's total wins, and a
   line chart lets you pick a team and a starting season to see how its
   wins changed over time.
2. **Survey**: Enter your own data through the survey form. Your answers
   are saved and used for the graphs from the survey data.
""")

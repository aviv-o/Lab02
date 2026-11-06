# This creates the page for users to input data.
# The collected data should be appended to the 'data.csv' file.

import streamlit as st
import pandas as pd
import os # The 'os' module is used for file system operations (e.g. checking if a file exists).

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Survey",
    page_icon="📝",
)

# PAGE TITLE AND USER DIRECTIONS
st.title("NFL Fan Survey 🏈")
st.write("Please fill out the form below to add your answers to the dataset.")

# DATA INPUT FORM
TEAMS = ["Bears", "49ers", "Texans", "Chiefs", "Eagles", "Cowboys",
         "Packers", "Bills", "Other"]

with st.form("survey_form", clear_on_submit=True):
    team_input = st.selectbox("What's your favorite NFL team?", TEAMS)
    player_input = st.text_input("Who's your favorite player?")
    games_input = st.slider("How many games of your team did you watch last season?", 0, 17, 8)

    # The submit button for the form.
    submitted = st.form_submit_button("Submit Data")

    # This block of code runs ONLY when the submit button is clicked.
    if submitted:
        if player_input.strip() == "":
            st.warning("Please enter a player's name.")
        else:
            # 1. Create a new row of data from the three inputs.
            new_row = pd.DataFrame({
                "team": [team_input],
                "player": [player_input.strip().title()],
                "games_watched": [games_input],
            })

            # 2. Add it to the existing data and write the file back.
            if os.path.exists("data.csv") and os.path.getsize("data.csv") > 0:
                updated = pd.concat([pd.read_csv("data.csv"), new_row], ignore_index=True)
            else:
                updated = new_row
            updated.to_csv("data.csv", index=False)

            st.success("Your data has been submitted!")
            st.write(f"You entered: **Team:** {team_input}, **Player:** {player_input}, **Games watched:** {games_input}")


# DATA DISPLAY
# This section shows the current contents of the CSV file, which helps in debugging.
st.divider() # Adds a horizontal line for visual separation.
st.header("Current Data in CSV")

# Check if the CSV file exists and is not empty before trying to read it.
if os.path.exists('data.csv') and os.path.getsize('data.csv') > 0:
    # Read the CSV file into a pandas DataFrame.
    current_data_df = pd.read_csv('data.csv')
    # Display the DataFrame as a table.
    st.dataframe(current_data_df)
else:
    st.warning("The 'data.csv' file is empty or does not exist yet.")

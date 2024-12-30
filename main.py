import streamlit as st
import pandas as pd

# Load the CSV file
df = pd.read_csv("d22file.csv", sep=",")

# Set the page layout to wide
st.set_page_config(layout="wide")

# Define column proportions
col1, col2, col3, col4 = st.columns([0.5, 1.5, 0.5, 1.5])

# Add content to the columns
with col1:
    # Placeholder if you want to add something later
    st.write("")  # Empty for now

with col2:
    st.title("Incrk.com")
    st.image("image.jpg", width=400, caption="Title", use_container_width=False)

with col3:
    # Placeholder if you want to add something later
    st.write("")  # Empty for now

with col4:
    for index, row in df.iterrows():
        st.title(row["title"])
        st.image(row["image"], width=300, caption=row["title"], use_container_width=True)
        st.write(row["description"])

import streamlit as st
import pandas as pd

df = pd.read_csv("d22file.csv",sep=",")


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.title("Incrk.com")
    st.image("image.jpg", width=400, caption="Title", use_container_width=False)



with col2:
    for index, row in df.iterrows():
        st.title(row["title"])
        st.image(row["image"], width=300, caption=row["title"], use_container_width=False)

        st.write(row["description"])



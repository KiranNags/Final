
import streamlit as st
import streamlit.components.v1 as components

# Read the HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Streamlit App Title
st.set_page_config(page_title="Kiran Video Player", layout="wide")
st.title("Kiran Video Player with Conviva DPI Integration")

# Embed the HTML video player
components.html(html_content, height=800, scrolling=True)

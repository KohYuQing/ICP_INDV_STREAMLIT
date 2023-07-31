import streamlit 
import requests
import pandas 
import snowflake.connector
from urllib.error import URLError
streamlit.title('My Parents New Healthy Diner')
streamlit.subheader('Breakfast Favourites')
streamlit.markdown('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.markdown('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.markdown('🐔 Hard-Boiled Free-Range Egg')
streamlit.markdown('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import joblib
from joblib import load
import pickle
from sklearn import preprocessing

st.set_page_config(page_title='Singapore Airbnb Price Predictor', page_icon=':money_with_wings:')
st.sidebar.title("Airbnb Singapore Listings: house (room) prices and locations")
st.sidebar.markdown("This web app allows you to explore the Airbnb listings in Singapore. You can filter the listings by a price range between $70-180, neighbourhoods and room type. You can also view the listings on a map in the 'Explore' tab and make predictions in the 'Predict' tab.")
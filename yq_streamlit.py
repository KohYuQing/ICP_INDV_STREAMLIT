import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import joblib
from joblib import load
import pickle
from sklearn import preprocessing

st.set_page_config(page_title='Singapore Airbnb Price Predictor', page_icon=':money_with_wings:')
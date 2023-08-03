import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import joblib
from joblib import load
import pickle
from sklearn import preprocessing
import requests
import zipfile
import io

st.set_page_config(page_title='Singapore Airbnb Price Predictor', page_icon=':money_with_wings:')
st.sidebar.title("Airbnb Singapore Listings: house (room) prices and locations")
st.sidebar.markdown("This web app allows you to explore the Airbnb listings in Singapore. You can filter the listings by a price range between $70-180, neighbourhoods and room type. You can also view the listings on a map in the 'Explore' tab and make predictions in the 'Predict' tab.")

@st.cache_data
def load_data():
    # First load the original airbnb listtings dataset
    data = pd.read_csv("final_data_noscaler.csv") #use this for the original dataset, before transformations and cleaning
    return data


def read_csv_from_zipped_github(url):
    # Send a GET request to the GitHub URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Create a BytesIO object from the response content
        zip_file = io.BytesIO(response.content)

        # Extract the contents of the zip file
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            # Assume there is only one CSV file in the zip archive (you can modify this if needed)
            csv_file_name = zip_ref.namelist()[0]
            with zip_ref.open(csv_file_name) as csv_file:
                # Read the CSV data into a Pandas DataFrame
                df = pd.read_csv(csv_file)

        return df
    else:
        st.error(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
        return None

def main():
    st.title("Read CSV from Zipped File on GitHub")

    # Replace the 'github_url' variable with the actual URL of the zipped CSV file on GitHub
    github_url = "https://github.com/KohYuQing/ICP_INDV_STREAMLIT/raw/main/snowflake_data.zip"
    df = read_csv_from_zipped_github(github_url)

def load_pickled_object(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)


data = load_data()
maintable = main()

with open('xgbr_gs.pkl', 'rb') as file:
    xgbr_gs = joblib.load(file)
with open('scaler.pkl', 'rb') as file:
    scaler = joblib.load(file)
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import joblib
from joblib import load
import pickle
from xgboost import XGBRegressor 
import requests
import zipfile
import io

# st.set_page_config(page_title='Singapore Airbnb Price Predictor', page_icon=':money_with_wings:')
# st.sidebar.title("Airbnb Singapore Listings: house (room) prices and locations")
# st.sidebar.markdown("This web app allows you to explore the Airbnb listings in Singapore. You can filter the listings by a price range between $70-180, neighbourhoods and room type. You can also view the listings on a map in the 'Explore' tab and make predictions in the 'Predict' tab.")

# @st.cache_data
# def load_data():
#     # First load the original airbnb listtings dataset
#     data = pd.read_csv("final_data_noscaler.csv") #use this for the original dataset, before transformations and cleaning
#     return data


# def read_csv_from_zipped_github(url):
#     # Send a GET request to the GitHub URL
#     response = requests.get(url)

#     # Check if the request was successful
#     if response.status_code == 200:
#         # Create a BytesIO object from the response content
#         zip_file = io.BytesIO(response.content)

#         # Extract the contents of the zip file
#         with zipfile.ZipFile(zip_file, 'r') as zip_ref:
#             # Assume there is only one CSV file in the zip archive (you can modify this if needed)
#             csv_file_name = zip_ref.namelist()[0]
#             with zip_ref.open(csv_file_name) as csv_file:
#                 # Read the CSV data into a Pandas DataFrame
#                 df = pd.read_csv(csv_file)

#         return df
#     else:
#         st.error(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
#         return None

# def main():
#     st.title("Read CSV from Zipped File on GitHub")

#     # Replace the 'github_url' variable with the actual URL of the zipped CSV file on GitHub
#     github_url = "https://github.com/KohYuQing/ICP_INDV_STREAMLIT/raw/main/snowflake_data.zip"
#     df = read_csv_from_zipped_github(github_url)


# data = load_data()
# maintable = main()

# with open('xgbr_gs.pkl', 'rb') as file:
#     xgbr_gs = joblib.load(file)
# with open('scaler.pkl', 'rb') as file:
#     scaler = joblib.load(file)

# df = pd.read_csv('final_data_noscaler.csv')
# total_sales = df[['TOTAL_SALES_PER_ITEM']]


# LOCATION_ID = df['LOCATION_ID']
# SHIFT_NUMBER= df['SHIFT_NUMBER']
# AVG_TEMPERATURE_AIR_2M_F = df['AVG_TEMPERATURE_AIR_2M_F']
# AVG_TEMPERATURE_WETBULB_2M_F = df['AVG_TEMPERATURE_WETBULB_2M_F']
# AVG_TEMPERATURE_DEWPOINT_2M_F= df['AVG_TEMPERATURE_DEWPOINT_2M_F']
# AVG_TEMPERATURE_WINDCHILL_2M_F = df['AVG_TEMPERATURE_WINDCHILL_2M_F']
# AVG_WIND_SPEED_100M_MPH  = df['AVG_WIND_SPEED_100M_MPH']
# COG_PER_ITEM_USD =df['COG_PER_ITEM_USD']
# ITEM_PRICE = df['ITEM_PRICE']
# VALUE = df['VALUE']
# SUBCATEGORY = df['SUBCATEGORY']
# discount = df['discount_10%']            
# # Define the user input functions 

# season_mapping = {'WINTER': 0, 'SPRING': 1, 'SUMMER': 2, 'AUTUMN': 3}
# season_reverse_mapping = {v: k for k, v in season_mapping.items()}
# season_labels = list(season_mapping.keys())
# season_values = list(season_mapping.values())

# city_mapping = {'San Mateo': 0, 'Denver': 1, 'Seattle': 2, 'New York City': 3, 'Boston': 4}
# city_reverse_mapping = {v: k for k, v in city_mapping.items()}
# city_labels = list(city_mapping.keys())

# itemcat_mapping = {'Dessert': 0, 'Beverage': 1, 'Main': 2, 'Snack': 3}
# itemcat_reverse_mapping = {v: k for k, v in itemcat_mapping.items()}
# itemcat_labels = list(itemcat_mapping.keys())

# menut_mapping = {'Ice Cream': 0, 'Grilled Cheese': 1, 'BBQ': 2, 'Tacos': 3, 'Chinese': 4, 'Poutine': 5, 'Hot Dogs': 6, 'Vegetarian': 7, 'Crepes': 8, 'Sandwiches': 9, 'Ramen': 10, 'Ethiopian': 11, 'Gyros': 12, 'Indian': 13, 'Mac & Cheese': 14}
# menut_reverse_mapping = {v: k for k, v in menut_mapping.items()}
# menut_labels = list(menut_mapping.keys())

# truckb_mapping = {'Freezing Point': 0, 'The Mega Melt': 1, 'Smoky BBQ': 2, "Guac n' Roll": 3, 'Peking Truck': 4, 'Revenge of the Curds': 5, 'Not the Wurst Hot Dogs': 6, 'Plant Palace': 7, 'Le Coin des Crêpes': 8, 'Better Off Bread': 9, 'Kitakata Ramen Bar': 10, 'Tasty Tibs': 11, 'Cheeky Greek': 12, "Nani's Kitchen": 13, 'The Mac Shack': 14}
# truckb_reverse_mapping = {v: k for k, v in truckb_mapping.items()}
# truckb_labels = list(truckb_mapping.keys())
# truckb_values = list(truckb_mapping.values())

# menuitem_mapping = {'Mango Sticky Rice': 0, 'Popsicle': 1, 'Waffle Cone': 2, 'Sugar Cone': 3, 'Two Scoop Bowl': 4, 'Lemonade': 5, 'Bottled Water': 6, 'Ice Tea': 7, 'Bottled Soda': 8, 'Ice Cream Sandwich': 9, 'The Ranch': 10, 'Miss Piggie': 11, 
#                     'The Original': 12, 'Three Meat Plate': 13, 'Fried Pickles': 14, 'Two Meat Plate': 15, 'Spring Mix Salad': 16, 'Rack of Pork Ribs': 17, 'Pulled Pork Sandwich': 18, 'Fish Burrito': 19, 'Veggie Taco Bowl': 20, 'Chicken Burrito': 21, 'Three Taco Combo Plate': 22,
#                     'Two Taco Combo Plate': 23, 'Lean Burrito Bowl': 24, 'Combo Lo Mein': 25, 'Wonton Soup': 26, 'Combo Fried Rice': 27, 'The Classic': 28, 'The Kitchen Sink': 29, 'Mothers Favorite': 30, 'New York Dog': 31, 'Chicago Dog': 32, 'Coney Dog': 33, 'Veggie Burger': 34,
#                     'Seitan Buffalo Wings': 35, 'The Salad of All Salads': 36, 'Breakfast Crepe': 37, 'Chicken Pot Pie Crepe': 38, 'Crepe Suzette': 39, 'Hot Ham & Cheese': 40, 'Pastrami': 41, 'Italian': 42, 'Creamy Chicken Ramen': 43, 'Spicy Miso Vegetable Ramen': 44, 'Tonkotsu Ramen': 45,
#                     'Veggie Combo': 46, 'Lean Beef Tibs': 47, 'Lean Chicken Tibs': 48, 'Gyro Plate': 49, 'Greek Salad': 50, 'The King Combo': 51, 'Tandoori Mixed Grill': 52, 'Lean Chicken Tikka Masala': 53, 'Combination Curry': 54, 'Lobster Mac & Cheese': 55, 'Standard Mac & Cheese': 56, 
#                     'Buffalo Mac & Cheese': 57}
# menuitem_reverse_mapping = {v: k for k, v in menuitem_mapping.items()}
# menuitem_labels = list(menuitem_mapping.keys())



# def get_city():
#     city = st.selectbox('Select a city', city_labels)
#     return city
# city_input = get_city()
# city_int = city_mapping[city_input]

# def get_itemcat():
#     itemcat = st.selectbox('Select a Item Category', itemcat_labels)
#     return itemcat
# itemcat_input = get_itemcat()
# itemcat_int = itemcat_mapping[itemcat_input]

# def get_menut():
#     menut = st.selectbox('Select a Menu Type', menut_labels)
#     return menut
# menut_input = get_menut()
# menut_int = menut_mapping[menut_input]

# def get_truckb():
#     truckb = st.selectbox('Select a Truck Brand Name', truckb_labels)
#     return truckb
# truckb_input = get_truckb()
# truckb_int = truckb_mapping[truckb_input]

# def get_season():
#     season = st.selectbox('Select a season', season_labels)
#     return season
# season_input = get_season()
# season_int = season_mapping[season_input]


# filtered_rows = []
# for index, row in df.iterrows():
#     if (row['TRUCK_BRAND_NAME'] in truckb_values) & (row['SEASON'] in season_values):
#         filtered_rows.append(row)


# filtered_rows = pd.DataFrame(columns=df.columns)
# if st.button('Generate Records'):
#     st.write(filtered_rows)






# def get_menuitem():
#     menuitem = st.selectbox('Select a Menu Item', menuitem_labels)
#     return menuitem
# menuitem_input = get_menuitem()
# menuitem_int = menuitem_mapping[menuitem_input]

# if st.button('Predict Price'):
#     input_data = [[menuitem_int,truckb_int,menut_int,itemcat_int,
#                    city_int,season_int]]
    
#     input_df = pd.DataFrame(input_data, columns=['MENU_ITEM_NAME',
#                                                  'TRUCK_BRAND_NAME','MENU_TYPE','ITEM_CATEGORY','CITY','SEASON'])
#     prediction = xgbr_gs.predict(input_df)


st.set_page_config(page_title='INVEMP Tasty Bytes Group 5', page_icon='🍖🍕🍜')

st.sidebar.title("INVEMP: Inventory/Warehouse Management & Prediction on Sales per Menu Item")
st.sidebar.markdown("This web app allows you to explore the internal inventory of Tasty Bytes. You can explore these functions in the web app (Description of Page)")

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Prediction A', 'Prediction B', 'Prediction C', 'Prediction D', 'Prediction E'])

with tab1:
  st.write('hello')
with tab2:
  #Tab 2 code here
  #Hector/Shahid
  st.write('hello')
with tab3:
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

        # Replace the 'github_url' variable with the actual URL of the zipped CSV file on GitHub
        github_url = "https://github.com/KohYuQing/ICP_INDV_STREAMLIT/raw/main/final_data.zip"
        df = read_csv_from_zipped_github(github_url)


    data = load_data()
    github_url = "https://github.com/KohYuQing/ICP_INDV_STREAMLIT/raw/main/final_data.zip"
    maintable = read_csv_from_zipped_github(github_url)

    with open('xgbr_gs.pkl', 'rb') as file:
        xgbr_gs = joblib.load(file)
    with open('scaler.pkl', 'rb') as file:
        scaler = joblib.load(file)

    df = pd.read_csv('final_data_noscaler.csv')
    total_sales = df[['TOTAL_SALES_PER_ITEM']]


    LOCATION_ID = df['LOCATION_ID']
    SHIFT_NUMBER= df['SHIFT_NUMBER']
    AVG_TEMPERATURE_AIR_2M_F = df['AVG_TEMPERATURE_AIR_2M_F']
    AVG_TEMPERATURE_WETBULB_2M_F = df['AVG_TEMPERATURE_WETBULB_2M_F']
    AVG_TEMPERATURE_DEWPOINT_2M_F= df['AVG_TEMPERATURE_DEWPOINT_2M_F']
    AVG_TEMPERATURE_WINDCHILL_2M_F = df['AVG_TEMPERATURE_WINDCHILL_2M_F']
    AVG_WIND_SPEED_100M_MPH  = df['AVG_WIND_SPEED_100M_MPH']
    COG_PER_ITEM_USD =df['COG_PER_ITEM_USD']
    ITEM_PRICE = df['ITEM_PRICE']
    VALUE = df['VALUE']
    SUBCATEGORY = df['SUBCATEGORY']
    discount = df['discount_10%']            
    # Define the user input functions 

    season_mapping = {'WINTER': 0, 'SPRING': 1, 'SUMMER': 2, 'AUTUMN': 3}
    season_reverse_mapping = {v: k for k, v in season_mapping.items()}
    season_labels = list(season_mapping.keys())
    season_values = list(season_mapping.values())

    city_mapping = {'San Mateo': 0, 'Denver': 1, 'Seattle': 2, 'New York City': 3, 'Boston': 4}
    city_reverse_mapping = {v: k for k, v in city_mapping.items()}
    city_labels = list(city_mapping.keys())
    city_values = list(city_mapping.values())

    itemcat_mapping = {'Dessert': 0, 'Beverage': 1, 'Main': 2, 'Snack': 3}
    itemcat_reverse_mapping = {v: k for k, v in itemcat_mapping.items()}
    itemcat_labels = list(itemcat_mapping.keys())

    menut_mapping = {'Ice Cream': 0, 'Grilled Cheese': 1, 'BBQ': 2, 'Tacos': 3, 'Chinese': 4, 'Poutine': 5, 'Hot Dogs': 6, 'Vegetarian': 7, 'Crepes': 8, 'Sandwiches': 9, 'Ramen': 10, 'Ethiopian': 11, 'Gyros': 12, 'Indian': 13, 'Mac & Cheese': 14}
    menut_reverse_mapping = {v: k for k, v in menut_mapping.items()}
    menut_labels = list(menut_mapping.keys())

    truckb_mapping = {'Freezing Point': 0, 'The Mega Melt': 1, 'Smoky BBQ': 2, "Guac n' Roll": 3, 'Peking Truck': 4, 'Revenge of the Curds': 5, 'Not the Wurst Hot Dogs': 6, 'Plant Palace': 7, 'Le Coin des Crêpes': 8, 'Better Off Bread': 9, 'Kitakata Ramen Bar': 10, 'Tasty Tibs': 11, 'Cheeky Greek': 12, "Nani's Kitchen": 13, 'The Mac Shack': 14}
    truckb_reverse_mapping = {v: k for k, v in truckb_mapping.items()}
    truckb_labels = list(truckb_mapping.keys())
    truckb_values = list(truckb_mapping.values())

    menuitem_mapping = {'Mango Sticky Rice': 0, 'Popsicle': 1, 'Waffle Cone': 2, 'Sugar Cone': 3, 'Two Scoop Bowl': 4, 'Lemonade': 5, 'Bottled Water': 6, 'Ice Tea': 7, 'Bottled Soda': 8, 'Ice Cream Sandwich': 9, 'The Ranch': 10, 'Miss Piggie': 11, 
                        'The Original': 12, 'Three Meat Plate': 13, 'Fried Pickles': 14, 'Two Meat Plate': 15, 'Spring Mix Salad': 16, 'Rack of Pork Ribs': 17, 'Pulled Pork Sandwich': 18, 'Fish Burrito': 19, 'Veggie Taco Bowl': 20, 'Chicken Burrito': 21, 'Three Taco Combo Plate': 22,
                        'Two Taco Combo Plate': 23, 'Lean Burrito Bowl': 24, 'Combo Lo Mein': 25, 'Wonton Soup': 26, 'Combo Fried Rice': 27, 'The Classic': 28, 'The Kitchen Sink': 29, 'Mothers Favorite': 30, 'New York Dog': 31, 'Chicago Dog': 32, 'Coney Dog': 33, 'Veggie Burger': 34,
                        'Seitan Buffalo Wings': 35, 'The Salad of All Salads': 36, 'Breakfast Crepe': 37, 'Chicken Pot Pie Crepe': 38, 'Crepe Suzette': 39, 'Hot Ham & Cheese': 40, 'Pastrami': 41, 'Italian': 42, 'Creamy Chicken Ramen': 43, 'Spicy Miso Vegetable Ramen': 44, 'Tonkotsu Ramen': 45,
                        'Veggie Combo': 46, 'Lean Beef Tibs': 47, 'Lean Chicken Tibs': 48, 'Gyro Plate': 49, 'Greek Salad': 50, 'The King Combo': 51, 'Tandoori Mixed Grill': 52, 'Lean Chicken Tikka Masala': 53, 'Combination Curry': 54, 'Lobster Mac & Cheese': 55, 'Standard Mac & Cheese': 56, 
                        'Buffalo Mac & Cheese': 57}
    menuitem_reverse_mapping = {v: k for k, v in menuitem_mapping.items()}
    menuitem_labels = list(menuitem_mapping.keys())



    # def get_city():
    #     city = st.selectbox('Select a city', city_labels)
    #     return city
    # city_input = get_city()
    # city_int = city_mapping[city_input]

    # def get_itemcat():
    #     itemcat = st.selectbox('Select a Item Category', itemcat_labels)
    #     return itemcat
    # itemcat_input = get_itemcat()
    # itemcat_int = itemcat_mapping[itemcat_input]

    # def get_menut():
    #     menut = st.selectbox('Select a Menu Type', menut_labels)
    #     return menut
    # menut_input = get_menut()
    # menut_int = menut_mapping[menut_input]
    def get_CITY():
        city = st.selectbox('Select a City', city_labels)
        return city
    city_input = get_CITY()
    city_int = city_mapping[city_input]

    def get_truckb():
        truckb = st.selectbox('Select a Truck Brand Name', truckb_labels)
        return truckb
    truckb_input = get_truckb()
    truckb_int = truckb_mapping[truckb_input]

    def get_season():
        season = st.selectbox('Select a season', season_labels)
        return season
    season_input = get_season()
    season_int = season_mapping[season_input]



    filtered_rows = []
    for index, row in maintable.iterrows():
        if (truckb_input in row['TRUCK_BRAND_NAME']) & (season_input in row['SEASON'] )& (city_input in row['CITY']):
            filtered_rows.append(row)


    filtered_df = pd.DataFrame(filtered_rows, columns=df.columns)
    if st.button('Generate Records'):
        st.write(filtered_df)

  #Tab 3 code here

with tab4:
  #Tab 4 code here
  st.write('hello')

with tab5:
  #Tab 5 code here
  st.write('hello')
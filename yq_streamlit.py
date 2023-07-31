import streamlit as st
import pandas as pd
import numpy as np
import requests
import snowflake.connector
from urllib.error import URLError

st.set_page_config(page_title='INVEMP Tasty Bytes Group 5', page_icon='🍖🍕🍜')

st.sidebar.title("INVEMP: Inventory/Warehouse Management & Prediction on Sales per Menu Item")
st.sidebar.markdown("This web app allows you to explore the internal inventory of Tasty Bytes. You can explore these functions in the web app (Description of Page)")

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Prediction A', 'Prediction B', 'Prediction C', 'Prediction D', 'Prediction E'])

with tab1:
  #Tab 1 code here
  #Hector/Shahid
with tab2:
  #Tab 2 code here
  #Hector/Shahid
with tab3:
  #Tab 3 code here

with tab4:
  #Tab 4 code here

with tab5:
  #Tab 5 code here

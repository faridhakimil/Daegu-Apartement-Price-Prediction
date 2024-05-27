# Deploy Used Apartement Predictor

# ======================================================
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.tree import DecisionTreeRegressor
import pickle
# ======================================================

# Title
st.write('''
# APARTEMENT PRICE RECOMMENDATION
''')

# ======================================================
hallway_type = ['terraced', 'mixed', 'corridor']


time_tosubway = ['0-5min', '10-15min', '15-20min', '5-10min', 'no_bus_stop_nearby']

subway_station = ['Kyungbuk-uni-hospital', 'Chil-sung-market', 'Bangoge', 'Sin-nam',
       'Banwoldang', 'no-subway-nearby', 'Myung-duk', 'Daegu']

facilities_etc          = [0, 1, 2, 3, 4, 5]

facilities_publicoffice = [0, 1, 2, 3, 4, 5, 6, 7]

facilities_school       = [0, 1, 2, 3, 4, 5]

facilities_apartement   = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

facilities_parking      = [1270.,    0.,   56.,  798.,  536.,  605.,  203.,  108., 1174.,
        930.,  475.,  184.,  400.,  218., 1321.,  524.,   76.,   79.,
        181.,   18.]

year_built              = [2007, 1986, 1997, 2005, 2006, 2009, 2014, 1993, 2013, 2008, 2015,
       1978, 1985, 1992, 2003, 1980]

size                    = [1387,  914,  558, 1743, 1334,  572,  910,  288, 1131,  843, 1160,
        644,  829,  743,  868, 1629, 1690, 1273, 1483,  156, 1412, 1394,
        903,  676,  355, 1419,  640, 1184, 1167,  135,  818,  206, 1643,
        907, 1377, 1252,  451,  587,  811,  508,  576, 1366, 1103,  426,
        281, 1327, 1092,  857, 1149, 1088, 1288, 1761, 1437, 1291,  636,
        814,  871, 1519, 1444, 1451, 1448, 1313, 1256, 1796, 1192, 1035,
        846,  273,  277,  779,  498,  736,  138,  430,  213,  163, 1369,
        192,  547,  839,  160,  793, 1085, 1060,  832]

# ======================================================

# Sidebar
st.sidebar.header("Please input the apartement's feature")

def apartement_input():

    ## Numerical feature
    Fasilitas_ETC           = st.sidebar.number_input(label= "Fasilitas_ETC"          , min_value= 0    , max_value= 10, value= 4)
    Fasilitas_Public_Office = st.sidebar.number_input(label= "Fasilitas_Public_Office", min_value= 0    , max_value= 10, value= 5)
    Fasilitas_School        = st.sidebar.number_input(label= "Fasilitas_School"       , min_value= 0    , max_value= 10, value= 3)
    Fasilitas_Apartement    = st.sidebar.number_input(label= "Fasilitas_Apartement"   , min_value= 0    , max_value= 10, value= 2)
    Fasilitas_Parking_Lot   = st.sidebar.number_input(label= "Fasilitas_Parking_Lot"  , min_value= 0    , max_value= 1400, value= 1000)
    Year_Built              = st.sidebar.number_input(label= "Year_Built"             , min_value= 1978 , max_value= 2015, value= 2005)
    Size                    = st.sidebar.number_input(label= "Size"                   , min_value= 135  , max_value= 1796, value= 900)

    ## Categorical feature
    Hallway     = st.sidebar.selectbox(label= "Hallway" , options= (hallway_type))
    Time        = st.sidebar.selectbox(label= "Time"    , options= (time_tosubway))
    Subway      = st.sidebar.selectbox(label= "Subway"  , options= (subway_station))

        
    st.subheader("Apartement Features")
    df = pd.DataFrame()
    df['Fasilitas_ETC']             = [Fasilitas_ETC]
    df["Fasilitas_Public_Office"]   = [Fasilitas_Public_Office]
    df["Fasilitas_School"]          = [Fasilitas_School]
    df["Fasilitas_Apartement"]      = [Fasilitas_Apartement]
    df["Fasilitas_Parking_Lot"]     = [Fasilitas_Parking_Lot]
    df["Year_Built"]                = [Year_Built]
    df["Size"]                      = [Size]
    df["Hallway"]                   = [Hallway]
    df["Time"]                      = [Time]
    df["Subway"]                    = [Subway]
    
    return df

df_apartement = apartement_input()
df_apartement.index = ['value']

# Apartement price recommendation

model_loaded = pickle.load(open(r'C:\Users\LENOVO\Desktop\OLD - DATA SCIENTIST\Capstone\Modul 3\model_dectree_Hakimil.sav', 'rb'))

col1, col2 = st.columns(2)

# Left column (col1)
with col1:
    st.write(df_apartement.transpose())

with col2:
    st.header("Prediction")

    if st.button("Recommend"):
        recommendation = model_loaded.predict(df_apartement)
        if recommendation > 0:
            st.success("The recommended price is {:.2f} Won".format(recommendation[0]))
        else:
            st.write("Something went wrong, please try again.")
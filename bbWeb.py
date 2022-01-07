﻿# Benzín Brno - Web - streamlit app - bbWeb.py
#
# streamlit run bbWeb.py

# from bbCFG import *
# from bbLST import *

from bbCFG import bbName, bbNmBB, bbNmVE, bbNmDE, bbXlsFlNm, bbXlsShNm
from bbLST import bbHLAVICKA, bbBenzinky, bbHlavCena, bbHlavNazv, bbHlavDate, bbHlavaUrl

import pandas as pd
import streamlit as st
import plotly.express as px
# from PIL import Image
# import time

help_input = r'''
  to run:
set ccd=%cd%
cd    c:\aaC\vEnv\vEnvPy
vEnv\Scripts\activate
cd %ccd%
streamlit run bbWeb.py
'''

# Excel file Tabulka
# df = pd.read_excel(bbXlsFlNm, sheet_name=bbXlsShNm)
df = pd.read_excel(bbXlsFlNm, sheet_name=bbXlsShNm,
                   converters={bbHLAVICKA[bbHlavDate]: pd.to_datetime, bbHLAVICKA[bbHlavaUrl]: str})
# Hlavicka posledni bunka - 'Last status check on: '
LastChech = str(list(df)[-1:][0])
# Prices
Prices = 'Prices - ' + LastChech

# Titulek
st.set_page_config(page_title=bbName)
st.header(bbNmBB + bbNmVE)
st.subheader(bbNmDE)
st.text('\n')


# Excel file Tabulka
st.subheader(Prices)
# How to get a value from a Pandas DataFrame and not the index and object type - https://bit.ly/3BhmuDc
# st.dataframe(df.values)
# st.dataframe(df.style.hide_index())
# st.dataframe(df.style.highlight_max(axis=0))
# st.dataframe(df.style.highlight_min(color='lightgreen'))
# st.dataframe(df.style.highlight_min(subset=df['Cena']))
# Verze s background_gradient
st.dataframe(df.style.background_gradient().hide_index())
#  Test
# st.dataframe(df)
# st.dataframe(df.style.background_gradient().hide_index())
st.text('\n')
st.text('\n')

# Bar chart
st.subheader('Bar chart')
# --- PLOT BAR CHART
bar_chart = px.bar(df,
                   x=bbHLAVICKA[bbHlavCena],
                   y=bbHLAVICKA[bbHlavNazv],
                   text=bbHLAVICKA[bbHlavCena],
                   #  title=Prices + bbNmBB + bbNmVE+' '+LastChech,
                   title=Prices,
                   color=bbHLAVICKA[bbHlavCena],
                   category_orders={bbHLAVICKA[bbHlavNazv]: ((list(zip(*bbBenzinky)))[0])})
st.plotly_chart(bar_chart)


# End
st.text('(c) '+bbName)

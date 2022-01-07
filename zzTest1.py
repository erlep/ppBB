# Benzín Brno - Web - streamlit app - bbWeb.py
#
# streamlit run bbWeb.py

# from bbCFG import *
# from bbLST import *

from bbCFG import bbName, bbNmBB, bbNmVE, bbNmDE, bbDateDMY, bbXlsFlNm, bbXlsShNm
from bbLST import bbHLAVICKA, bbBenzinky, bbHlavCena, bbHlavNazv

import pandas as pd
import streamlit as st
import plotly.express as px
# from PIL import Image
import time

help_input = r'''
  to run:
set ccd=%cd%
cd    c:\aaC\vEnv\vEnvPy
vEnv\Scripts\activate
cd %ccd%
streamlit run bbWeb.py
'''

# Excel file Tabulka
df = pd.read_excel(bbXlsFlNm, sheet_name=bbXlsShNm)
# Hlavicka posledni bunka - 'Last status check on: '
LastChech = str(list(df)[-1:][0])
print(LastChech, type(LastChech))

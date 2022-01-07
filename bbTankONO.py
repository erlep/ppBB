﻿# Benzín Brno - TankONO - Natural "95" - pumpa: 'ČS Brno-Hviezdoslavova' - bbTankONO.py
# http://www.tank-ono.cz/cz/index.php?page=cenik

# from bbCFG import bbprint
# from bbCFG import bbProduct
# import requests
# # from bs4 import BeautifulSoup
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from unicodedata import normalize

# extract - stahne stranku
def extract(url, Key):
  import requests
  import pandas as pd

  # requests - nacte stranku
  # url = r'http://www.tank-ono.cz/cz/index.php?page=cenik'
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
  r = requests.get(url, headers)

  # pd najde tabulky
  table = pd.read_html(r.content, attrs={"class": "cenik"})
  # print(f'Total tables: {len(table)}')

  # tabulek je 2, zajima me c. 1
  df = table[0]
  # df.info()
  # df.head()

  # adding column name to the respective columns - https://bit.ly/3oxfuhN
  df.columns = ['Name', 'Cena91', 'Cena95', 'Cena95+', 'Cena98', 'CenaD', 'CenaD+', 'CenaAdB', 'CenaLPG', 'CenaM1', 'CenaM2']

  # Key = 'ČS Brno-Hviezdoslavova'
  Radek = df.loc[df['Name'] == Key]
  # How to get a value from a Pandas DataFrame and not the index and object type - https://bit.ly/3BhmuDc
  item = Radek['Cena95'].values[0]

  # 3350 => 33.50
  item = float(item) / 100
  # print("item:", item, '|| type:', type(item))
  # Cena
  # Cena = bbCenaMsk.format(item)
  Cena = item
  # print("Cena:", Cena, '|| type:', type(Cena))
  # print('Cena paliva -', Key, '- je:', Cena )
  return Cena

# test function
def tTankO(url=''):
  from bbCFG import brint, bbProduct
  brint('tTankO:', 'url', url)
  if bbProduct:
    return TankO(url)
  else:
    # s = '19.9' + '   url: ' + url
    # return s
    return 19.9

# TankONO - vrati cenu za Natural "95" - pumpa: 'ČS Brno-Hviezdoslavova' - http://www.tank-ono.cz/cz/index.php?page=cenik
def TankO(url=''):
  url = r'http://www.tank-ono.cz/cz/index.php?page=cenik'
  Key = 'ČS Brno-Hviezdoslavova'
  Cena = extract(url, Key)
  # print('Cena paliva -', Key, '- je:', Cena)
  return Cena

# main
def bbTankONO_main():
  print('def TankO(): ', tTankO('zz'))
  print('OkDone.')

# name__
if __name__ == '__main__':
  bbTankONO_main()

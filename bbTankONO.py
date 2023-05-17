# Benzín Brno - TankONO - Natural "95" - pumpa: 'ČS Brno-Hviezdoslavova' - bbTankONO.py
# http://www.tank-ono.cz/cz/index.php?page=cenik
# 18.05.2022 - zmena na asyncio, trio nelze s playwright

import asyncio
from bbCena import tF

# extract - stahne stranku
async def extract(url, Key):
  import requests
  import pandas as pd

  # requests - nacte stranku
  # url = r'http://www.tank-ono.cz/cz/index.php?page=cenik'
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
  r = requests.get(url, headers)

  # pd najde tabulky
  table = pd.read_html(r.content, attrs={"class": "cenik"})
  # print(f'Total tables: {len(table)}')

  # tabulky jsou 4, zajima me c. 0
  df = table[0]
  # print('\n\ninfo \n\n')
  # df.info()
  # print('head \n\n')
  # df.head()

  # adding column name to the respective columns - https://bit.ly/3oxfuhN
  df.columns = ['Name', 'Cena91', 'Cena95', 'Cena95+', 'Cena98', 'CenaD', 'CenaD+', 'CenaAdB', 'CenaLPG', 'CenaM1', 'CenaM2']
  # Key = 'ČS Brno-Hviezdoslavova'
  Radek = df.loc[df['Name'] == Key]
  # print('Radek', Radek)
  # How to get a value from a Pandas DataFrame and not the index and object type - https://bit.ly/3BhmuDc
  # item = Radek['Cena95'].values[0]
  item = Radek.iloc[:, 1].values[0]
  # print('item', item)

  # 3350 => 33.50
  item = float(item) / 100
  # print("item:", item, '|| type:', type(item))
  # Cena
  Cena = item
  # print("Cena:", Cena, '|| type:', type(Cena))
  return Cena

# test function
async def tTankO(url=''):
  from bbCFG import brint, bbProduct, bbNoUrl
  brint('jsem v tTankO  url', url)
  if bbProduct and (url != bbNoUrl):
    return await TankO(url)
  else:
    return 19.9

# TankONO - vrati cenu za Natural "95" - pumpa: 'ČS Brno-Hviezdoslavova' - http://www.tank-ono.cz/cz/index.php?page=cenik
async def TankO(url=''):
  url = r'http://www.tank-ono.cz/cz/index.php?page=cenik'
  Key = 'ČS Brno-Hviezdoslavova'
  Cena = extract(url, Key)
  # print('Cena paliva -', Key, '- je:', Cena)
  return await Cena

# main
# tF(tTankO(s))
async def bbTankONO_main():
  # print('def TankO(): ', tTankO('zz'))
  # tst = await (tTankO())
  tst = await tF(tTankO())
  print('tTankO(): ', tst)
  print('OkDone.')

# __name__
if __name__ == '__main__':
  # bbTankONO_main()
  asyncio.run(bbTankONO_main())

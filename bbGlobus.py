# Benzín Brno - Globus - Natural - bbGlobus.py
# https://www.globus.cz/brno/cerpaci-stanice-a-myci-linka.html
# https://www.globus.cz/brno/sluzby-a-produkty/cerpaci-stanice-a-myci-linka
# 20.12.2023 - httpx misto requests ktery neumi asyncio

import asyncio

# extract - stahne stranku
async def extract(url, Key):
  from bbCFG import bbCenaMsk, bbHeaders
  # import requests
  import pandas as pd
  import sys
  import httpx
  # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
  # r = requests.get(url, headers)
  # BeautifulSoup - ted nepotrebuji neni JavaScript
  # soup = BeautifulSoup(r.content, 'html.parser')
  r = await httpx.AsyncClient(http2=True, verify=False, max_redirects=9).get(url, headers=bbHeaders, follow_redirects=True)
  # print('r.content', type(r.content), '\n', r.content)

  Cena = 0
  try:
    # pd najde tabulky
    table = pd.read_html(r.content)
    # print(f'Total tables: {len(table)}')
  except:  # catch *all* exceptions # pylint: disable=bare-except
    e = sys.exc_info()[0]
    print("Error in bbGlobus.py: ", e)
    return Cena

  # tabulek je 6, zajima me c. 2.
  df = table[1]  # pandas.core.frame.DataFrame
  # adding column name to the respective columns - https://bit.ly/3oxfuhN
  try:
    df.columns = ['Name', 'smazat', 'Cena']
  except:  # catch *all* exceptions # pylint: disable=bare-except
    e = sys.exc_info()[0]
    print("Error in bbGlobus.py: ", e)
    return Cena
  # smazani sloupce - https://bit.ly/3oBNYjk
  del df['smazat']
  # Cena zmena typu na float - https://bit.ly/3Bi79SL
  df['Cena'] = df['Cena'].astype('float64')
  # Prepocitani df tj. / 100
  df['Cena'] = (df['Cena'] / 100)
  # How to add a trailing zeros to a pandas dataframe column? - https://bit.ly/3D5zwUO
  df['Cena'] = df['Cena'].map(bbCenaMsk.format)
  # LookUp - nalezeni hodnoty Key - https://bit.ly/3DuT59p
  Radek = df.loc[df['Name'] == Key]
  # How to get a value from a Pandas DataFrame and not the index and object type - https://bit.ly/3BhmuDc
  # Catching all exceptions without pylint error - https://bit.ly/3kvu86m
  try:
    Cena = Radek['Cena'].values[0]
  except:  # catch *all* exceptions  - pylint: disable=bare-except
    e = sys.exc_info()[0]
    print("Error in bbGlobus.py: ", e)
    Cena = 0
  # => float
  Cena = float(Cena)
  return Cena

# test function
async def tGlobu(url=''):
  from bbCFG import brint, bbProduct, bbNoUrl
  brint('tGlobu:', 'url', url)
  if bbProduct and (url != bbNoUrl):
    return await Globu(url)
  else:
    return 29.9

# globus - vrati cenu za natual - https://www.globus.cz/brno/cerpaci-stanice-a-myci-linka.html
async def Globu(url=''):
  if url == '':
    # url = r'https://www.globus.cz/brno/cerpaci-stanice-a-myci-linka.html'
    url = r'https://www.globus.cz/brno/sluzby-a-produkty/cerpaci-stanice-a-myci-linka'
  Key = 'Drive 95'
  Key = 'Natural 95'  # zmena media - 26.10.2021 13:15
  Cena = await extract(url, Key)
  # print('Cena paliva -', Key, '- je:', Cena, '  type', type(Cena))
  return Cena

# main
async def bbGlobus_main():
  print('def Globu(): ', await Globu())
  print('OkDone.')

# __name__
if __name__ == '__main__':
  # bbGlobus_main()
  asyncio.run(bbGlobus_main())

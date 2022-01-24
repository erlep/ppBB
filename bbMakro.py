# Benzín Brno - Makro - "Natural 95" - bbMakro.py
# https://www.makro.cz/prodejny/brno

# extract - stahne stranku
def extract(url, Key):
  # requests - nacte stranku
  # url = r'http://www.tank-ono.cz/cz/index.php?page=cenik'
  import requests
  import pandas as pd
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
  r = requests.get(url, headers)

  # pd najde tabulky
  table = pd.read_html(r.content, attrs={"class": "table gas-table"})
  # print(f'Total tables: {len(table)}')

  # tabulek je 2, zajima me c. 1
  df = table[0]
  # df.info()
  # df.head()

  # How to get a value from a Pandas DataFrame and not the index and object type - https://bit.ly/3BhmuDc
  item = df[Key].values[0]
  # '34,50 KÄ\x8d/l'  => 34.50
  item = item.split(' ')[0]  # jen to pred mezerou
  item = item.replace(",", ".")
  # item
  item = float(item)
  # print("item:", item, '|| type:', type(item))
  # Cena
  # Cena = bbCenaMsk.format(item)
  Cena = item
  # print("Cena:", Cena, '|| type:', type(Cena))
  # print('Cena paliva -', Key, '- je:', Cena )
  return Cena

# test function
def tMakro(url=''):
  from bbCFG import brint, bbProduct
  brint('tMakro:', 'url', url)
  if bbProduct:
    return Makro(url)
  else:
    return 29.9

# TankONO - vrati cenu za Natural "95" - pumpa: 'ČS Brno-Hviezdoslavova' - http://www.tank-ono.cz/cz/index.php?page=cenik
def Makro(url=''):
  url = r'https://www.makro.cz/prodejny/brno'
  Key = 'Natural 95'
  Cena = extract(url, Key)
  # print('Cena paliva -', Key, '- je:', Cena)
  return Cena

# main
def bbMakro_main():
  print('def Makro(): ', Makro())
  print('OkDone.')

# name__
if __name__ == '__main__':
  bbMakro_main()

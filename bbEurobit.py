# Benzín Brno - Eurobit - NATURAL 95 - pumpa: 'Brno - Podolí' - bbEurobit.py
# https://www.eurobit.cz/ceny
# 14.05.2023 -  1.verze

import asyncio
from bbCena import tF

# extract - stahne stranku
async def extract(url=''):
  from bbGetPage import GetPage
  import sys
  import re
  page_source = await GetPage(url)
  # Parsuj cenu pomoci RegEx
  item = str(page_source)
  # print(item)  #debug
  # https://regex101.com/r/H4q4sn/3
  # "Brno - Podolí","chrudim1Natural":"35,90 Kč"}
  try:
    item = re.search(r'\"Brno - Podolí\",\"chrudim1Natural\":\"(35,90) Kč', item)
    if not(item):
      return 0
    # prevedu na string
    item = str(item.group(1))
    item = item.replace(",", ".")
    # print('item', item, type(item))  # debug
  except:  # catch *all* exceptions # pylint: disable=bare-except
    e = sys.exc_info()[0]
    print("Error v bbEurobit.py: ", e)
    item = '0'
  # Cena
  # print('item', item, type(item))
  item = float(item)
  Cena = item
  return Cena
  return 0

# test function
async def tEuroB(url=''):
  from bbCFG import brint, bbProduct, bbNoUrl
  brint('tEuroB:  url', url)
  if bbProduct and (url != bbNoUrl):
    return await EuroB(url)
  else:
    # s = '19.9' + '   url: ' + url
    # return s
    return 14.05

# EuroB
async def EuroB(url=''):
  url = r'https://www.eurobit.cz/ceny'
  Cena = await extract(url)
  return Cena

# main
async def bbEurobit_main():
  print('tEuroB(): ', await tEuroB())
  print('OkDone.')

# __name__
if __name__ == '__main__':
  asyncio.run(bbEurobit_main())

# Notes
# https://www.eurobit.cz/ceny
# "title":"Brno - Podolí","chrudim1Natural":"35,90 Kč"}

# History
# 14.05.2023 -  1.verze

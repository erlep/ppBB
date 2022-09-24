# Benzín Brno - Makro - "Natural 95" - bbMakro.py
# https://www.makro.cz/prodejny/brno
import asyncio

# extract - stahne stranku
async def extract(url=''):
  from bbGetPage import GetPage
  from bs4 import BeautifulSoup
  import sys
  import lxml.html
  import re
  page_source = await GetPage(url)
  # print('page_source', page_source, type(page_source))
  # Parse processed webpage with BeautifulSoup
  # soup = BeautifulSoup(page_source, features="lxml")
  # Zkusim ziskat cenu - https://bit.ly/3K89bdu
  # item = soup.find("div", {"class": "price slide element-position"})
  # try:
  #   item = soup.select('#content > div > div:nth-child(4) > div > div > div.component.generic-component.component-position.fuel-prices.carousel-light.interactive.activated > div > div.prices.slides > div:nth-child(2) > div.field-price')
  # except:  # catch *all* exceptions # pylint: disable=bare-except
  #   e = sys.exc_info()[0]
  #   print("Error v bbMakro.py: ", e)
  #   item = '0'
  #  [<div class="field-price">38,90</div>] <   => 38.90

  # if (item is None) or (not item):
  #   print("Cena nenalezena v bbMakro.py. Treba novy soubor cookies.")
  #   return 0

  # Parsuj cenu pomoci RegEx
  item = str(page_source)
  item = re.search(r"Natural\s95.+?element-position", item).group()
  # print('item', item, type(item))
  # prevedu na string
  item = str(item)
  item = re.search(r"\>\d.+?\<", item).group()
  item = item.replace(">", "").replace("<", "").replace(",", ".")
  item = float(item)
  Cena = item
  return Cena

# test function
async def tMakro(url=''):
  from bbCFG import brint, bbProduct, bbNoUrl
  brint('tMakro:', 'url', url)
  if bbProduct and (url != bbNoUrl):
    return await Makro(url)
  else:
    return 29.9

# TankONO - vrati cenu za Natural "95" - pumpa: 'ČS Brno-Hviezdoslavova' - http://www.tank-ono.cz/cz/index.php?page=cenik
async def Makro(url=''):
  url = r'https://www.makro.cz/prodejny/brno'
  Key = 'Natural 95'
  # Cena = await extract(url, Key)
  Cena = await extract(url)
  # print('Cena paliva -', Key, '- je:', Cena)
  return Cena

# main
async def bbMakro_main():
  print('def Makro(): ', await Makro())
  print('OkDone.')

# __name__
if __name__ == '__main__':
  # bbMakro_main()
  asyncio.run(bbMakro_main())

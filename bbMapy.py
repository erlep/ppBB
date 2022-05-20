# Benzín Brno - Mapy.cz - https://bit.ly/3izRnLE - bbMapy.py
# Pro JavaScript pouziva: selenium <-> playwright
# 18.05.2022 - zmena na asyncio, trio nelze s playwright
import asyncio

# extract - stahne stranku
async def extract(url=''):
  from bbGetPage import GetPage
  from bs4 import BeautifulSoup
  import sys
  page_source = await GetPage(url)
  # Parse processed webpage with BeautifulSoup
  soup = BeautifulSoup(page_source, features="lxml")
  # Zkusim ziskat cenu
  try:
    item = soup.find(itemprop="price").get_text()
  except:  # catch *all* exceptions # pylint: disable=bare-except
    e = sys.exc_info()[0]
    print("Error v bbMapy.py: ", e)
    item = '0'
  # 34,40 Kč => 34.40
  item = item.replace(" Kč", "")
  item = item.replace(",", ".")
  # item
  item = float(item)
  # print("item:", item, '|| type:', type(item))
  # Cena
  # Cena = bbCenaMsk.format(item)
  Cena = item
  # print("Cena:", Cena, '|| type:', type(Cena))
  # Closes the current window
  return Cena

# test function
async def tMappy(url=''):
  from bbCFG import brint, bbProduct, bbNoUrl
  brint('jsem v tMappy   url', url)
  if bbProduct and (url != bbNoUrl):
    return await Mappy(url)
  else:
    return 39.9
  # s = '39.9' + '   url: ' + url
  # return s

# globus - vrati cenu za natual - https://www.globus.cz/brno/cerpaci-stanice-a-myci-linka.html
async def Mappy(url):
  # Key = 'Benzín'
  Cena = await extract(url)
  # print('Cena paliva -', Key, '- je:', Cena)
  return Cena

# main
async def bbMapy_main():
  url = r'https://bit.ly/3izRnLE'
  # print("def Mapy(r'https://bit.ly/3izRnLE'): ", Mappy(url))
  tst = await Mappy(url)
  print("def Mapy(r'https://bit.ly/3izRnLE'): ", tst)
  print('OkDone.')

# __name__
if __name__ == '__main__':
  # bbMapy_main()
  asyncio.run(bbMapy_main())

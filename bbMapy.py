# Benzín Brno - Mapy.cz - https://bit.ly/3izRnLE - bbMapy.py
# Pro JavaScript pouziva: selenium <-> playwright
# 18.05.2022 - zmena na asyncio, trio nelze s playwright
import asyncio

# extract - stahne stranku
async def extract(url=''):
  from bbGetPage import GetPage
  from bs4 import BeautifulSoup
  import sys
  # import re

  page_source = await GetPage(url)
  # print('page_source', page_source, type(page_source))
  # Regex test
  # regex = r"Benzín"
  # matches = re.search(regex, page_source, re.MULTILINE)
  # if matches:
  #   print("Match was found at {start}-{end}: {match}".format(start=matches.start(), end=matches.end(), match=matches.group()))
  #   for groupNum in range(0, len(matches.groups())):
  #     groupNum = groupNum + 1
  #     print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=matches.start(groupNum), end=matches.end(groupNum), group=matches.group(groupNum)))
  # else:
  #   print ('\n\nVyraz nenalezen\n\n')

  # Parse processed webpage with BeautifulSoup
  soup = BeautifulSoup(page_source, features="lxml")
  # Zkusim ziskat cenu
  try:
    # <span itemprop="price" content="36.50">36,50 Kč</span>
    item = soup.find(itemprop="price").get_text()
  except:  # catch *all* exceptions # pylint: disable=bare-except
    e = sys.exc_info()[0]
    print("Error v bbMapy.py: url", url, '\t\t', e)
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
  # url = r'https://mapy.cz/s/cutobofugo' # EuroOil
  # url = r'https://mapy.cz/s/mogofetafo'  # AVIA
  # url = r'https://mapy.cz/s/rafenusope'  # Eurobit
  # url = 'https://mapy.cz/s/cutobofugo'  # 'EuroOil Opuštěná       ', 'https://mapy.cz/s/cutobofugo'
  # url = 'https://mapy.cz/s/rodokobesa'  # 'AVIA                   ', 'https://mapy.cz/s/rodokobesa'
  # url = 'https://mapy.cz/s/jajularama'  # 'Eurobit                ', 'https://mapy.cz/s/jajularama'
  # new urls
  url = 'https://bit.ly/3izRnLE'        # 'Tesco - mapy.cz        ', 'https://bit.ly/3izRnLE'
  url = 'https://bit.ly/3izRnLE'        # 'Tesco - mapy.cz        ', 'https://bit.ly/3izRnLE'
  url = 'https://mapy.cz/s/jatejehoda'  # 'OMV IKEA               https://mapy.cz/s/jatejehoda
  url = 'https://mapy.cz/s/kepegubeve'  # 'MOL Olomoucká          https://mapy.cz/s/kepegubeve
  url = 'https://mapy.cz/s/lopagokoha'  # 'Makro                  https://mapy.cz/s/lopagokoha
  url = 'https://mapy.cz/s/mavadopata'  # 'Tesco - mapy.cz        https://mapy.cz/s/mavadopata
  url = 'https://mapy.cz/s/megolelafe'  # 'Shell Olomoucká        https://mapy.cz/s/megolelafe

  # test
  tst = await Mappy(url)
  print("def Mapy(", url, ": ", tst)
  print('OkDone.')

# __name__
if __name__ == '__main__':
  print('\n\nmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')
  # bbMapy_main()
  asyncio.run(bbMapy_main())

# playwright open  https://mapy.cz/s/megolelafe
# playwright codegen   --save-storage c:\aac\f1.txt  https://mapy.cz/s/cutobofugo

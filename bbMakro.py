# Benzín Brno - Makro - "Natural 95" - bbMakro.py
# https://www.makro.cz/prodejny/brno
import asyncio

# extract - stahne stranku
async def extract(url=''):
  from bbGetPage import GetPage
  import sys
  import re
  page_source = await GetPage(url)
  # Parsuj cenu pomoci RegEx
  item = str(page_source)
  try:
    item = re.search(r"Natural\s95.+?element-position", item)
    if not(item):
      return 0
    # prevedu na string
    item = str(item.group())
    item = re.search(r"\>\d.+?\<", item)
    if not(item):
      return 0
    item = item.group().replace(">", "").replace("<", "").replace(",", ".")
  except:  # catch *all* exceptions # pylint: disable=bare-except
    e = sys.exc_info()[0]
    print("Error v bbMakro.py: ", e)
    item = '0'
  # Cena
  # print('item', item, type(item))
  item = float(item)
  Cena = item
  return Cena

# test function
async def tMakro(url=''):
  from bbCFG import brint, bbProduct, bbNoUrl
  brint('tMakro:  url', url)
  if bbProduct and (url != bbNoUrl):
    return await Makro(url)
  else:
    return 29.9

# Makro
async def Makro(url=''):
  url = r'https://www.makro.cz/prodejny/brno'
  Cena = await extract(url)
  return Cena

# main
async def bbMakro_main():
  print('def Makro(): ', await Makro())
  print('OkDone.')

# __name__
if __name__ == '__main__':
  asyncio.run(bbMakro_main())

# playwright open  https://mapy.cz/s/megolelafe
# playwright codegen   --save-storage c:\aac\f1.txt  https://www.makro.cz/prodejny/brno

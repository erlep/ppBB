# Benzín Brno - Mapy.cz - https://bit.ly/3izRnLE - bbMapy.py
# Pro JavaScript pouziva: selenium <-> playwright

# extract - stahne stranku
def extract(url=''):
  from bbGetPage import GetPage
  from bs4 import BeautifulSoup
  import sys
  page_source = GetPage(url)
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
def tMappy(url=''):
  from bbCFG import brint, bbProduct, bbNoUrl
  brint('tMappy:', 'url', url)
  if bbProduct and (url != bbNoUrl):
    return Mappy(url)
  else:
    return 39.9
  # s = '39.9' + '   url: ' + url
  # return s

# globus - vrati cenu za natual - https://www.globus.cz/brno/cerpaci-stanice-a-myci-linka.html
def Mappy(url):
  # Key = 'Benzín'
  Cena = extract(url)
  # print('Cena paliva -', Key, '- je:', Cena)
  return Cena

# main
def bbMapy_main():
  url = r'https://bit.ly/3izRnLE'
  print("def Mapy(r'https://bit.ly/3izRnLE'): ", Mappy(url))
  print('OkDone.')

# name__
if __name__ == '__main__':
  bbMapy_main()

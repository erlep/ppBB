# Benzín Brno - mBenzin.cz - bbmBenzin.py
# https://www.mbenzin.cz/Nejlevnejsi-benzin/brno
# Benzina Albert Modřice - https://bit.ly/3ltfpd1

# extract - stahne stranku
def extract(url, Key):
  # requests - nacte stranku
  # url = r'https://bit.ly/3ltfpd1'
  import requests
  from bs4 import BeautifulSoup
  # Hlavicka
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
  r = requests.get(url, headers)
  # r.content

  # BeautifulSoup - ted nepotrebuji neni JavaScript
  soup = BeautifulSoup(r.content, 'html.parser')
  # Benzin
  Key = 'ContentPlaceHolder1_lN95Cost'
  # span + id
  try:
    item = soup.find('span', id=Key).text.strip()
  except:  # catch *all* exceptions  - pylint: disable=bare-except
    item = ''
  # '35,90'  => 35.90
  item = item.replace(",", ".")
  # item
  item = float(item)
  # print("item:", item, '|| type:', type(item))
  # Cena
  # Cena = bbCenaMsk.format(item)
  Cena = item
  return Cena

# test function
async def tmBenz(url=''):
  from bbCFG import brint, bbProduct, bbNoUrl, bbNmVR
  brint('tmBenz:', 'url', url)
  if bbProduct and (url != bbNoUrl):
    return await mBenz(url)
  else:
    return bbNmVR

# globus - vrati cenu za natual - https://www.globus.cz/brno/cerpaci-stanice-a-myci-linka.html
async def mBenz(url):
  from bbCFG import brint
  Key = 'ContentPlaceHolder1_lN95Cost'
  Cena = extract(url, Key)
  brint('Cena paliva -', Key, '- je:', Cena, 'type', type(Cena))
  return Cena

# main
def bbmBenzin_main():
  url = r'https://bit.ly/3ltfpd1'
  print("mBenzin Benzina Albert Modřice - https://bit.ly/3ltfpd1:", mBenz(url))
  print('OkDone.')

# __name__
if __name__ == '__main__':
  bbmBenzin_main()

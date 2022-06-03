# Benzín Brno - bbLST.py - LIST tj. seznam benzinek
# 18.05.2022 - zmena na asyncio, trio nelze s playwright
import asyncio

from bbCena import tF
from bbCFG import bbNoUrl
from bbGlobus import tGlobu
from bbMakro import tMakro
from bbMapy import tMappy
from bbmBenzin import tmBenz
from bbTankONO import tTankO

# s - budouci promenna url
s = bbNoUrl  # '--url--'

# Hlavicka tabulky - 'Název', 'Cena', 'Url'
bbHLAVICKA = ['Název', 'Cena', 'Old Cena', 'Delta Cena', 'Old Datum', 'Url']
bbHlavNazv = 0  # pozice 'Název' v bbHlavicka
bbHlavCena = 1  # pozice 'Cena' v bbHlavicka
bbHlavOldC = 2  # pozice 'Old Cena' v bbHlavicka
bbHlavDlta = 3  # pozice 'Delta Cena' v bbHlavicka
bbHlavDate = 4  # pozice 'Old Datum' v bbHlavicka
bbHlavaUrl = 5  # pozice 'Url' v bbHlavicka

# Konfigurace benzinek - Nazev, Fce, Url
bbBenzinky = [
    ['TankONO                ', 'tF(tTankO(s))', 'tF(tTankO(s))', r'http://www.tank-ono.cz/cz/index.php?page=cenik'],
    ['Tesco                  ', 'tF(tMappy(s))', 'tF(tMappy(s))', r'https://bit.ly/3izRnLE'],
    ['Globus                 ', 'tF(tGlobu(s))', 'tF(tGlobu(s))', r'https://www.globus.cz/brno/cerpaci-stanice-a-myci-linka.html'],
    ['Makro                  ', 'tF(tMakro(s))', 'tF(tMakro(s))', r'https://www.makro.cz/prodejny/brno'],
    ['Shell Olomoucká        ', 'tF(tMappy(s))', 'tF(tMappy(s))', r'https://mapy.cz/s/megolelafe'],
    ['MOL Olomoucká          ', 'tF(tMappy(s))', 'tF(tMappy(s))', r'https://mapy.cz/s/kepegubeve'],
    ['Benzina Albert Modřice ', 'tF(tmBenz(s))', 'tF(tmBenz(s))', r'https://bit.ly/3ltfpd1'],
    ['OMV IKEA               ', 'tF(tMappy(s))', 'tF(tMappy(s))', r'https://mapy.cz/s/jatejehoda'],
    ['EuroOil Opuštěná       ', 'tF(tMappy(s))', 'tF(tMappy(s))', r'https://mapy.cz/s/cutobofugo'],
]

# main
async def bbLST_main():
  from bbCFG import bbRender, bbTtest
  print('\n\n\n')
  print("bbTtest:    ", bbTtest)
  print("bbRender:   ", bbRender)
  # Seznam pro odkazy
  bbFce = await tF(tTankO(s))  # 'TankONO                ', 'http://www.tank-ono.cz/cz/index.php?page=cenik'],
  bbFce = await tF(tMappy(s))  # 'Tesco                  ', 'https://bit.ly/3izRnLE'],
  bbFce = await tF(tGlobu(s))  # 'Globus                 ', 'https://www.globus.cz/brno/cerpaci-stanice-a-myci-linka.html'],
  bbFce = await tF(tMakro(s))  # 'Makro                  ', 'https://www.makro.cz/prodejny/brno'],
  bbFce = await tF(tMappy(s))  # 'Shell Olomoucká        ', 'https://mapy.cz/s/megolelafe'],
  bbFce = await tF(tMappy(s))  # 'MOL Olomoucká          ', 'https://mapy.cz/s/kepegubeve'],
  bbFce = await tF(tmBenz(s))  # 'Benzina Albert Modřice ', 'https://bit.ly/3ltfpd1'],
  bbFce = await tF(tMappy(s))  # 'OMV IKEA               ', 'https://mapy.cz/s/jatejehoda'],
  bbFce = await tF(tMappy(s))  # 'EuroOil Opuštěná       ', 'https://mapy.cz/s/cutobofugo'],
  #
  bbFce = await tF(tmBenz(s))
  print("bbFce:    ", bbFce)
  print('Nazvy benzinek')
  # print((list(zip(*bbBenzinky)))[0])
  print()
  print('OkDone.')

# __name__
if __name__ == '__main__':
  # bbLST_main()
  asyncio.run(bbLST_main())

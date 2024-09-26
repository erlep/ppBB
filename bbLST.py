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
from bbEurobit import tEuroB

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

# Konfigurace benzinek - Nazev, Fce, Url - "nejlevnější benzín" • Mapy.cz - https://bit.ly/3hDBXsh
# [Benzin_Brno na Mapy.Cz](https://frame.mapy.cz/s/lohezoreba)
# https://www.eurobit.cz/ceny
bbBenzinky = [
    ['TankONO                ', 'tF(tTankO(s))', 'tF(tTankO(s))', r'https://www.tank-ono.cz/cz/index.php?page=cenik'],
    ['Tesco                  ', 'tF(tMappy(s))', 'tF(tMappy(s))', r'https://mapy.cz/s/mavadopata'],
    ['Globus                 ', 'tF(tGlobu(s))', 'tF(tGlobu(s))', r'https://www.globus.cz/brno/sluzby-a-produkty/cerpaci-stanice-a-myci-linka'],
    # ['Makro                  ', 'tF(tMakro(s))', 'tF(tMakro(s))', r'https://www.makro.cz/prodejny/brno'],
    # Makro docasne pres mapy.cz nez opravim
    ['Makro                  ', 'tF(tMappy(s))', 'tF(tMappy(s))', r'https://mapy.cz/s/lopagokoha'],
    ['Shell Olomoucká        ', 'tF(tMappy(s))', 'tF(tMappy(s))', r'https://mapy.cz/s/megolelafe'],
    ['MOL Olomoucká          ', 'tF(tMappy(s))', 'tF(tMappy(s))', r'https://mapy.cz/s/kepegubeve'],
    ['Benzina Albert Modřice ', 'tF(tmBenz(s))', 'tF(tmBenz(s))', r'https://bit.ly/3ltfpd1'],
    ['OMV IKEA               ', 'tF(tMappy(s))', 'tF(tMappy(s))', r'https://mapy.cz/s/jatejehoda'],
    ['EuroOil Opuštěná       ', 'tF(tMappy(s))', 'tF(tMappy(s))', r'https://mapy.cz/s/cutobofugo'],
    # ['AVIA                   ', 'tF(tMappy(s))', 'tF(tMappy(s))', r'https://mapy.cz/s/rodokobesa'],
    ['AVIA                   ', 'tF(tmBenz(s))', 'tF(tmBenz(s))', r'https://bit.ly/3wIivSA'],
    # ['Eurobit              ', 'tF(tMappy(s))', 'tF(tMappy(s))', r'https://mapy.cz/s/jajularama'],
    ['Eurobit                ', 'tF(tEuroB(s))', 'tF(tEuroB(s))', r'https://www.eurobit.cz/ceny'],
]

# main
async def bbLST_main():
  from bbCFG import bbRender, bbTtest
  print('\n\n\n')
  print("bbTtest:    ", bbTtest)
  print("bbRender:   ", bbRender)
  # Seznam pro odkazy
  bbFce = await tF(tTankO(s))  # 'TankONO                ', 'http://www.tank-ono.cz/cz/index.php?page=cenik'],
  bbFce = await tF(tMappy(s))  # 'Tesco - mapy.cz        ', 'https://bit.ly/3izRnLE'],        mapy.cz
  bbFce = await tF(tGlobu(s))  # 'Globus                 ', 'https://www.globus.cz/brno/sluzby-a-produkty/cerpaci-stanice-a-myci-linka
  bbFce = await tF(tMakro(s))  # 'Makro                  ', 'https://www.makro.cz/prodejny/brno'],
  bbFce = await tF(tMappy(s))  # 'Shell Olomoucká        ', 'https://mapy.cz/s/megolelafe'],
  bbFce = await tF(tMappy(s))  # 'MOL Olomoucká          ', 'https://mapy.cz/s/kepegubeve'],
  bbFce = await tF(tmBenz(s))  # 'Benzina Albert Modřice ', 'https://bit.ly/3ltfpd1'],        mBenzin.cz
  bbFce = await tF(tMappy(s))  # 'OMV IKEA               ', 'https://mapy.cz/s/jatejehoda'],
  bbFce = await tF(tMappy(s))  # 'EuroOil Opuštěná       ', 'https://mapy.cz/s/cutobofugo'],
  bbFce = await tF(tMappy(s))  # 'Eurobit                ', 'https://mapy.cz/s/jajularama'],
  bbFce = await tF(tEuroB(s))  # 'Eurobit                ', 'https://www.eurobit.cz/ceny'],
  bbFce = await tF(tMappy(s))  # 'AVIA                   ', 'https://mapy.cz/s/rodokobesa'],
  bbFce = await tF(tmBenz(s))  # 'AVIA                   ', 'https://bit.ly/3wIivSA'],
  #
  bbFce = await tF(tEuroB(s))
  print("bbFce:    ", bbFce)
  print('Nazvy benzinek')
  # print((list(zip(*bbBenzinky)))[0])
  print()
  print('OkDone.')

# __name__
if __name__ == '__main__':
  # bbLST_main()
  asyncio.run(bbLST_main())

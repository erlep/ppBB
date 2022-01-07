# Benzín Brno - bbLST.py - LIST tj. seznam benzinek
# v2 - pokus

from bbCFG import bbNoUrl
from bbCena import tF
from bbTankONO import tTankO
from bbMapy import tMappy
from bbGlobus import tGlobu
from bbMakro import tMakro
from bbmBenzin import tmBenz

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
    ['TankONO                ', 'tF(tTankO(s))', tF(tTankO(s)), r'http://www.tank-ono.cz/cz/index.php?page=cenik'],
    ['Tesco                  ', 'tF(tMappy(s))', tF(tMappy(s)), r'https://bit.ly/3izRnLE'],
    ['Globus                 ', 'tF(tGlobu(s))', tF(tGlobu(s)), r'https://www.globus.cz/brno/cerpaci-stanice-a-myci-linka.html'],
    ['Makro                  ', 'tF(tMakro(s))', tF(tMakro(s)), r'https://www.makro.cz/prodejny/brno'],
    ['Shell Olomoucká        ', 'tF(tMappy(s))', tF(tMappy(s)), r'https://mapy.cz/s/megolelafe'],
    # ['Shell Olomoucká        ', 'tF(tmBenz(s))', tF(tmBenz(s)), r'https://bit.ly/32Q9KHr'],
    ['MOL Olomoucká          ', 'tF(tMappy(s))', tF(tMappy(s)), r'https://mapy.cz/s/kepegubeve'],
    ['Benzina Albert Modřice ', 'tF(tmBenz(s))', tF(tmBenz(s)), r'https://bit.ly/3ltfpd1'],
    ['OMV IKEA               ', 'tF(tMappy(s))', tF(tMappy(s)), r'https://mapy.cz/s/jatejehoda'],
    ['EuroOil Opuštěná       ', 'tF(tMappy(s))', tF(tMappy(s)), r'https://mapy.cz/s/cutobofugo'],
]

# main
def bbLST_main():
  from bbCFG import bbTtest, bbRender
  print("bbTtest:    ", bbTtest)
  print("bbRender:   ", bbRender)
  bbFce = tF(tTankO(s))
  print("bbFce:    ", bbFce)
  print('Nazvy benzinek')
  print((list(zip(*bbBenzinky)))[0])
  print()
  print('OkDone.')

# name__
if __name__ == '__main__':
  bbLST_main()

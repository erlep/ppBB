# Benzín Brno - bbSaveXls.py - vypise ceny jednotlivych benzinek - bbSaveXls.py
# Ulozi ceny benzinek do Xls souboru
# 18.05.2022 - zmena na asyncio, trio nelze s playwright
import asyncio
import time
import pandas as pd
from bbCena import F2f, tF
from bbCFG import bbCsvFlNm, bbDateDMY, bbDateMsk, bbLogFlNm, bbXlsFlNm, bbXlsShNm, brint
from bbGlobus import tGlobu
from bbLST import bbBenzinky, bbHlavaUrl, bbHlavCena, bbHlavDate, bbHlavDlta, bbHLAVICKA, bbHlavOldC, bbNoUrl, s
from bbMakro import tMakro
from bbMapy import tMappy
from bbmBenzin import tmBenz
from bbTankONO import tTankO

# asnyc verze Eval
async def aEval(sStr, sFce):
  s = sStr  # 3. sloupec - Url je jako parametr s funkce
  brint("aEval: sFce", sFce, '  s', s)
  Cena = await eval(sFce)  # nazev promenne v promenne
  brint("aEval: sFce", sFce, '  s', s, '  Cena', Cena, '  type(Cena)', type(Cena))
  return Cena

# asnyc verze aSaveXls
async def aSaveXls(Dump=False):
  # Zmeny cen
  zmena = []
  # Xls file
  # dfXls = pd.read_excel(bbXlsFlNm, sheet_name=bbXlsShNm)
  # df1 = pd.read_excel(file, converters= {'COLUMN': pd.to_datetime}) - https://bit.ly/3nsSsrL
  dfXls = pd.read_excel(bbXlsFlNm, sheet_name=bbXlsShNm, converters={bbHLAVICKA[bbHlavDate]: pd.to_datetime})
  # print(dfXls)

  # Benzinky
  # Now date
  NowDate = 'Last status check on: ' + str(time.strftime(bbDateDMY))
  # Hlavicka tabulky - ['Název', 'Cena', 'Old Cena', 'Delta Cena', 'Old Datum', 'Url']
  Hlava = bbHLAVICKA[:]
  Hlava[bbHlavaUrl] = NowDate
  df = pd.DataFrame(columns=Hlava)
  # pole benzinek: Nazev, Fce, Url
  for i, n in enumerate(bbBenzinky):
    # Zjisti cenu - pomoci eval, s - je url
    s = n[3]  # 3. sloupec - Url je jako parametr s funkce
    Cena = await aEval(s, n[1])  # 1. sloupec string s nazvem funkce
    brint('  su tu n[1]:', n[1], 'Cena', Cena, '  type(Cena)', type(Cena))
    # Nazev: cena
    brint('#', i, ': Nazev:', n[0], ' Fce:', n[1], ' Cena:', Cena, ' 2:', n[2], ' Url:', n[3])
    # Udaje Old, Cena - 2. sloupec
    OldCena = dfXls.iloc[i, bbHlavCena]
    OldDelt = dfXls.iloc[i, bbHlavDlta]
    OldDate = dfXls.iloc[i, bbHlavDate]
    brint('Cena1', Cena, '  type(Cena)', type(Cena), '  OldDelt:', OldDelt, '  type(OldDelt)', type(OldDelt))
    # zmena ceny string
    zc = ''  # dlouhy
    zz = ''  # jen +-
    # Kdyz neni Zjistena cena
    if Cena == 0:
      Cena = OldCena
      print('Cena nezjistena - ', ' Nazev:', n[0], ' Fce:', n[1], ' Url:', n[3], '!')
    # Je Zmena Ceny
    if Cena != OldCena:
      # Zmena ceny
      OldDelt = await F2f(Cena - float(OldCena))
      # pridani +-
      if OldDelt > 0:
        OldDelt = '+' + str(OldDelt)
      else:
        OldDelt = str(OldDelt)
      # import time - strftime - https://bit.ly/3Edt2np
      OldDate = time.strftime(bbDateMsk)
      zc = ' ' + str((OldDelt)) + ' Cena: ' + str(float(Cena)) + ' Old: ' + str(float(OldCena)) + ' ' + str(OldDate) + ' - zmena ceny '
      #  Vypis zmenu kdyz neni dump
      txt = n[0] + ': ' + str(Cena) + zc
      print(txt) if not(Dump) else None
      # Log protokol zmen - append to file - https://bit.ly/3mXdyhz
      with open(bbLogFlNm, "a", encoding='UTF-8') as LogF:
        LogF.write(txt+'\n')
      # zmena
      zz = OldDelt
    else:
      OldCena = dfXls.iloc[i, bbHlavOldC]
    zmena.append(zz)
    # DataSet
    brint('#', i, ': Nazev:', n[0], ' Cena:', Cena, ' OldCena:', OldCena, ' OldDelt:', OldDelt, ' n[3]:', n[3])
    # url - https://bit.ly/3qJlRjq
    # lnk = '=HYPERLINK("http://www.someurl.com", "some website")'
    lnk = n[3]
    # lnk = '=HYPERLINK("' + lnk + '", "' + lnk + '")'
    df.loc[i] = [n[0], Cena, OldCena, OldDelt, OldDate, lnk]
    # Vypisuj?
    if Dump:
      # Zjisti cenu
      print(n[0], ':', Cena, zc)
  # Save Xls
  # df.style.set_precision(2).background_gradient().hide_index().to_excel('styled.xlsx', engine='openpyxl')
  df.to_excel(bbXlsFlNm, index=False, sheet_name=bbXlsShNm)
  # Save CSV
  df.to_csv(bbCsvFlNm, index=False)
  # print('zmena', zmena)
  return zmena

# await wSaveXls
async def wSaveXls(Dump=False):
  zmena = await aSaveXls(Dump)
  # print('zmena', zmena)
  return zmena

def SaveXls(Dump=False):
  """ Ulozi ceny benzinu do Xls
  Args:
      Dump: Vypisuj ceny
  """
  zmena = asyncio.run(wSaveXls(Dump))
  brint('zmena', zmena)
  return zmena

# main
def bbSaveXls_main():
  print()
  zmena = SaveXls(True)
  print("SaveXls():   zmena", zmena)
  print('OkDone.')

# __name__
if __name__ == '__main__':
  bbSaveXls_main()

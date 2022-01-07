# Benzín Brno - bbSaveXls.py - vypise ceny jednotlivych benzinek - bbSaveXls.py
# Ulozi ceny benzinek do Xls souboru

# from bbCFG import *
# from bbLST import *
# from bbLog import *
# from bbTankONO import *
# from bbMapy import *
# from bbGlobus import *
# from bbMakro import *
# from bbmBenzin import *
# from bbCena import *

# import pandas as pd
# import time

def SaveXls(Dump=False):
  """ Ulozi ceny benzinu do Xls

  Args:
      Dump: Vypisuj ceny
  """
  from bbCFG import brint, bbXlsFlNm, bbXlsShNm, bbDateMsk, bbLogFlNm, bbDateDMY
  from bbLST import bbHLAVICKA, bbBenzinky, bbHlavCena, bbHlavOldC, bbHlavDlta, bbHlavDate, bbHlavaUrl, bbNoUrl, s
  from bbCena import F2f, tF
  from bbTankONO import tTankO
  from bbMapy import tMappy
  from bbGlobus import tGlobu
  from bbMakro import tMakro
  from bbmBenzin import tmBenz

  import pandas as pd
  import time

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
    s = n[3]  # Url
    Cena = eval(n[1])  # nazev promenne v promenne
    brint('  su tu n[1]:', n[1], 'Cena', Cena)
    # Nazev: cena
    brint('#', i, ': Nazev:', n[0], ' Fce:', n[1], ' Cena:', Cena, ' 2:', n[2], ' Url:', n[3])
    # Udaje Old, Cena - 2. sloupec
    OldCena = dfXls.iloc[i, bbHlavCena]
    OldDelt = dfXls.iloc[i, bbHlavDlta]
    OldDate = dfXls.iloc[i, bbHlavDate]
    # zmena ceny string
    zc = ''
    # Kdyz neni Zjistena cena
    if Cena == 0:
      Cena = OldCena
      print('Cena nezjistena - ', ' Nazev:', n[0], ' Fce:', n[1], ' Url:', n[3], '!')
    # Je Zmena Ceny
    if Cena != OldCena:
      # Zmena ceny
      OldDelt = F2f(Cena - OldCena)
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
    else:
      OldCena = dfXls.iloc[i, bbHlavOldC]

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
  return None

# main
def bbSaveXls_main():
  print()
  print("SaveXls():    ", SaveXls())
  print('OkDone.')

# __name__
if __name__ == '__main__':
  bbSaveXls_main()

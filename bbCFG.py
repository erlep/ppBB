# Benzín Brno - bbCFG.py - config file
#  BenzinBrno v0.00 - Natural 95 prices in Brno - Python Version

# Globalni promenne
bbNmBB = 'BenzinBrno '
bbNmVR = 0.46  # TimeZone
# bbNmVE = 'v' + str(bbNmVR).format()
bbNmVE = 'GitV' + '{:.2f}'.format(bbNmVR)
bbNmDE = ' - Natural 95 prices in Brno - Python Version'
bbName = 'BenzinBrno v0.00 - Natural 95 prices in Brno - Python Version'
bbName = bbNmBB + bbNmVE + bbNmDE
bbNadpis = 'Ceny Benzínu v Brně:'
bbTtest = r'C:\peg\z1drv\OneDrive\aaEgp_P2E2\1Drv\qqq_Prj\ppBB\bbCFG.py'
bbCenFlNm = 'bbCeny'   # nazev protokolu zmen
bbLogFlNm = bbCenFlNm + '.Log'    # nazev protokolu zmen
bbXlsFlNm = bbCenFlNm + '.xlsx'   # nazev xls souboru
bbCsvFlNm = bbCenFlNm + '.csv'    # nazev csv souboru
bbPngFlNm = bbCenFlNm + '.png'    # nazev png souboru
bbXlsShNm = bbNmBB.strip()  # sheet name, strip = trim
bbNoUrl = '--url--'
bbDnu = int(3)  # kolik dnu zobrazovat zmenu ceny
# Configurace App
bbProduct = True  # True / False  - ostra / ladici verze
bbNoBBprn = True  # True / False  - ladeni tj. vypisovani dodatecnych informaci  ano / ne
bbCenaNoF = True  # True / False  - NEformatovat cenu real na string: # 34.4  => 34,40 Kč
bbHeadLes = True  # True / False  - headless - NEzobrazobvat  prohlizec Chrome
# Renderer
bbRender = 'playwright'  # selenium | playwright | requests_html
bbTimeGet = 43212  # timeout [miliseconds]
# import time - strftime - https://bit.ly/3Edt2np
bbDateMsk = "%Y-%m-%d %H:%M:%S"  # format casu - time.strftime("%Y/%m/%e %H:%M:%S") "%Y/%m/%d %H:%M"
bbDateDMY = "%d.%m.%Y %H:%M"  # format casu
bbDateLog = "%d.%m.%Y--%H:%M"  # format casu
# TimeZone
bbTimeZone = 'Europe/Amsterdam'
# Formatovani Ceny (float) - Cena = '{:.2f}'.format(item)
bbCenaMsk = '{:.2f}'  # format na 2 desetinna mista
# Graf
bbCenaMin = 33  # dolni mez ceny na ose X v grafu

# brint - my print, pomoci *ssAll
def brint(*ssAll):
  if not (bbNoBBprn):
    import inspect
    # Spojeni hodnot dict do retezce
    ss = ' '.join(str(v) for v in ssAll).strip()
    # akt fce
    # print(inspect.stack()[0][0].f_code.co_name)
    # predchozi funkce - stack[1]
    s0 = inspect.stack()[1][0].f_code.co_name + '/' + inspect.stack()[2][0].f_code.co_name + ': '
    print(s0, ss)

# main
def bbCFG_main():
  # print("bbTtest:    ", bbTtest)
  # print("bbRender:   ", bbRender)
  # print("bbName:     ", bbName)
  # print("bbNmNM:     ", bbXlsShNm)
  brint(' bbPrintDebug Test je OK')
  brint("bbNmVE:     ", bbNmVE)
  print('OkDone.')

# __name__
if __name__ == '__main__':
  bbCFG_main()
  ProgramInfo = '''
-----------------------------------------------------
History:
  14.05.2023 0.46 - Eurobit
  29.11.2022 0.45 - oprava ceny pro AVIA a EuroOil
  28.11.2022 0.44 - implementace Github Actions

  28.11.2022 0.44 - implementace Github Actions
  03.06.2022 0.38 - zmena na skutecne async
  18.05.2022 0.37 - zmena na Trio async
  30.11.2021 0.24 - Shell Olomoucká: Mapy -> mBenz
  29.11.2021 0.23 - oprava kdyz na mapy.cz neni cena
  29.11.2021 0.22 - celkem funckni
-----------------------------------------------------
  '''

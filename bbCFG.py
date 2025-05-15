# Benzín Brno - bbCFG.py - config file
#  BenzinBrno v0.00 - Natural 95 prices in Brno - Python Version

# Globalni promenne
bbNmBB = 'BenzinBrno '
bbNmVR = 0.57  # playwrite + Github Action fixed
# bbNmVE = 'v' + str(bbNmVR).format()
bbFmt2 = '{:6.2f}'  # float with 2 decimals
bbNmVE = 'GitV' + bbFmt2.format(bbNmVR)
bbNmDE = ' - Natural 95 prices in Brno - Python Version'
bbName = 'BenzinBrno v0.00 - Natural 95 prices in Brno - Python Version'
bbName = bbNmBB + bbNmVE + bbNmDE
bbNadpis = 'Ceny Benzínu v Brně:'
bbTtest = r'bbTtest'
bbCenFlNm = 'bbCeny'   # nazev protokolu zmen
bbLogFlNm = bbCenFlNm + '.Log'      # nazev protokolu zmen
bbXlsFlNm = bbCenFlNm + '.xlsx'     # nazev xls souboru
bbCsvFlNm = bbCenFlNm + '.csv'      # nazev csv souboru
bbPngFlNm = bbCenFlNm + '.png'      # nazev png souboru
bbPngFxls = bbCenFlNm + '.xls.png'  # nazev png souboru z xls souboru
bbXlsShNm = bbNmBB.strip()          # sheet name, strip = trim
bbNoUrl = '--url--'
bbDnu = int(3)  # kolik dnu zobrazovat zmenu ceny
# Configurace App
bbProduct = True  # True / False  - ostra / ladici verze
bbNoBBprn = True  # True / False  - ladeni tj. vypisovani dodatecnych informaci  ano / ne
bbCenaNoF = True  # True / False  - NEformatovat cenu real na string: # 34.4  => 34,40 Kč
bbHeadLes = True  # True / False  - headless - NEzobrazobvat  prohlizec Chrome
# Renderer
bbRender = 'playwright'  # selenium | playwright | requests_html
bbTimeGet = 50_000  # timeout [miliseconds] 30 sekund
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
bbCenaCft = 0.02  # 0.1=10% - koeficient pro rozsah pro dolni a horni mez ceny na ose X v grafu
# Chrome header - user agent - https://www.whatsmyua.info/
bbUsrAgnt = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
bbUsrAgnt = r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
bbHeaders = {'User-Agent': f'{bbUsrAgnt}'}

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
  print('delam bbCFG_main')
  print("bbHeaders:    ", bbHeaders)
  # print("bbTtest:    ", bbTtest)
  # print("bbRender:   ", bbRender)
  # print("bbName:     ", bbName)
  # print("bbNmNM:     ", bbXlsShNm)
  brint(' bbPrintDebug Test je OK')
  print("bbNmVE:     ", bbNmVE)
  print('OkDone.')

# __name__
if __name__ == '__main__':
  bbCFG_main()
  ProgramInfo = '''
-----------------------------------------------------
History:
  15.05.2025 0.57 - playwrite + Github Action fixed
  11.03.2024 0.52 - AVIA zmena z tMappy() https://mapy.cz/s/rodokobesa na tmBenz() https://bit.ly/3wIivSA
  03.01.2024 0.51 - opraveno try aby nepadalo aj.
  21.12.2023 0.50 - opraveny mapy.cz na podporu Cookies
  20.12.2023 0.49 - httpx misto requests ktery neumi asyncio
  19.05.2023 0.48 - Excel table as .png
  19.05.2023 0.47 - fix kaleido==0.2.1 vs. kaleido == 0.1.0.post1
  14.05.2023 0.46 - Eurobit
  29.11.2022 0.45 - oprava ceny pro AVIA a EuroOil
  28.11.2022 0.44 - implementace Github Actions
  03.06.2022 0.38 - zmena na skutecne async
  18.05.2022 0.37 - zmena na Trio async
  30.11.2021 0.24 - Shell Olomoucká: Mapy -> mBenz
  29.11.2021 0.23 - oprava kdyz na mapy.cz neni cena
  29.11.2021 0.22 - celkem funckni
-----------------------------------------------------
  '''

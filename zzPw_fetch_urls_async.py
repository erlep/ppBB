# Web Scraping With Playwright - https://bit.ly/3PEM6S6
# Asynchronous Web Scraping with Python, aiohttp, and asyncio - https://bit.ly/39wZsPM

import asyncio
import time
from asyncio.windows_events import NULL
from playwright.async_api import async_playwright
from bbCena import F2f, tF
from bbCFG import bbCsvFlNm, bbDateDMY, bbDateMsk, bbLogFlNm, bbNoUrl, bbXlsFlNm, bbXlsShNm, brint
from bbGlobus import tGlobu
from bbLST import bbBenzinky, bbHlavaUrl, bbHlavCena, bbHlavDate, bbHlavDlta, bbHLAVICKA, bbHlavOldC, bbNoUrl, s
from bbMakro import tMakro
from bbMapy import tMappy
from bbmBenzin import tmBenz
from bbTankONO import tTankO

async def DoRow(nm, s, fce):
  brint("\tDoRow: nm", nm, '  s', s, '  fce', fce)
  # response = await asks.get(url)
  # print("Finished: ", url, len(response.content))
  # Cena = eval(n[1])  # nazev promenne v promenne
  Cena = await eval(fce)  # nazev promenne v promenne
  print("DoRow: nm", nm, "  Cena: ", Cena)

async def fetch_all(rows):
  tasks = []
  for i, n in enumerate(rows):
    # Zjisti cenu - pomoci eval, s - je url
    nm = n[0]
    fce = n[1]
    # s = bbNoUrl  # '--url--'
    s = n[3]
    print(i, ':  nm', nm, '  fce', fce, '  s', s)
    # Cena = eval(n[1])  # nazev promenne v promenne
    task = asyncio.ensure_future(DoRow(nm, s, fce))
    tasks.append(task)
  await asyncio.gather(*tasks)

def main(rows):
  start_time = time.time()
  loop = asyncio.get_event_loop()
  future = asyncio.ensure_future(fetch_all(rows))
  loop.run_until_complete(future)
  print("Total time:", time.time() - start_time)

if __name__ == "__main__":
  main(bbBenzinky)

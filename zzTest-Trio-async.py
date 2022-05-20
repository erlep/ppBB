# Is asyncio too hard to use? Try Trio! - https://bit.ly/37yRrZN

import time

import asks  # misto requests pro async
import trio

from bbCena import F2f, tF
from bbCFG import (bbCsvFlNm, bbDateDMY, bbDateMsk, bbLogFlNm, bbNoUrl, bbXlsFlNm, bbXlsShNm, brint)
from bbGlobus import tGlobu
from bbLST import (bbBenzinky, bbHlavaUrl, bbHlavCena, bbHlavDate, bbHlavDlta, bbHLAVICKA, bbHlavOldC, bbNoUrl, s)
from bbMakro import tMakro
from bbMapy import tMappy
from bbmBenzin import tmBenz
from bbTankONO import tTankO

asks.init("trio")

async def DoRow(nm, s, fce):
  print("DoRow: nm", nm, '  s', s, '  fce', fce)
  # response = await asks.get(url)
  # print("Finished: ", url, len(response.content))

  # Cena = eval(n[1])  # nazev promenne v promenne
  Cena = await eval(fce)  # nazev promenne v promenne
  print("DoRow: nm", nm, "  Cena: ", Cena)

async def main(rows):
  start_time = time.time()
  async with trio.open_nursery() as nursery:
    for i, n in enumerate(rows):
      # Zjisti cenu - pomoci eval, s - je url
      nm = n[0]
      fce = n[1]
      # s = bbNoUrl  # '--url--'
      s = n[3]
      print(i, ':  nm', nm, '  fce', fce, '  s', s)
      # Cena = eval(n[1])  # nazev promenne v promenne
      nursery.start_soon(DoRow, nm, s, fce)
  print("Total time:", time.time() - start_time)


if __name__ == "__main__":
  trio.run(main, bbBenzinky)

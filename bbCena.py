# Benzín Brno - bbCena.py - pro vstupni real naformatuje cenu paliva: 34.4  => 34,40 Kč
# from bbCFG import *
# 18.05.2022 - zmena na asyncio, trio nelze s playwright
import asyncio
from bbCFG import bbCenaMsk, bbCenaNoF, bbProduct, brint

def F(val):
  """ Formatovani Ceny z real na string: # 34.4  => 34,40 Kč
  Args:
      val : Cena type real
  Returns:
      Naformatovana cena
  """
  brint("val:", val, '|| type:', type(val))
  Cena = F2f(val)
  # Formatovat?
  if (bbCenaNoF):
    return Cena
  # 34.4  => 34,40 Kč
  Cena = str(Cena)
  Cena = Cena.replace(".", ",")
  Cena = Cena + " Kč"
  # print("Cena:", Cena, '|| type:', type(Cena), "   val:", val, '|| type:', type(val))
  return Cena

# Formatuje real na 2 def mista, vraci real
def F2f(val):
  if type(val) != float:
    aval = val
    txt = 'NENI float ' + str(aval)
  else:
    aval = val
    txt = 'je float'
  brint('jsem v F2f val:', val, '  txt', txt, '|| type:', type(val))
  # hodnota aval
  val = aval
  # => float
  item = float(val)
  # 34.4  => 34,40 Kč
  Cena = bbCenaMsk.format(item)
  Cena = float(Cena)
  return Cena

# testovaci funkce
async def tF(val):
  if type(val) != float:
    aval = await val
    txt = 'NENI float ' + str(aval)
  else:
    aval = val
    txt = 'je float'
  brint('jsem v tF ', val, txt, ' aval typ', aval, type(aval))
  # hodnota aval
  val = aval
  # val = await val
  brint('tF:', 'val', val, type(val))
  if bbProduct:
    return val
  else:
    return val

# main
async def bbCena_main():
  # print("F(18.9551): ", tF(18.9551))
  # print("F(18.9551): ", tF(18.9551))
  # print("F(29.99):   ", F(29.99))
  # print("F(29.9):    ", F(29.9))
  # print("F(29):      ", F(29))
  # print("F2f(0.3999):", await F2f(0.3999))
  # tst = await tF(18.9551)
  # print('tF(18.9551)', tst)
  tst = await tF(18.9551)
  print('tF(18.9551)', tst)

  print('OkDone.')

# __name__
if __name__ == '__main__':
  # bbCena_main()
  asyncio.run(bbCena_main())

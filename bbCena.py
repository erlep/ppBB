# Benzín Brno - bbCena.py - pro vstupni real naformatuje cenu paliva: 34.4  => 34,40 Kč
# from bbCFG import *

def F(val):
  """ Formatovani Ceny z real na string: # 34.4  => 34,40 Kč
  Args:
      val : Cena type real
  Returns:
      Naformatovana cena
  """
  from bbCFG import brint, bbCenaNoF
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
  from bbCFG import brint, bbCenaMsk
  brint("val:", val, '|| type:', type(val))
  # => float
  item = float(val)
  # 34.4  => 34,40 Kč
  Cena = bbCenaMsk.format(item)
  Cena = float(Cena)
  return Cena

# testovaci funkce
def tF(val):
  from bbCFG import brint, bbProduct
  brint('tF:', 'val', val)
  if bbProduct:
    return F(val)
  else:
    return val

# main
def bbCena_main():
  print("F(18.9551): ", F(18.9551))
  print("F(29.99):   ", F(29.99))
  print("F(29.9):    ", F(29.9))
  print("F(29):      ", F(29))
  print("F2f(0.3999):", F2f(0.3999))
  print('OkDone.')

# name__
if __name__ == '__main__':
  bbCena_main()

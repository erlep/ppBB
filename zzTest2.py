# Benzín Brno - bbTest.py - testovaci soubor

from bbCFG import *
from bbLog import *

# ---06.11.2021--06:16--PC5406257--proj_sw_backup--T_TmChk-2.bat---{~~
def bbTest():
  bbTest2()

# ---06.11.2021--06:16--PC5406257--proj_sw_backup--T_TmChk-2.bat---{~~
def bbTest2():
  brint("bbprint('','su tu')", ' - jako parametr', 'su tu')
  print('su tu')

# main
def main():
  bbTest()
  print()
  print('OkDone.')

# name__
if __name__ == '__main__':
  main()

# Benzín Brno - bbDoChk.py - Kontrola cen na benzinkach
# Pro JavaScript pouziva: selenium <-> playwright

# Soubory
# Main  file: bb__.py
# Tento file: bbDoChk.py
# Ceny Log:   bbCeny.Log
# Chk Log:    DoChk.Log
# Notes:      Notes.Txt
# vEnv - C:\aaC\vEnv\R-I.txt

def DoChk():
  from bbCFG import bbName
  from bbGraf2 import Graf
  # from bbLST import *
  from bbLog import LogClose, LogOpen
  from bbSaveXls import SaveXls

  # Open
  LogOpen()
  # Tiulek
  print(bbName)
  # Benzinky zjisti ceny a uloz do Xls
  zmena = SaveXls(True)
  # print('zmena', zmena)
  # Save picture
  Graf(zmena)
  # Close
  LogClose()
  # Done
  print('OkDone.')

# main
def bbDoChk_main():
  DoChk()

# __name__
if __name__ == '__main__':
  bbDoChk_main()

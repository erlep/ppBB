# Benzín Brno - bbGraf.py - bar chart - graf cen ulozit do png

# ulozi graf do .\img\ceny.png
def Graf():
  from bbCFG import bbXlsFlNm, bbXlsShNm, bbPngFlNm, bbNmVE, bbDateDMY, bbNmBB
  from bbLST import bbHLAVICKA, bbHlavNazv, bbHlavCena, bbHlavOldC, bbHlavDlta, bbHlavDate, bbHlavaUrl, bbNoUrl, s
  import pandas as pd
  import time
  import matplotlib.pyplot as plt
  import numpy as np
  import os

  # Xls file
  df = pd.read_excel(bbXlsFlNm, sheet_name=bbXlsShNm, converters={bbHLAVICKA[bbHlavDate]: pd.to_datetime})
  # Název - trim
  x = df[bbHLAVICKA[bbHlavNazv]].str.strip()
  # Cena - ',' -> '.'
  y = df[bbHLAVICKA[bbHlavCena]]

  # Matplotlib Bars - w3 https://bit.ly/3u9WR6H
  # x = np.array(["A", "B", "C", "D"])
  # y = np.array([13.6, 18.1, 10.9, 10.1])
  plt.barh(x, y, color="DarkBlue")
  # displaying the title
  LastChech = str(list(df)[-1:][0])
  tit = bbNmBB + bbNmVE + ' ' + LastChech + '                       '
  plt.title(tit)
  # print('>>', tit, '<<')
  plt.xlabel('Price [Kč]', size=15)
  plt.ylabel('Petrol Station Name', size=15)
  # otocit osu Y
  plt.gca().invert_yaxis()
  # otocit y label
  # h = plt.ylabel('y')
  # h.set_rotation(0)

  # Popis hodnot https://bit.ly/342VdbG
  for index, value in enumerate(y):
    # print(' index , val ', index, value)
    plt.text(value - 5.0, index, str(value) + ' Kč', color="White")

  # Save to PNG - bbCeny.png
  # plt.savefig('foo.pdf')
  # plt.savefig('foo.png')
  plt.savefig(os.path.join(bbPngFlNm), dpi=300, format='png', bbox_inches='tight')
  # plt.show()
  ############################
  ############################

# main
def bbGraf_main():
  print('bbGraf_main.')
  Graf()
  print('OkDone.')

# name__
if __name__ == '__main__':
  bbGraf_main()

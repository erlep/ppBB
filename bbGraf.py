# Benzín Brno - bbGraf.py - bar chart - graf cen ulozit do png - pomoci matplotlib.pyplot

# ulozi graf do .\img\ceny.png
def Graf():
  from bbCFG import bbXlsFlNm, bbXlsShNm, bbPngFlNm, bbNmVE, bbNmBB
  from bbLST import bbHLAVICKA, bbHlavNazv, bbHlavCena, bbHlavDate
  import pandas as pd
  import matplotlib.pyplot as plt
  import os

  # Zkus přepnout matplotlib backend - peg 11.05.2025 17:18 NETESTOVANO
  # matplotlib.use('Agg')

  # Xls file
  df = pd.read_excel(bbXlsFlNm, sheet_name=bbXlsShNm, converters={bbHLAVICKA[bbHlavDate]: pd.to_datetime})
  # Název - trim
  x = df[bbHLAVICKA[bbHlavNazv]].str.strip()
  # Cena - ',' -> '.'
  y = df[bbHLAVICKA[bbHlavCena]]

  # Matplotlib Bars - w3 https://bit.ly/3u9WR6H
  # x = np.array(["A", "B", "C", "D"])
  # y = np.array([13.6, 18.1, 10.9, 10.1])
  plt.barh(x, y, color="DodgerBlue")
  # displaying the title
  LastChech = str(list(df)[-1:][0])
  tit = bbNmBB + bbNmVE + ' ' + LastChech + '              '
  plt.title(tit)
  # print('>>', tit, '<<')
  plt.xlabel('Price [Kč]', size=15)
  plt.ylabel('Petrol Station Name', size=15)
  # otocit osu Y
  plt.gca().invert_yaxis()
  # otocit y label
  # h = plt.ylabel('y')
  # h.set_rotation(0)

  # setting y-axis limit in matplotlib - https://bit.ly/3qXr9aw
  x1, x2, y1, y2 = plt.axis()
  x1 = 32  # 32,- Kč
  plt.axis((x1, x2, y1, y2))

  # Popis hodnot https://bit.ly/342VdbG
  for index, value in enumerate(y):
    # print(' index , val ', index, value)
    plt.text(value - 1.0, index, str(value) + ' Kč', color="White")

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

# __name__
if __name__ == '__main__':
  bbGraf_main()

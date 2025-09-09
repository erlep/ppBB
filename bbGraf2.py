# Benzín Brno - bbGraf.py - bar chart - graf cen ulozit do png - pomoci plotly.express

# ulozi graf do .\img\ceny.png
def Graf(zmena=''):
  from bbCFG import brint,bbXlsFlNm, bbXlsShNm, bbPngFlNm, bbNmVE, bbNmBB, bbCenaMin, bbCenaCft
  from bbLST import bbHLAVICKA, bbBenzinky, bbHlavCena, bbHlavNazv, bbHlavDate, bbHlavaUrl
  import pandas as pd
  import plotly.express as px
  import os

  # Excel file Tabulka
  # df = pd.read_excel(bbXlsFlNm, sheet_name=bbXlsShNm)
  df = pd.read_excel(bbXlsFlNm, sheet_name=bbXlsShNm,
                     converters={bbHLAVICKA[bbHlavDate]: pd.to_datetime, bbHLAVICKA[bbHlavaUrl]: str})
  # zjisteni max  a min ceny
  minCena = df.iloc[:, bbHlavCena].min()
  maxCena = df.iloc[:, bbHlavCena].max()
  brint('Cena: \n  minCena', minCena, '\n  maxCena', maxCena)
  # Hlavicka  LastChech = str(list(df)[-1:][0])
  LastChech = str(list(df)[-1:][0])
  tit = bbNmBB + bbNmVE + ' ' + LastChech + ' ' * 14

  # fig = px.bar(df, x=bbHLAVICKA[bbHlavNazv], y=bbHLAVICKA[bbHlavCena])
  fig = px.bar(df,
               x=bbHLAVICKA[bbHlavCena],
               y=bbHLAVICKA[bbHlavNazv],
               text=bbHLAVICKA[bbHlavCena],
               #  title=Prices + bbNmBB + bbNmVE+' '+LastChech,
               title=tit,
               color=bbHLAVICKA[bbHlavCena],
               category_orders={bbHLAVICKA[bbHlavNazv]: ((list(zip(*bbBenzinky)))[0])}
               )

  # ######################################################
  # #               range_x=[32, 40])
  # # How to obtain generated x-axis and y-axis range in plotly plot? - https://bit.ly/3AzY7kt
  # full_fig = fig.full_figure_for_development(warn=False)
  # # print('full', full_fig.layout.xaxis.range, type(full_fig.layout.xaxis.range))
  # xlim = list(full_fig.layout.xaxis.range)
  # # min hodnota
  # xlim[0] = bbCenaMin
  # # print('xlim', xlim, type(xlim))
  # # https://plotly.com/python/reference/layout/xaxis/
  # # fig.update_xaxes(range=[32, 40])
  # fig.update_xaxes(range=xlim)

  # zmena y limit: full_figure_for_development - vytuhava
  # https://plotly.com/python/axes/#setting-the-range-of-axes-manually
  fig.update_xaxes(range=[minCena - minCena*bbCenaCft*2, maxCena + maxCena*bbCenaCft])

  # text s info o zmene ceny
  # fig.add_annotation(dict(font=dict(color='darkred', size=15),
  #                         x=-0.34,
  #                         y=+1.14,
  #                         showarrow=False,
  #                         text=zmena,
  #                         textangle=0,
  #                         xanchor='left',
  #                         yanchor='top',
  #                         xref="paper",
  #                         yref="paper"))

  # pocet benzinek - 9
  pocet = len(df.index)
  # prida do grafu zmenu ceny
  for i, n in enumerate(bbBenzinky):
    OldCena = df.iloc[i, bbHlavCena]
    # print(i, n[0], OldCena, (pocet-(i+1)), zmena[i])
    fig.add_annotation(  # zmena ceny x=cena, y = 8 az 0
        text=zmena[i], x=OldCena*1.01, y=(pocet-(i+1)), arrowhead=0, showarrow=False, font=dict(color='darkred'))
  # fig.add_annotation(  # popis pro TankONO
  #     text="below target!", x=44, y=8, arrowhead=0, showarrow=False, font=dict(color='darkred'))

  # Show image
  fig.show()
  # print(fig)

  # How to save plotly express plot into a html or static image file? - https://bit.ly/3KKM1cX
  # pip install -U kaleido
  fig.write_image(os.path.join(bbPngFlNm), scale=2.0)

# main
def bbGraf_main():
  print('bbGraf_main.')
  Graf(['-1.1', '+2.2', '3.1', '4.12', '', '6.20', '', '8.88', '+9.0', '', ''])
  print('OkDone.')

# __name__
if __name__ == '__main__':
  bbGraf_main()

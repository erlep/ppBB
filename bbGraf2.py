# Benzín Brno - bbGraf.py - bar chart - graf cen ulozit do png - pomoci plotly.express

# ulozi graf do .\img\ceny.png
def Graf():
  from bbCFG import bbXlsFlNm, bbXlsShNm, bbPngFlNm, bbNmVE, bbNmBB
  from bbLST import bbHLAVICKA, bbBenzinky, bbHlavCena, bbHlavNazv, bbHlavDate, bbHlavaUrl
  import pandas as pd
  import plotly.express as px
  import os

  # Excel file Tabulka
  # df = pd.read_excel(bbXlsFlNm, sheet_name=bbXlsShNm)
  df = pd.read_excel(bbXlsFlNm, sheet_name=bbXlsShNm,
                     converters={bbHLAVICKA[bbHlavDate]: pd.to_datetime, bbHLAVICKA[bbHlavaUrl]: str})
  # Hlavi  LastChech = str(list(df)[-1:][0])
  LastChech = str(list(df)[-1:][0])
  tit = bbNmBB + bbNmVE + ' ' + LastChech + '              '

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
  #               range_x=[32, 40])
  # How to obtain generated x-axis and y-axis range in plotly plot? - https://bit.ly/3AzY7kt
  full_fig = fig.full_figure_for_development(warn=False)
  # print('full', full_fig.layout.xaxis.range, type(full_fig.layout.xaxis.range))
  xlim = list(full_fig.layout.xaxis.range)
  # min hodnota
  xlim[0] = 32
  # print('xlim', xlim, type(xlim))
  # https://plotly.com/python/reference/layout/xaxis/
  # fig.update_xaxes(range=[32, 40])
  fig.update_xaxes(range=xlim)
  fig.show()

  # How to save plotly express plot into a html or static image file? - https://bit.ly/3KKM1cX
  # pip install -U kaleido
  fig.write_image(os.path.join(bbPngFlNm), scale=2.0)

# main
def bbGraf_main():
  print('bbGraf_main.')
  Graf()
  print('OkDone.')

# name__
if __name__ == '__main__':
  bbGraf_main()

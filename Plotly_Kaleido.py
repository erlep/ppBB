# import plotly.express as px

# fig = px.scatter(x=[1, 2, 3], y=[4, 5, 6], title="Test")
# fig.write_image("test.png")
# print("Obrázek uložen.")

# import kaleido
# print("Kaleido funguje.")

import plotly.express as px
import plotly.io as pio

fig = px.scatter(x=[1, 2, 3], y=[4, 5, 6], title="Test")
pio.write_image(fig, "test.png", format="png", scale=2)
print("Obrázek uložen.")

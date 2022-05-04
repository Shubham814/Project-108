import pandas
import plotly.figure_factory as ff


readCSV = pandas.read_csv("data.csv")
rating = readCSV["Avg Rating"].tolist()

fig = ff.create_distplot([rating],["Average Rating"])
fig.show()


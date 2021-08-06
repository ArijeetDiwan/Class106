import plotly_express as px
import csv 
with open("./TemperatureandIceCream.csv") as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="Temperature",y="Ice-cream Sales")
    fig.show()

#data is highly correlated as temperture increase the sale of ice cream goes up
#where as temperture vs sale of warm clothes are inversly correlated 
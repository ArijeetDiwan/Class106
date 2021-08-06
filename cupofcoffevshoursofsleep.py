import plotly_express as px
import csv 
#fall graph data is close to the centre straight line
with open("./cupsofcoffeeandhoursofsleep.csv") as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
    #dataset are inversly correlated
    fig.show()
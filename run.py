import json
import plotly
import plotly.express as px
import plotly.graph_objects as go
# from static.tools.balanceTracker import *
# from static.tools.ContributionPerDay import *
# from static.tools.transactionScatter import *
# from static.tools.expensePerDay import *
from flask import Flask, redirect, render_template, session, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    df = px.data.medals_wide()

    #build the graphs that we want on the page
    graph1 = px.bar(df, x= "nation", y= ['gold', 'silver', 'bronze'], title = "Graph1")
    graph1JSON = json.dumps(graph1, cls=plotly.utils.PlotlyJSONEncoder)

    graph2 = px.bar(df, x= "nation", y= ['gold', 'silver', 'bronze'], title = "Graph2")
    graph2JSON = json.dumps(graph2, cls=plotly.utils.PlotlyJSONEncoder)

    graph3 = px.bar(df, x= "nation", y= ['gold', 'silver', 'bronze'], title = "Graph3")
    graph3JSON = json.dumps(graph3, cls=plotly.utils.PlotlyJSONEncoder)     


    #Return the page from the index.html render tamplates with the graphs we just created as parameters
    return render_template('index.html', graph1JSON = graph1JSON, graph2JSON = graph2JSON, graph3JSON = graph3JSON)

if __name__ == "__main__":
    app.run(debug=True)

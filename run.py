import json
from urllib import request
import plotly 
import plotly.express as px
import plotly.graph_objects as go
from flask import *
from static.tools.transactionScatter import transactionMain
import pandas as pd
import selenium

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def index():
    url = 'https://opencollective.com/darkreader'
    if url[:27] == 'https://opencollective.com/':
        url =  url + '/transactions'
    else:
        return render_template('index.html', nolink = True, Error = True)

    name = url.split('/')[3].capitalize()
    print(name)
    df = pd.read_csv('static/tools/Data.csv')

    #build the graphs that we want on the page
    graph1 = px.line(df, x= "Order Date", y="Running Balance", title = "Running Balance")
    graph1JSON = json.dumps(graph1, cls=plotly.utils.PlotlyJSONEncoder)

    graph2 = px.scatter(transactionMain(df, 0), x= "Order Date", y= 'Net Amount (USD)', title = "All Transactions")
    graph2JSON = json.dumps(graph2, cls=plotly.utils.PlotlyJSONEncoder)

    graph3 = px.scatter(transactionMain(df, 1), x = 'Order Date',y= 'Net Amount (USD)', title = "All Contributions",)
    graph3JSON = json.dumps(graph3, cls=plotly.utils.PlotlyJSONEncoder)     
    if request.method == 'POST':
        if request.form.get('tips'):
            return 

    #Return the page from the index.html render tamplates with the graphs we just created as parameters
    return render_template('index.html', name=name,graph1JSON = graph1JSON,
     graph2JSON = graph2JSON, graph3JSON = graph3JSON)

if __name__ == "__main__":
    app.run(debug=True)

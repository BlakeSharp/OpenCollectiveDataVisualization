import json
from urllib import request
import plotly 
import plotly.express as px
import plotly.graph_objects as go
from flask import request, render_template, Flask
from static.tools.transactionScatter import transactionMain
import pandas as pd
import selenium

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def index():
    url = ""
    if request.method == "POST":  #if the request is a post (called by the form action)

        url = request.form.get("comname") # comname = COMmunityNAME, input in form
        # if len(url) > 27:
        #     url = url[:27] #this shortens the link to fit the 'https://opencollective/x/' format 
        name = url.split('/')[3].capitalize() #This takes text after the final / to display the name of the community

        df = pd.read_csv('static/tools/Data.csv') #this loads the data from file

        # From file --> From link download file when open collective fixes bug

        #use selenium to use a headless broswer and take a screenshot of biggest donors HERE


        #build the graphs that we want on the page 
        
            #The amount of money the community has had available at given times line chart
        graph1 = px.line(df, x= "Order Date", y="Running Balance", title = "Running Balance")
        graph1JSON = json.dumps(graph1, cls=plotly.utils.PlotlyJSONEncoder)

            #all Transaction (Noth expenses and donations) scatter plot
        graph2 = px.scatter(transactionMain(df, 0), x= "Order Date", y= 'Net Amount (USD)', title = "All Transactions")
        graph2JSON = json.dumps(graph2, cls=plotly.utils.PlotlyJSONEncoder)

            #All donations scatter plot
        graph3 = px.scatter(transactionMain(df, 1), x = 'Order Date',y= 'Net Amount (USD)', title = "All Contributions",)
        graph3JSON = json.dumps(graph3, cls=plotly.utils.PlotlyJSONEncoder)     

        #add a graph a bar graph to visaulize the amount of frequency of donation amounts


        #Return the page from the index.html render tamplates with the graphs we just created as parameters
        return render_template('index.html', name=name,graph1JSON = graph1JSON,
        graph2JSON = graph2JSON, graph3JSON = graph3JSON)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

import json
import plotly
import plotly.express as px
import plotly.graph_objects as go
#from application.static.tools.balanceTracker import *
#from application.static.tools.ContributionPerDay import *
#from application.static.tools.transactionScatter import *
#from application.static.tools.expensePerDay import *
from flask import Flask, redirect, render_template, session, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    #fig1 = balanceMain()

    #graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)

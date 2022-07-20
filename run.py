import json
from math import exp
import plotly 
import plotly.express as px
from flask import request, render_template, Flask
from static.tools.biggestExpenses import expensesMain
from static.tools.transactionScatter import transactionMain
import pandas as pd
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
import time
app = Flask(__name__)




@app.route("/", methods = ['POST', 'GET'])
def index():
    url = "https://opencollective.com/darkreader"
    if request.method == "POST":  #if the request is a post (called by the form action)
        #Selenium start
            #settings and setup
        options = FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options = options)
        driver.get(url)
        topcontributions = driver.find_element("id","section-top-financial-contributors") #Navigate to top contributers div
        team = driver.find_element("xpath", '//*[@id="section-our-team"]/div/div/div[1]')
        time.sleep(2) #this gives time for firefox to lead the contributers images

        #This prevents "can't read byte data error"
        ss_teams = team.screenshot_as_png
        screenshot_as_bytes = topcontributions.screenshot_as_png

        with open('static/topcontributions.png', 'wb') as f:
            f.write(screenshot_as_bytes)
        with open('static/team.png', 'wb') as f:
            f.write(ss_teams)
        #Selenium end

        url = request.form.get("comname") # comname = COMmunityNAME, input in form
        try:
            url = url[:(27 + len(url.split('/')[3]))]
            name = url.split('/')[3].capitalize() #takes text after the final / to display the name of the community

        except:
            name = "url"

        df = pd.read_csv('static/tools/Data.csv') #(temp) loads the data from file

        #This makes a df of all values in data > 0
        posdon = transactionMain(df, 1)

        #This makes a df of all values in data < 0 
        negdon = transactionMain(df, 2)

        # From file --> From link download file when open collective fixes bug

        #build the graphs that we want on the page         
            #The amount of money the community has had available at given times line chart
        graph1 = px.line(df, x= "Order Date", y="Running Balance", title = "Running Balance", custom_data = ['User Name', 'Net Amount (USD)','Transaction Description'])

            #all Transaction (Noth expenses and donations) scatter plot
        graph2 = px.scatter(transactionMain(df, 0), x= "Order Date", y= 'Net Amount (USD)', title = "All Transactions")

            #All donations scatter plot
        graph3 = px.scatter(posdon, x = 'Order Date',y= 'Net Amount (USD)', title = "All Contributions"
        , custom_data = ['User Name','Subscription Interval'])
            #update the hover to show the name, amount, and order date 
        graph3.update_traces(hovertemplate = "User Name : %{customdata[0]} <br> Amount: %{y} USD <br> Interval: %{customdata[1]} <br> Date = %{x}")
        graph1.update_traces(hovertemplate = "User Name : %{customdata[0]} <br> Running Balance: %{y} <br> Amount: %{customdata[1]} USD <br> Description %{customdata[2]} <br> Date = %{x}")
        
        
        #Convert all graphs to json objects
        graph1JSON = json.dumps(graph1, cls=plotly.utils.PlotlyJSONEncoder) 
        graph2JSON = json.dumps(graph2, cls=plotly.utils.PlotlyJSONEncoder)
        graph3JSON = json.dumps(graph3, cls=plotly.utils.PlotlyJSONEncoder)     

        #add a graph a bar graph to visaulize the amount of frequency of donation amounts

        largestExpenses = expensesMain(df)


        # # contributions
        amtContributions = len(posdon.index)
        # # of expsese
        amtExpenses = len(negdon.index)
        # total raised
        totalRaised = int(posdon['Net Amount (USD)'].sum())
        # total spent
        totalSpent = abs(int(negdon['Net Amount (USD)'].sum()))
        # average contribution
        avgcon = int(totalRaised/amtContributions)
        avgexp = abs(int(totalSpent/amtExpenses))
        # founded


        #Return the page from the index.html render tamplates with the graphs we just created as parameters
        return render_template('index.html', name=name,graph1JSON = graph1JSON,
        graph2JSON = graph2JSON, graph3JSON = graph3JSON, expenses = largestExpenses.round(2), enames = largestExpenses.index.values,
        acon = amtContributions, aexp = amtExpenses, traised = totalRaised, tspent = totalSpent, avgcon = avgcon, avgexp = avgexp
        )
    
    #indow.html without parameters will be shown if the request is not a POST
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

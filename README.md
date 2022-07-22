# Open Collective Data Visualization
  Open Collective is a fundraising platform that creates transparently funded communities.
By making all transactions public, both donations and expenses, Open Collective supports grassroots communities that rely
on donations to raise, manage, and spend their money. The benefit that Open Collective provides to the patron is the
ability to track and assess how their donations are being spent. While Open Collective successfully provides a more open transparent space
through their download CSV function, they fall short of providing potential patrons with the resources to properly interpret that data, That is where Open Collective Data Visualization (OCDV) helps.
By providing tables, graphs, and other important information OCDV allows all potential patrons to properly assess how well the money is being managed and ultimately decide if they want to support the community.

## Instructions
To use OCDV is quite easy, simply:
1) **Navigate to the Open collective page of your choosing**
2) **Copy the desired community's home page URL** `https://opencollective.com/darkreader`
3) **Paste into the `Community` field on OCDV**
4) **Click the `View` button** 

## INCLUDED INFORMATION
Open collective Data Visualization is broken into three main sections. 
1) #### Information
- The team behind the project
- Top organization and individual sponsors
2) #### Data Tables
- Miscellaneous Data
- Largest expenses grouped by individual
3) #### Graphs
- Running Balance (line graph)
- All Transactions (Scatter Plot)
- All contributions (Scatter Plot)

## HOW IT WAS BUILT
OCDV is built using Flask as a backend web framework, utilizing pandas for data manipulation, plotly for displaying the graphs, and Selenium for the information images. While OCDV began as a Tkinter app, I transferred it to Flask for the ease of viewing the data. 

## IMAGES

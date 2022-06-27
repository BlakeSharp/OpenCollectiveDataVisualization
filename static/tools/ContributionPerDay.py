import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import datetime


def contributionMain():
    data = pd.read_csv("static/tools/Data.csv")
    data["Net Amount (USD)"] = round(data["Net Amount (USD)"].astype(float), 2)
    edit = data.loc[data["Net Amount (USD)"] > 0]

    for i in range(0, len(data["Order Date"])):
        try:
            data["Order Date"][i] = datetime.datetime.strptime(
                data["Order Date"][i].split("T")[0], "%Y-%m-%d"
            )
        except:
            pass
    data.to_csv("static/tools/Data.csv", index=False)

    
def createGraph():
    fig = px.line(
        edit,
        x=edit["Order Date"],
        y=(edit["Net Amount (USD)"]),
        hover_data=[edit["User Name"], edit["Transaction Description"]],
        title="Net contributions per day (USD) over time",
        template="seaborn"
    )
    fig.update_layout(hovermode="x unified")
    fig.show()


# this stops the import from running the script and allows from running direct from this file


def main():
    contributionMain()


if __name__ == "__main__":
    main()

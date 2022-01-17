import plotly.express as px
import pandas as pd
import datetime

data = pd.read_csv("Community/Data.csv")
data["UserName"] = ""

data["Net Amount (USD)"] = round(data["Net Amount (USD)"].astype(float), 2)
edit = data.loc[data["Net Amount (USD)"] < 0]

for i in range(0, len(data["Order Date"])):
    try:
        data["Order Date"][i] = datetime.datetime.strptime(
            data["Order Date"][i].split("T")[0], "%Y-%m-%d"
        )
    except:
        break


def expensesMain():
    data.to_csv("Community/Data.csv", index=False)
    createGraph()


def createGraph():
    fig = px.line(
        edit,
        x=edit["Order Date"],
        y=edit["Net Amount (USD)"],
        hover_data=[edit["User Name"]],
        title="Net expenses per day (USD) over time",
    )
    fig.show()


# this stops the import from running the script and allows from running direct from this file


def main():
    expensesMain()


if __name__ == "__main__":
    main()

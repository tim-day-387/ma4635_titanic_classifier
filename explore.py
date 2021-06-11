# Imports
import pandas as pd

# Provides basics stats
def giveStats(dataframe):
    total_passengers = len(dataframe.Survived)
    total_survived = sum(dataframe.Survived)
    total_percent = total_survived/total_passengers*100

    print("------ Overview ------")
    print("Passengers: ",total_passengers,"\nSurvived: ",total_survived,"\nPercent: ",total_percent,"%")

# Explore Ticket
def exploreTicket(dataframe,query):
    sel = []
    for i, row in dataframe.iterrows():
        if query in str(row.Ticket):
            sel.append(i)
    sel_df = dataframe.iloc[sel]

    sel_passengers = len(sel_df.Survived)
    sel_survived = sum(sel_df.Survived)
    if(sel_passengers != 0):
        sel_percent = sel_survived/sel_passengers*100
    else:
        sel_percent = -1

    print("------ Overview ------")
    print("Passengers: ",sel_passengers,"\nSurvived: ",sel_survived,"\nPercent: ",sel_percent,"%")

    print("-------- Ports -------")
    print("C: ",len(sel_df.loc[sel_df.Embarked == 'C']),"\nQ: ",len(sel_df.loc[sel_df.Embarked == 'Q']),"\nS: ",len(sel_df.loc[sel_df.Embarked == 'S']),)


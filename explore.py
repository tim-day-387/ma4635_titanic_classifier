# Imports
import pandas as pd

# Data
train = pd.read_csv("data/train.csv")
total_passengers = len(train.Survived)
total_survived = sum(train.Survived)
total_percent = total_survived/total_passengers*100

print("Passengers: ", total_passengers, 
      "\nSurvived: ", total_survived, 
      "\nPercent: ", total_percent, "%")


# Explore Ticket
query = 'SOTON'
sel = []
for i, row in train.iterrows():
    if query in str(row.Ticket):
        sel.append(i)
sel_df = train.iloc[sel]

sel_passengers = len(sel_df.Survived)
sel_survived = sum(sel_df.Survived)
sel_percent = sel_survived/sel_passengers*100

print("Passengers: ", sel_passengers, 
      "\nSurvived: ", sel_survived, 
      "\nPercent: ", sel_percent, "%")

print("Ports:",
     "\nC: ", len(sel_df.loc[sel_df.Embarked == 'C']),
     "\nQ: ", len(sel_df.loc[sel_df.Embarked == 'Q']),
     "\nS: ", len(sel_df.loc[sel_df.Embarked == 'S']),
     )


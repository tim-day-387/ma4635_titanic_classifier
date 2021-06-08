# Imports
import pandas as pd
from sklearn import preprocessing
import numpy as np
import sys
from sklearn.cluster import AffinityPropagation
import distance
import json

# Seeds
r = 4635
np.random.seed(r)

# Data
train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")

# Convert sex to dummy variable
def sex_to_dummy(df):
    # female:0, male:1
    le = preprocessing.LabelEncoder()
    le.fit(df.Sex)
    df.Sex = le.transform(df.Sex)
    return df

# Encode ticket by tag
def encode_ticket(df, datasplit):
    if datasplit == 'train':
        # extract set of recurring tags from ticket values
        tags = []
        indicies_with_tag = [] # save for efficiency in future step
        # extract tag from each non float ticket
        for i, row in df.iterrows():
            if type(row.Ticket) != float:
                split = row.Ticket.split(' ')
                if len(split) > 1:
                    tags.append(split[0])
                    indicies_with_tag.append(i)
        tags = list(set(tags))
        # cluster tags to reduce dimensionality
        tags = np.asarray(tags)
        # calculate levenshtein distances between tags
        lev_similarity = -1*np.array([[distance.levenshtein(w1,w2) for w1 in tags] for w2 in tags])
        affprop = AffinityPropagation(affinity="precomputed", damping=0.5, random_state=r)
        affprop.fit(lev_similarity)
        cluster_dict = {}
        # generate affinity propogation clusters
        for cluster_id in np.unique(affprop.labels_):
            exemplar = tags[affprop.cluster_centers_indices_[cluster_id]]
            cluster = np.unique(tags[np.nonzero(affprop.labels_==cluster_id)])
            cluster_str = ", ".join(cluster)
            cluster_dict[exemplar] = cluster_str.split(', ')
            # print(" - *%s:* %s" % (exemplar, cluster_str)) 
        
        # save clusters for use on test data
        with open('ticketClusters.json', 'w') as fp:
            json.dump(cluster_dict, fp)
            
    if datasplit == 'test':
        # load clusters generated from train data  
        with open('ticketClusters.json', 'r') as fp:
            cluster_dict = json.load(fp)
        # must be run on entire set of test data
        indicies_with_tag = range(0,len(df))
    
    # one hot encode based on clusters
    for key in cluster_dict:
        df[key] = 0 # initialize cluster columns as 0
    for i, row in df.iloc[indicies_with_tag].iterrows():
        # for each ticket containing a tag
        # fill in applicable one-hot-encoded column with 1
        if type(row.Ticket) != float:
            split = row.Ticket.split(' ')
            if len(split) > 1:
                for item in cluster_dict.items():
                    if split[0] in item[1]:
                        df[item[0]].iloc[i] = 1
    df = df.drop(columns=['Ticket'])
    return df

# Encode embarked
def encode_embarked(df, datasplit, encoding):
    # encode based on chosen method of encoding
    if encoding == 'travel_dist':
        # this is a rough estimate of the number of miles from Southampton, the first point of embarkation
        df['Embarked'] = df['Embarked'].replace(['S','C','Q'],[0,80,480])
    elif encoding == 'embark_order':
        # this is simply the order in which the ports were traversed, sequentially
        df['Embarked'] = df['Embarked'].replace(['S','C','Q'],[0,1,2])
    elif encoding == 'one_hot':
        # plain old one-hot, if you've given up
        df['Embarked_S'] = df['Embarked'].replace(['S','C','Q'],[1,0,0])
        df['Embarked_C'] = df['Embarked'].replace(['S','C','Q'],[0,1,0])
        df['Embarked_Q'] = df['Embarked'].replace(['S','C','Q'],[0,0,1])
        df = df.drop(columns=['Embarked'])
    else:
        print("Error. Incorrect entry for distance parameter. Possible values are:\ntravel_dist\nembark_order\none_hot")
    df = df.fillna(df.median())
    return df

# Run all preprocessing functions
def main(df, datasplit):
    # count nulls by column before replacing
    print(" \nTotal missing values by column in the data :\n\n", df.isnull().sum())
    # replace nulls in numerical columns with the column mean
    df = df.fillna(df.mean())
    # convert sex column into dummy variables
    df = sex_to_dummy(df)
    # encode ticket by tag
    df = encode_ticket(df, datasplit)
    # encode embarked by travel distance, sequence, or one-hot
    # third parameter must be one of: 'travel_dist', 'embark_order', 'one_hot'
    df = encode_embarked(df, datasplit, 'embark_order')
    return df

# Run preprocessing
train = main(train, 'train')
test = main(test, 'test')

# Output data
train.to_csv("data/train_clean.csv", index=False)
test.to_csv("data/test_clean.csv", index=False)


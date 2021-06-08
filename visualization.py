# Imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
train = pd.read_csv("data/train_clean.csv")
train.head()
train_df = pd.DataFrame(train)

sns.set(style="darkgrid")
sns.factorplot('Sex',data=train,kind='count')
sns.factorplot('Pclass',data=train_df,kind='count')

# Plot
survived_sex = train_df[train_df['Survived']==1]['Sex'].value_counts()
dead_sex = train_df[train_df['Survived']==0]['Sex'].value_counts()
df_sex = pd.DataFrame([dead_sex,survived_sex])
df_sex.index=['Did_not_Survive','Survived']
df_sex.plot(kind='bar',stacked=True,fig=(18,6),title='Sex')

# Plot
survived_pclass = train_df[train_df['Survived']==1]['Pclass'].value_counts()
dead_pclass = train_df[train_df['Survived']==0]['Pclass'].value_counts()
df_pclass = pd.DataFrame([dead_pclass,survived_pclass])
df_pclass.index=['Did_not_Survive','Survived']
df_pclass.plot(kind='bar',stacked=True,fig=(18,6),title='Pclass')

# Plot
# 0 is female and 1 is male, pecentage
feq_tab_sex = pd.crosstab(train_df['Sex'], train_df['Survived'])
fig_sex = feq_tab_sex.div(feq_tab_sex.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True)
fig_sex = plt.xlabel('Sex')
fig_sex = plt.ylabel('Percentage')

# Plot
# 0 is female and 1 is male, Number
feq_tab_sex = pd.crosstab(train_df['Sex'], train_df['Survived'])
fig_sex = feq_tab_sex.plot(kind="bar", stacked=True)
fig_sex = plt.xlabel('Sex')
fig_sex = plt.ylabel('Number')

# Plot
feq_tab_pclass = pd.crosstab(train_df['Pclass'], train_df['Survived'])
fig_pclass = feq_tab_pclass.plot(kind="bar", stacked=True)
fig_pclass = plt.xlabel('Pclass')
fig_pclass = plt.ylabel('Number')

# Plot
feq_tab_age = pd.crosstab(train_df['Age'], train_df['Survived'])
feq_tab_age

# Plot
fig_age = feq_tab_age.plot(kind="bar", stacked=True)
fig_age = plt.xlabel('Pclass')
fig_age = plt.ylabel('Number')


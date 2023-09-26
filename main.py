# 1 import  all the useful library


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 2 read the dataset
df=pd.read_csv('Shark Tank India Dataset.csv')
print(df)

# 3 Display the head of the data
df=df.head()
print(df)


# 4 Display the number of columns and rows with shape
df=df.shape
print(df)


# (5) Use describe function  to display the count, mean, std and max
df=df.describe()
print(df)


# (6) display detail of columns of the dataset
df=df.info()
print(df)


# (7) check missing values if any
df=df.isnull()
print(df)


# (8) Display columns
df=df.columns
print(df)


# (9) check deal value and count it
df=df['deal'].value_counts()
print(df)


# (10) one maximum take out pitcher amount
df=df[df['pitcher_ask_amount']==df['pitcher_ask_amount'].max()]
print(df)


# 11 one maximum deal amount
df=df[df['deal_amount']==df['deal_amount'].max()]
print(df)


# (12) maximum amt of shark
df=df[df['amount_per_shark']==df['amount_per_shark'].max()]
print(df)


# 13 minimum value of ask equity
df=df[df['ask_equity']==df['ask_equity'].min()]
print(df)


# 14 show only ashneer done deal
ash_veer=df[df['ashneer_deal']==1]
print(ash_veer)


# 15 Total amount invested on shark tank
ash_veer=[df[df['ashneer_deal']==1]['amount_per_shark'].sum()]
print(ash_veer)


# 16   show Ash veer deals with anupam
ashneer_deal= df[df['anupam_deal']==1]
print(ashneer_deal)


# 17 show ash deal with Aman
ashneer_deal = df[df['aman_deal'] == 1]
print(ashneer_deal)


# 18 show ashveer deal with Namita
ashneer_deal = df[df['namita_deal'] == 1]
print(ashneer_deal)


# 19 show Ashveer deal with vineeta_deal
ashneer_deal = df[df['vineeta_deal'] == 1]
print(ashneer_deal)


# 20 show Ashneer deal with Peyush
ashneer_deal = df[df['peyush_deal'] == 1]
print(ashneer_deal)


# 21 show Ashneer deal with Ghazal
ashneer_deal = df[df['ghazal_deal'] == 1]
print(ashneer_deal)


# 22 total equatiy and total amount of invested
eqt = df.groupby('ashneer_deal')['equity_per_shark'].sum().loc[1]
amt = df.groupby('ashneer_deal')['amount_per_shark'].sum().loc[1]
print("Total equity buy on shark tank",eqt,'%')
print("Total amount invested on shark tank",amt,"lakhs")


# 23 Analysis all are present in companies
list=['ashneer_present','anupam_present','aman_present','namita_present','vineeta_present','peyush_present','ghazal_present']
for i in list:
    p=df[i].sum()
    print(i,"present is front of " , p , "companies")


# 24 All are deals with how many companies
list=['ashneer_deal','anupam_deal','aman_deal','namita_deal','vineeta_deal','peyush_deal','ghazal_deal']
for i in list:
    d=df[i].sum()
    print(i," deal with " , d , "companies")

sns.countplot(data=df,x='total_sharks_invested')
plt.show()



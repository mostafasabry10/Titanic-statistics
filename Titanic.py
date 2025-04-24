
import numpy as np
import pandas as pd 
import plotly.express as px 
import streamlit as st
st.set_page_config(layout="wide", page_title = 'Simple DashBoard')

html_title = """<h1 style="color:red;text-align:center;"> Titanic statistics and plots </h1>"""
st.markdown(html_title,unsafe_allow_html=True)

df = pd.read_csv(r'G:\Mostafa 2\engineering\coursera and ITI\Data Science epsilon AI\All Sessions\session 24\Titanic-Dataset.csv',index_col = 0)
df.info()
df.describe()
df.describe(include = 'object')
df.isna().sum()
df.drop(['Cabin','Ticket','SibSp','Parch','Name'],axis = 1, inplace = True)
def convert (x):
    if pd.isna(x):
        return x
    else :
        return int(x)
df['Age'] = df['Age'].apply(convert).astype('Int64')
df.Fare = df.Fare.round(2)
def into (x):
    if x == 1:
        return 'First'
    elif x == 2:
        return 'Second'
    else :
        return 'Third'
df.Pclass = df.Pclass.apply(into)

col1,col2,col3,col4,col5 = st.columns(5)

survival_rate = df.groupby('Pclass')['Survived'].sum().reset_index()
col1.plotly_chart(px.bar(survival_rate,x='Pclass',y='Survived',width = 500,title = 'Survival rate per each Class'))

Survived_per_gender = df.groupby('Sex')['Survived'].sum().sort_values(ascending = False).reset_index()
col2.plotly_chart(px.bar(Survived_per_gender,x ='Sex',y = 'Survived',width = 400, title = 'Survived rate for each gender'))

Average_Age_per_class = df.groupby('Pclass')['Age'].mean().round(2).reset_index()
col3.plotly_chart(px.bar(Average_Age_per_class, x = 'Pclass', y = 'Age',width = 600, title = 'Average rate for each Class'))

Average_fare_per_class = df.groupby('Pclass')['Fare'].mean().round(2).sort_values(ascending = False).reset_index()
col4.plotly_chart(px.bar(Average_fare_per_class, x = 'Pclass' , y = 'Fare',width = 600,title = 'Average Fare For each Class'))

Survived_per_Embarked = df.groupby('Embarked')['Survived'].sum().sort_values(ascending = False).reset_index()
col5.plotly_chart(px.bar(Survived_per_Embarked , x = 'Embarked' , y = 'Survived',width = 600, title = 'Number of Survived people for each Embarked'))

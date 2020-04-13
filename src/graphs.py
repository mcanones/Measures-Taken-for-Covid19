import pandas as pd 
import nbformat
import plotly.graph_objects as go
import plotly.express as px
from src.table import *

def make_graphs(df,p1,p2):

    #SUB-DATASET
    sub_df=df[(df['ISO_ALP_2']==p1)|(df['ISO_ALP_2']==p2)]
    #GRAPH CONFIRMED
    fig = px.line(sub_df, x='ENTRY_DATE', y='CONFIRMED' , range_x=['2020-03-14','2020-04-09'], color='ISO_ALP_2')
    fig.write_image('./output/graph_confirmed'+p1+p2+'.png')
    #GRAPH DEATHS
    fig = px.line(sub_df, x='ENTRY_DATE', y='DEATHS' , range_x=['2020-03-14','2020-04-09'], color='ISO_ALP_2')
    fig.write_image('./output/graph_deaths'+p1+p2+'.png')
    #GRAPH MEASURES
    fig = px.scatter(sub_df, x='CATEGORY', y='CONFIRMED' , range_x=['2020-03-14','2020-04-09'], color=sub_df['ISO_ALP_2'])
    fig.write_image('./output/graph_measures'+p1+p2+'.png')
    #GRAPH TABLE 
    generate_small_table(df,p1)
    generate_small_table(df,p2)

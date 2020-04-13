import pandas as pd 
import nbformat
import plotly.graph_objects as go
import plotly.express as px

def make_graphs(df,p1,p2,p3):

    #GRAPHS ONE COUNTRY
    sub_df=df[['CONFIRMED','DEATHS','ENTRY_DATE','REGION','ISO_ALP_2']]
    sub_df=sub_df[sub_df['ISO_ALP_2']==p1]
    fig = px.line(sub_df, x='ENTRY_DATE', y='CONFIRMED' , range_x=['2020-03-14','2020-04-09'])
    fig.write_image('./output/graph_confirmed'+p1+'.png')
    fig = px.line(sub_df, x='ENTRY_DATE', y='DEATHS' , range_x=['2020-03-14','2020-04-09'])
    fig.write_image('./output/graph_deaths'+p1+'.png')

    #TABLE ONE COUNTRY
    sub_df=df[['REGION','ISO_ALP_2','ENTRY_DATE','MEASURE','COMMENTS']]
    sub_df=sub_df[sub_df['ISO_ALP_2']==p1]
    sub_df=sub_df[sub_df['COMMENTS']!='Unknown']

    fig = go.Figure(data=[go.Table(
        columnorder = [1,2,3,4,5],
        columnwidth = [50,70,100,100,600],
        header=dict(values=list(sub_df.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[sub_df.REGION, sub_df.ISO_ALP_2, sub_df.ENTRY_DATE, sub_df.MEASURE,  sub_df.COMMENTS],
                fill_color='lavender',
                align='left')),
    ])
    fig.write_image('./output/table.png')
    fig.show()

    #GRAPH TWO COUNTRIES
    df_2=df[df['CATEGORY']==p3]
    df_2=df_2[(df_2['ISO_ALP_2']==p1) | (df_2['ISO_ALP_2']==p2)]
    fig = px.scatter(df_2, x='ENTRY_DATE', y='CONFIRMED' , range_x=['2020-03-14','2020-04-09'], color=df_2['ISO_ALP_2'])
    fig.write_image('./output/graph_confirmed'+p3+p1+p2+'.png')

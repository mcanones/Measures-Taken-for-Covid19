import pandas as pd 
import numpy as np
import nbformat
import plotly.graph_objects as go
import plotly.express as px

def generate_big_table(df,p):

    sub_df=df[['REGION','ISO_ALP_2','ENTRY_DATE','MEASURE','COMMENTS']]
    sub_df=sub_df[sub_df['ISO_ALP_2']==p]
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

    fig.show()

def generate_small_table(df, p):
    
    #Generate subdataset 
    sub_df=df[df['ISO_ALP_2']==p]
    sub_df=sub_df[['ENTRY_DATE','CATEGORY','MEASURE']]
    sub_df["health_m"]=np.where(sub_df["CATEGORY"].isin(["Public health measures"]),1,0)
    sub_df["movement_m"]=np.where(sub_df["CATEGORY"].isin(["Movement restrictions"]),1,0)
    sub_df["social_m"]=np.where(sub_df["CATEGORY"].isin(["Social distancing"]),1,0)
    sub_df["gov_m"]=np.where(sub_df["CATEGORY"].isin(["Governance and socio-economic measures"]),1,0)
    sub_df["lockdown"]=np.where(sub_df["CATEGORY"].isin(["Lockdown"]),1,0)
    sub_df=sub_df.groupby(["ENTRY_DATE"]).sum()
    dates=sub_df.index

    #Generate table
    fig = go.Figure(data=[go.Table(
        columnorder = [1,2,3,4,5,6],
        columnwidth = [10,10,10,10,10,10],
        header=dict(values=['ENTRY_DATE','health_m', 'movement_m', 'social_m', 'gov_m', 'lockdown'],
                    fill_color='paleturquoise',
                    align='center'),
        cells=dict(values=[dates, sub_df.health_m, sub_df.movement_m, sub_df.social_m, sub_df.gov_m, sub_df.lockdown],
                    fill_color='lavender',
                    align='center')),
        ])
        
    #Save table
    fig.write_image('./output/table'+p+'.png')


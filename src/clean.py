import numpy as np
import pandas as pd
import datetime
import pycountry

def clean_df(df):
    
    #Select columns of interest
    columns=['COUNTRY', 'REGION','CATEGORY', 'MEASURE', 'COMMENTS', 'SOURCE', 'ENTRY_DATE']
    df=df[columns]

    #Drop duplicates
    df = df.drop_duplicates()

    #Drop rows with null values
    df = df[df.isnull().sum(axis=1) < 5]

    #Filling Null Values
    df=df.fillna('Unknown')
    df=df.reset_index(drop=True)

    #Correcting ENTRY_DATE column
    for i,e in df['ENTRY_DATE'].items():
        fecha=e.split('-')
        fecha=[fecha[2],fecha[1],fecha[0]]
        fecha=[int(e) for e in fecha]
        df['ENTRY_DATE'][i]=datetime.date(*fecha)

    #Correction COUNTRY column
    correct_countries={'Czech republic':'Czech Republic','China, Hong Kong Special Administrative Region':'China','Congo DR':'Congo',
                        'Korea DPR':'Korea Republic Of', 'Moldova Republic of':'Moldova Republic Of', "Korea Republic of":"Korea Republic Of"}
    df=df.replace({"COUNTRY": correct_countries})

    #Correcting ISO column

    input_countries=list(df['COUNTRY'].unique())
    countries = {}
    for country in pycountry.countries:
        countries[country.name] = country.alpha_2
    df["ISO_ALP_2"] = df["COUNTRY"]
    df=df.replace({"ISO_ALP_2": countries})

    others={'Bolivia':'BO', 'Venezuela':'VE', 'Congo':'CD','United States of America':'US', 
    'Tanzania':'TZ', 'Palestine':'PS', 'Syria':'SY', 'Korea Republic Of':'KP', 'Czech Republic':'CZ', 
    'Lao PDR':'LA', 'Micronesia':'FM', 'Moldova Republic Of':'MD', 'Iran':'IR', 'North Macedonia Republic Of':'MK',}
    df=df.replace({"ISO_ALP_2": others})


    #Correcting MEASURE column
    for i,e in df['MEASURE'].items():
        df['MEASURE'][i]=e.lower()
        if 'ÿ' in e:
            df['MEASURE'][i]=e.replace('ÿ','')
    
    #Correcting SOURCE column
    for i,e in df['SOURCE'].items():
        df['SOURCE'][i]=e.lower()
        if '.' in e:
            df['SOURCE'][i]=e.replace('.','')

    df.to_csv("../output/clean.csv")

    return df



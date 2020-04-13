import numpy as np
import pandas as pd
import datetime
from req_inf import *

def obtain_data(df):
    countries=df['ISO_ALP_2'].unique()
    lista=[]
    for e in countries:
        try:
            country_info=request_inf(e)
            sub_info=[(e['confirmed'],e['deaths'],e['date']) for e in country_info['data']['timeline']]
            dicty={}
            for i,e in enumerate(sub_info):
                date_aux=sub_info[i][2].split('-')
                date_aux2=[int(e) for e in date_aux]
                dicty={
                    'CONFIRMED':int(sub_info[i][0]),
                    'DEATHS':int(sub_info[i][1]),
                    'ENTRY_DATE':datetime.date(*date_aux2),
                    'ISO_ALP_2':country_info['data']['code'],
                    'POPULATION':int(country_info['data']['population'])
                      }
                lista.append(dicty)
        except:
            pass
    return lista 
import numpy as np
import pandas as pd
import datetime
from clean import * 
from req_inf import *
from data_mining import *

df = pd.read_csv('../input/covid.csv', encoding='latin-1')

df=clean_df(df)

new_cols=obtain_data(df)

df_enriched=pd.DataFrame(new_cols)

res = pd.merge(df, df_enriched, how='inner', on=['ISO_ALP_2','ENTRY_DATE'])

res[['CONFIRMED','DEATHS','POPULATION']]=res[['CONFIRMED','DEATHS','POPULATION']].astype(int)

res.to_csv("../output/mining.csv")

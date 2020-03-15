import pandas as pd 
import numpy as np 
import matplotlib as mpl 

feature = '.*\|(.*\|)'

#pf=pd.read_csv('properatti.csv')
#pfp=pf.groupby('place_name', as_index=False)['price_aprox_usd'].mean()

df=pd.read_csv('properatti.csv')
#df['place_with_parent_names'] = df['place_with_parent_names']\
#                                .str.extract('.*\|(.*\|)', expand=False).astype('str')

oldplace = df['place_with_parent_names']\
                               .str.extract('.*\|(.*\|)', expand=False).astype('str')
newplace = df['place_with_parent_names']\
                                .str.extract('.*\|(.*\|)..+?\|', expand=False).astype('str')
                              
dfpp=df.pivot_table('price_aprox_usd', [newplace, oldplace], aggfunc={'price_aprox_usd':'mean'})
#for i in oldplace:
# if i in newplace:
#    print('YES')
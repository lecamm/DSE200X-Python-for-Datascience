# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 14:13:56 2019

@author: lecam
"""
#% load libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#load data
data = pd.read_csv('../Week5-Visualization/world-development-indicators/Indicators.csv')
#%%analysis
indicators=data.IndicatorName.unique().tolist()
interest = [s for s in indicators if "CO2" in s]
Indic=['Electricity production from renewable sources, excluding hydroelectric (% of total)',
       'Fossil fuel energy consumption (% of total)',
       'Electricity production from oil, gas and coal sources (% of total)',
       'CO2 emissions (metric tons per capita)',
       'CO2 emissions from electricity and heat production, total (% of total fuel combustion)']
#,'GDP per capita (current US$)'
ds=data[data.IndicatorName.isin(Indic)]
countries=ds.CountryName.unique().tolist()
int_countries= [s for s in countries if "all income" in s]
int_countries.extend(['North America','European Union'])

check=pd.DataFrame(columns=Indic,index=int_countries)
for i in int_countries:
    for j in Indic:
        check.loc[i,[j]]=ds.Year[ds.CountryName==i][ds.IndicatorName==j].count()
check['min']=[ds.Year[ds.CountryName==i][ds.IndicatorName==Indic[0]].min() for i in int_countries]
check['max']=[ds.Year[ds.CountryName==i][ds.IndicatorName==Indic[0]].max() for i in int_countries]
#%%evolution per year of renewable energy production in different regions of the world
countries_filter=ds.CountryName.isin(int_countries)
year_filter=(ds.Year>=1971)&(ds.Year<=2012)
ds=ds[countries_filter][year_filter]

#%%visualization
plt.rcParams.update({'font.size': 12})
plt.close('all')
colors = list(plt.cm.tab20(np.linspace(0,1,len(int_countries))))
fig, ax = plt.subplots(figsize=(12,6))
ax.set_prop_cycle('color', colors)
[plt.plot(ds.Year[ds.CountryName==i][ds.IndicatorName==Indic[0]],ds.Value[ds.CountryName==i][ds.IndicatorName==Indic[0]],'.-') for i in int_countries]
plt.legend(int_countries)
plt.ylabel(Indic[0][:46]+'\n'+Indic[0][46:])
plt.xlabel('Year')
#plt.title('Evolution of renewable energy production in the world',fontsize=20)
#mng = plt.get_current_fig_manager()
#mng.window.showMaximized()
plt.savefig('Evol_renewables.png')
#%%
plt.close('all')
fig, ax = plt.subplots(figsize=(14,8))
ax.set_prop_cycle('color', colors)
[plt.plot(ds.Year[ds.CountryName==i][ds.IndicatorName==Indic[-1]],ds.Value[ds.CountryName==i][ds.IndicatorName==Indic[-1]],'.-') for i in int_countries]
plt.legend(int_countries,loc='lower right')
plt.ylabel(Indic[-1][:51]+'\n'+Indic[-1][51:])
plt.xlabel('Year')
plt.ylim(15,55)
#mng = plt.get_current_fig_manager()
#mng.window.showMaximized()
plt.savefig('Evol_CO2.png')
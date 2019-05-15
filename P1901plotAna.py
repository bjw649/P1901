#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import plotly as ly
import pathlib
import os

plt.style.use("ggplot")

print(os.getcwd())
tnp = "../Data/R6_Date_Temp.csv"  #ChlA, DO, Temp, DIN, SRP, Tbdty
df = pd.read_csv(tnp)
df.head()

df["Date"] = pd.to_datetime(df["Date"], errors='coerce', dayfirst=True )
df.head()
#%%
df=df.set_index('Date')
df.head()

tnp = "../Data/AlgaeR6.csv"  #ChlA, DO, Temp, DIN, SRP, Tbdty
df1 = pd.read_csv(tnp)
df1.head()
#%%
df1["Date"] = pd.to_datetime(df1["Date"], errors='coerce', dayfirst=True )
df1.head()
#%%
df1 = df1.set_index('Date')
df['Anabaena'] = df1['Anabaena']
df.head()
df.tail()
#%%
df = df.interpolate('time').reindex(Anabaena)
df.tail()



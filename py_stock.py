import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib as style
import pandas_datareader.data as web

style.use('ggplt')
start = dt.datetime(2000,1,1)
end = dt.datetime(2016,12,31)   
df = web.DataReader("TSLA","yahoo",start,end)
# print(df)

df.to_csv("tesla.csv")

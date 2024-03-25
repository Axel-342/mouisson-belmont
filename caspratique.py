import pandas as pd

df = pd.read_csv('test (3).csv').dropna()

df = df(columns=['Series_reference','Suppressed','Suppressed','UNITS','Magnitude','Subject','Group','Series_title_1','Series_title_3','Series_title_4','Series_title_5'])

df.to_csv('fichierfin',index=False)
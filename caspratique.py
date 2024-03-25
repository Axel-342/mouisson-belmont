import pandas as pd

df = pd.read_csv('test.csv').dropna()

df = df.drop(columns=['Series_reference','Suppressed','UNITS','Magnitude','Subject','Group','Series_title_1','Series_title_3','Series_title_4','Series_title_5'])

df.to_csv('fichierfin.csv', index=False)
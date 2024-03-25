import pandas as pd

df = pd.read_csv('test.csv')

df = df.drop(columns=['Series_reference','Suppressed','Suppressed.1','UNITS','Magnitude','Subject','Group','Series_title_1','Series_title_3','Series_title_4','Series_title_5']).dropna()

df.to_csv('fichierfin.csv', index=False)

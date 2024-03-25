import pandas as pd

df = pd.read_csv('test.csv')

df = df.drop(columns=['Series_reference','Suppressed','Suppressed.1','UNITS','Magnitude','Subject','Group','Series_title_1','Series_title_3','Series_title_4','Series_title_5']).dropna()

filtered_df = df[df['Series_title_2'].str.contains('Credit|Debit|Services', na=False)]

filtered_df.to_csv('fichierfin.csv', index=False)





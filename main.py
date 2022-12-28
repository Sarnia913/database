import pandas as pd
gsheetid='1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
sheet_name='Class'
gsheet_url='https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}'.format(gsheetid,sheet_name)
df=pd.read_csv(gsheet_url)
print(df)
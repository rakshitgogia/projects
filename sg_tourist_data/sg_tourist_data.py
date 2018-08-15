import pandas as pd

df = pd.read_excel("sg_visitor_arrivals_2017.xlsx",
                   sheet_name = 1, skiprows=range(7), skipfooter=10, usecols=12)
print(df.head())
print(df.tail())

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("sg_visitor_arrivals_2017.xlsx", index_col=0,
                   sheet_name = 1, skiprows=range(8), skipfooter=10, usecols=12)
df.index = df.index.str.lower()
plt.plot(df.loc['india'])
plt.xlabel("Month")
plt.ylabel("Number of tourist arrivals")
plt.show()

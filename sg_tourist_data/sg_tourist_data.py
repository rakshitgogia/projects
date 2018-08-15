import pandas as pd
import matplotlib.pyplot as plt
import sys

query = 'Total'
# query_list = ["SOUTHEAST ASIA", "GREATER CHINA", "NORTH ASIA", "SOUTH ASIA",
#                   "WEST ASIA", "AMERICAS", "EUROPE", "OCEANIA", "AFRICA"]
query_list = ["NORTH ASIA", "SOUTH ASIA", "EUROPE", "OCEANIA"]
query = query_list
if len(sys.argv) > 1:
    query = sys.argv[1]
if type(query) == list:
    query_lower = [word.lower() for word in query]
elif type(query) == str:
    query_lower = query.lower()
df = pd.read_excel("sg_visitor_arrivals_2017.xlsx", index_col=0,
                   sheet_name=1, skiprows=range(8), skipfooter=10, usecols=12)
df.index = df.index.str.lower()
df = df.T
df[query_lower].plot()
plt.xlabel("Month")
if query_lower != "total" and type(query_lower) != list:
    plt.ylabel("Number of tourist arrivals from " + str(query))
else:
    plt.ylabel("Number of tourist arrivals")

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
# import sys
import argparse

query = 'Total'


parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='This program uses the pandas and matplotlib libraries to '
                'provide a visualisation for Singapore\'s tourist arrival data in 2017')

parser.add_argument('-q', '--query', nargs= '+',
                    help='Name of specific country or region you want '
                         'a visualisation for')
args = parser.parse_args()
if args.query:
    query = ' '.join(args.query)
# query_list = ["SOUTHEAST ASIA", "GREATER CHINA", "NORTH ASIA", "SOUTH ASIA",
#                   "WEST ASIA", "AMERICAS", "EUROPE", "OCEANIA", "AFRICA"]
# query_list = ["NORTH ASIA", "SOUTH ASIA", "EUROPE", "OCEANIA"]
# query = query_list
# if len(sys.argv) > 1:
#     query = sys.argv[1]
if type(query) == list:
    query_lower = [word.lower() for word in query]
elif type(query) == str:
    query_lower = query.lower()
df = pd.read_excel("sg_visitor_arrivals_2017.xlsx", index_col=0,
                   sheet_name=1, skiprows=range(8), skipfooter=10, usecols=12)

df.index = df.index.str.lower()
# transpose the data set
df = df.T
xticks = df.index
# df['month'] = df.iloc[0].dt.strftime('%b')
xticks_label = xticks.strftime('%b')
xticks_label = list(xticks_label)
# type(xticks)
df[query_lower].plot()
plt.xlabel("Month")
plt.xticks(xticks, xticks_label)
if query_lower != "total" and type(query_lower) != list:
    plt.ylabel("Number of tourist arrivals in 2017 from " + str(query))
else:
    plt.ylabel("Number of tourist arrivals in 2017")

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import argparse

# default: shows the total tourist arrivals if no command-line arguments
# for a specific region are provided
query = 'total'

# parse command line arguments
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='This program uses pandas and matplotlib libraries to provide'
                ' a visualisation for Singapore\'s tourist arrival data in 2017')

parser.add_argument('-q', '--query', nargs= '+', action='append',
                    help='Name of specific country or region you want '
                         'a visualisation for')
args = parser.parse_args()
if args.query:
    query = [' '.join(region) for region in args.query]
if len(query) == 1:
    query = ' '.join(query)

# convert to lower case
if type(query) == list:
    query_lower = [word.lower() for word in query]
else:
    query_lower = query.lower()
# read from excel file
df = pd.read_excel("sg_visitor_arrivals_2017.xlsx", index_col=0,
                   sheet_name=1, skiprows=range(8), skipfooter=10, usecols=12)
# convert country names in dataframe to lower case
df.index = df.index.str.lower()
# transpose the data set
df = df.T

df[query_lower].plot()
# add features such as x and y axes labels and x axis ticks
plt.xlabel("Month")
if query_lower != "total" and type(query_lower) != list:
    plt.ylabel("Number of tourist arrivals in 2017 from " + str(query))
else:
    plt.ylabel("Number of tourist arrivals in 2017")
xticks_labels = list(df.index.strftime('%b'))
plt.xticks(df.index, xticks_labels)

plt.show()

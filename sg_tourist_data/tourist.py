import pandas as pd
import matplotlib.pyplot as plt
import argparse


def get_query():
    # default: shows the total tourist arrivals if no command-line arguments
    # for a specific region are provided
    query = 'total'
    query = ["SOUTHEAST ASIA", "GREATER CHINA", "NORTH ASIA", "SOUTH ASIA",
             "WEST ASIA", "AMERICAS", "EUROPE", "OCEANIA", "AFRICA"]
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
    return query


def to_lower(query):
    # convert query to lower case
    if type(query) == list:
        query_lower = [word.lower() for word in query]
    else:
        query_lower = query.lower()
    return query_lower


def make_plot(query_lower, query):
    # read from excel file
    df = pd.read_excel("sg_visitor_arrivals_2017.xlsx", index_col=0,
                       sheet_name=1, skiprows=range(8), skipfooter=10,
                       usecols=12)
    # convert country names in dataframe to lower case
    df.index = df.index.str.lower()
    # transpose the data set
    df = df.T
    try:
        plt.plot(df[query_lower], marker='x')
    except KeyError:
        print("Invalid search query")
        exit(1)
    # add features such as x and y axes labels and x axis ticks
    plt.xlabel("Month")
    if type(query_lower) == list:
        plt.ylabel("Number of tourist arrivals in 2017")
        plt.legend(query)
        # generate filename from query_lower
        query_lower_no_spaces = [word.replace(" ", "") for word in query_lower]
        filename = "_".join(query_lower_no_spaces)
    elif query_lower == "total":
        plt.ylabel("Number of tourist arrivals in 2017")
        filename = query_lower
    else:
        plt.ylabel("Number of tourist arrivals in 2017 from " + str(query))
        filename = query_lower.replace(" ", "")
    xticks_labels = list(df.index.strftime('%b'))
    plt.xticks(df.index, xticks_labels)
    # save the plot and display it
    plt.savefig('examples/' + filename + '.png', bbox_inches='tight')
    plt.show()


my_query = get_query()
my_query_lower = to_lower(my_query)
make_plot(my_query_lower, my_query)


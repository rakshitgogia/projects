from datetime import date
import sys

total_swipes = 125
first_day = date(2018, 9, 3)
last_day = date(2018, 12, 15)

if (len(sys.argv) != 2):
    print("Please enter your meal plan balance!")
    exit(1)
num_swipes = int(sys.argv[1])
days_since = date.today() - first_day
days_till = last_day - date.today()
days_in_semester = last_day - first_day
current_rate = (total_swipes - num_swipes)/days_since.days
required_rate = num_swipes/days_till.days

color_red = '\033[91m'
color_end = '\033[0m'
# report
print("From your", total_swipes, "swipes meal plan, you have used", total_swipes - num_swipes, "swipes.")
print("Since", first_day.strftime("%B %-d,"),
      "you have been using", color_red + "{}".format(round(current_rate, 2)) + color_end, "swipes per day.")
print("To survive until", last_day.strftime("%B %-d,"), "you need to use",
      color_red + "{}".format(round(required_rate, 2)) + color_end, "swipes per day.")

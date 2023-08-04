# with open("weather_data.csv") as data: # this is a hassle of code because of all the cleaning required for the data
#     temporary_data = data.readline()

# import csv  # with this portion its much better but not the best!
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#             temperatures.append(row)
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)

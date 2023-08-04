# why not directly read data? because it's a hassle to clean the data with 'with open("weather_data.csv") as data_file: and then data = data_file.readlines()

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

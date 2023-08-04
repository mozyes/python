import pandas

data = pandas.read_csv("weather_data.csv")

monday = data[data.day == "Monday"]
monday_temperature = int(monday.temp)
temp_f = monday_temperature * 1.8 + 32
print(temp_f)

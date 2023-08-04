import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()

# using series method. series is basically column and whole table is basically frame.
print(data["temp"].max())
print(data["temp"].mean())

# get data from column
print(data["condition"]) #treating it like dictionary
# can be called like print(data.condition) #treating it like object

# get data from row
print(data[data["day"] == "Monday"])

# get data from max temp.
print(data[data.temp == data["temp"].max()])  

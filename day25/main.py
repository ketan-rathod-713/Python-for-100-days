
# csv = comma separated values
# very common method for displaying data tabular like spread shit
#
# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# Inbuilt library for working with tabular csv file
# import csv
# # inbuilt library
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1]!="temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

# what if we have more complex data then it is not sufficient as lot code to write

# so now pandas
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
#
# # pandas has series and dafaFrame objects
# # check it by type["temp]
#
# print(type(data))
# print(type(data["temp"]))
#
# # we can convert data frame to lots of file stuff and do that see docs
#
# data_to_dict = data.to_dict()
# print(data_to_dict)
#
# # convert series to list
# dataTempList = data["temp"].to_list()
# print(dataTempList)
#
# ans = sum(dataTempList)/len(dataTempList)
# print(ans)
#
# print(data["temp"].mean())
# # There are lots of data series methods max, min and so on
#
# print(data["temp"].max())
#
# print(data.temp) # This is also valid , be carefull about attribute , it is like dictionary like here
#
# # How to get specific row from table
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])
# # filter that column by condition
#
# # What if we want that particular row's data
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# # create dataframe from any data
#
# data_dict = {
#     "students":["any","james","just"],
#     "scores":[23,34,23]
# }
#
# data1 = pandas.DataFrame(data_dict)
# print(data1)
# data1.to_csv("new_data.csv") # new csv file willl be created

# later we will be seeing numPy , matplotlib

# Now use the squiral data for data Analysis

# count the color of squiral
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


grey = data[data["Primary Fur Color"] == "Gray"]
grey_count = len(grey)

red = data[data["Primary Fur Color"] == "Cinnamon"]
red_count = len(red)

black = data[data["Primary Fur Color"] == "Black"]
black_count = len(black)

print(grey_count)
print(red_count)
print(black_count)

# Now convert it into csv by converting it into data frame

data_dict = {
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count" : [grey_count,red_count,black_count]
}

print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
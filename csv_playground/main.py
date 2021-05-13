# with open("csv_playground/weather_data.csv") as file:
#     content = []
#     for line in file.readlines():
#         content.append(line.strip().split(','))

# print(content)

# import csv

# with open("csv_playground/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temps = []
#     for row in data:
#         if row[1] != "temp":
#             temps.append(int(row[1]))

# print(temps)

import pandas
# from pandas.core.frame import DataFrame

# data = pandas.read_csv("csv_playground/weather_data.csv")
# print(data)
# print(data["temp"])

# print(data.temp)
# print(data.temp.mean())
# print(data.temp.max())
# # get a row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

## create a DataFrame

# data_dict = {
#     "fruits": ["Apple", "Pears", "Strawberry", "Blueberry"],
#     "amount": [5, 7, 15, 32]
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("csv_playground/fruits.csv")

data = pandas.read_csv("csv_playground/2018_central_park_squirrel_census_squirrel_data.csv")
fur_data = data["Primary Fur Color"]

red = fur_data[fur_data == "Cinnamon"].count()
grey = fur_data[fur_data == "Gray"].count()
black = fur_data[fur_data == "Black"].count()

data_dict = {
    "fur color": ["Cinnamon", "Gray", "Black"],
    "Squirrel population": [red, grey, black]
}
data_framed_data = pandas.DataFrame(data_dict)
data_framed_data.to_csv("csv_playground/squirrel_count.csv")
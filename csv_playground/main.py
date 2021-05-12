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
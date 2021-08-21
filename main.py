# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)


# import pandas
#
# data = pandas.read_csv('weather_data.csv')
# monday = (data[data.day == 'Monday'])
#
#
# def farenheight_converter(celsius):
#     return ((celsius * (9/5)) + 32)
#
# print(farenheight_converter(monday.temp))
import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

grey_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_count = len(data[data['Primary Fur Color'] == 'Black'])
print(grey_count)
print(red_count)
print(black_count)

squirrel_dict = {
    "Fur Color" : ['gray', 'red', 'black'],
    'Number' : [grey_count, red_count, black_count]
}
squirrel_summary = pandas.DataFrame(squirrel_dict)
squirrel_summary.to_csv('squrrel_summary.csv')
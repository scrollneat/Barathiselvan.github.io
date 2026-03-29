# import csv
# with open("PYTHON_PROJECT/Day - 25/weather_data.csv", 'r') as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#     for i in data:
#         if i[1] != 'temp':
#             temperature.append(int(i[1]))
#     print(temperature)

# To get one column values above lines of code needs to be written. that is why we are going to use Pandas library

import pandas as pd
import numpy as np
data = pd.read_csv("PYTHON_PROJECT/Day - 25/weather_data.csv")
print(data)

new_data = data.to_dict()
print(new_data)

temp_list = data['temp'].to_list()
print(temp_list)

print(data['temp'])
print(data['temp'].mean())
print(data['temp'].max())

#Get Data from Column
print(data['condition'])
print(data.condition)
# both are same above


#to get column
new = data[data.day == 'Monday']
print(new)

#row of data which has highest temperature
hig_temp = data[data.temp == data.temp.max()]
print(hig_temp)

#to access specific column in a specific table
monday = data[data.day == 'Monday']
print(monday.condition)
fah_temp= monday.temp[0]
print((fah_temp*1.8)+32)
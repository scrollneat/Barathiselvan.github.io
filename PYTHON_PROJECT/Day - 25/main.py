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
data = pd.read_csv("PYTHON_PROJECT/Day - 25/weather_data.csv")
print(data['temp'])
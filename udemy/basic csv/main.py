# import csv
# with open("weather.csv") as file:
#     csv_object = csv.reader(file)
#     for i in csv_object:
#         print(i)

import pandas

data = pandas.read_csv("weather.csv")
data_dict = data.to_dict()

date =[]
temp = []
humidity = []
wind_speed = []
condition =[]
total = [date,temp,humidity,wind_speed,condition]
i = 0
for key in data_dict.keys():

    for keyin,value in data_dict[key].items():
        listin = [keyin, value]
        total[i].append(listin)
    i+=1

for val in total:
    print(val)
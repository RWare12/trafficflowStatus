import json
import csv

# light - 25
# mod - 50
# heavy - 75

northOrSouth = ''
csvHeader = ['Street','Status','Lane Points','% Observed']
myData = []
myData.append(csvHeader)

# while (northOrSouth is not 'n' or northOrSouth is not 's'):
#     northOrSouth = input('n = northbound / s = southbound: ')

    # if(northOrSouth is 'n'):
with open('northbound.json') as f:
    trafficData = json.load(f)
    for data in range(len(trafficData)):
        tempData = []
        status = trafficData[data].get('northbound').get('status').replace('light','25').replace('mod','50').replace('heavy','75')
        street = trafficData[data].get('line')
        tempData = [street,status,'1','100']
        myData.append(tempData)
            


# with open('northbound.json') as f:
#     data = json.load(f)

# print(data[0].get("northbound").get("status"))


# print(data[0])
# print(data[0].get("northbound"))


# print(data[0].get("southbound"))
# print(data[0].get("southbound").get("status"))

# print(data[0].get('line'))
# print(myData)
# train = []
# train = ['asdsasa','asdsadas','adsad','adsad']
# myData.append(train)
# train = []
# train = ['asdsasa','asdsadas','adsad','adsad']
# myData.append(train)

myFile = open('example2.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
     
print("Writing complete")


print(myData)






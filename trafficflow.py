import json
import csv
import saveCsvFile

# light - 25
# mod - 50
# heavy - 75

northOrSouth = ''
streetChoice = ''
bound = ''
csvHeader = ['Street','Status','Lane Points','% Observed']
streetName = ['QUEZON AVE','ORTIGAS','ESPAA','C5','EDSA','SLEX','COMMONWEALTH','ROXAS BLVD','MARCOS HIGHWAY']
myData = []
myData.append(csvHeader)
trafficData = ''

with open('trafficflowStatus.json') as f:
    trafficData = json.load(f)

# getting direction whether north or south
while True:
    northOrSouth = input('n = northbound / s = southbound: ')
    if 'n' in northOrSouth:
        break
    elif 's' in northOrSouth:
        break
    else:
        print('Invalid Input')

    
for sName in range(len(streetName)):
    print(sName+1,'-'+streetName[sName])

# getting specific street
while True:
    try:
        streetChoice = int(input('Enter Street[1-9]: '))
        if(streetChoice > 9):
            print("Invalid Input")
        elif(streetChoice < 0):
            print("Invalid Input")
        else:
            break
    except:
        print("Invalid Input!")

# process if northbound
if(northOrSouth is 'n'):
    for data in range(len(trafficData)):
        bound = 'Northbound'
        sStreet = trafficData[data].get('line').split(' ')
        if streetName[streetChoice-1].replace(" AVE","").replace(" BLVD","").replace(" HIGHWAY","") in sStreet[0]:
            tempData = []
            status = trafficData[data].get('northbound').get('status').replace('light','25').replace('mod','50').replace('heavy','75')
            street = trafficData[data].get('line')
            tempData = [street,status,'1','100']
            myData.append(tempData)

# process if southbound
if(northOrSouth is 's'):
    for data in range(len(trafficData)):
        bound = 'Southbound'
        sStreet = trafficData[data].get('line').split(' ')
        if streetName[streetChoice-1].replace(" AVE","").replace(" BLVD","").replace(" HIGHWAY","") in sStreet[0]:
            tempData = []
            status = trafficData[data].get('northbound').get('status').replace('light','25').replace('mod','50').replace('heavy','75')
            street = trafficData[data].get('line')
            tempData = [street,status,'1','100']
            myData.append(tempData)

print(myData)
saveCsvFile.saveFile(myData,bound.lower(),streetName[streetChoice-1].replace(" ","_").lower())

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
streetName = ['QUEZON AVE','ORTIGAS','ESPAA','C5','EDSA','SLEX','COMMONWEALTH','ROXAS_BLVD','MARCOS_HIGHWAY']
myData = []
myData.append(csvHeader)

while True:
    northOrSouth = input('n = northbound / s = southbound: ')
    if northOrSouth is 'n' or 's':
        break
    else:
        print('Invalid Input')

    
for sName in range(len(streetName)):
    print(sName+1,'-'+streetName[sName])

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

print(streetName[streetChoice-1])


if(northOrSouth is 'n'):
    with open('trafficflowStatus.json') as f:
        trafficData = json.load(f)
        for data in range(len(trafficData)):
            bound = 'Northbound'
            if streetName[streetChoice-1] in trafficData[data].get('line'):
                tempData = []
                status = trafficData[data].get('northbound').get('status').replace('light','25').replace('mod','50').replace('heavy','75')
                street = trafficData[data].get('line')
                tempData = [street,status,'1','100']
                myData.append(tempData)


if(northOrSouth is 's'):
    with open('trafficflowStatus.json') as f:
        trafficData = json.load(f)
        for data in range(len(trafficData)):
            bound = 'Southbound'
            if streetName[streetChoice-1] in trafficData[data].get('line'):
                tempData = []
                status = trafficData[data].get('northbound').get('status').replace('light','25').replace('mod','50').replace('heavy','75')
                street = trafficData[data].get('line')
                tempData = [street,status,'1','100']
                myData.append(tempData)


print(myData)
saveCsvFile.saveFile(myData,bound,streetName[streetChoice-1])







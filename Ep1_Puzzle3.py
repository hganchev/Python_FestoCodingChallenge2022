# 1.3 Place Sequence
# In the galaxy, twelve places are maintained by the galactic government: Bio-Lab, Factory, 
# Shopping Mall, Food Plant, Office Station, Gym, Starship Garage, Happy-Center, Palace, Junkyard, Pod Racing Track and Mining Outpost.
# For each of these places, the government keeps a record of all people coming and leaving, 
# called security_log.txt. A typical entry looks like this:
# Place: Factory
# [...]
# 11:44
# in: James Sasaki, Maria Sosa, Theresa Gil, Yanyan Walker
# out: Ester Ning
# This means that at 11:44, four people arrived at the factory and one person left.
# All entries refer to last monday. Times are noted in 24-hour-hh:mm-format, ranging from 00:00 to 23:59.
# During the escape, Jelly Jones lost his fitness tracker. Most of its memory is destroyed, but you manage 
# to recover the places he visited on Monday. They are (in this order):
# Junkyard
# Pod Racing Track
# Pod Racing Track
# Palace
# Factory
# Download this sequence as place_sequence.txt.
# Identify all people that visited these places in this order (and no other places).
# Solution code: the sum of the IDs of all people in question.
import collections
import pandas as pd
securityLog = open('security_log.txt').read()
securitySplit = securityLog.split("Place: ")[1:]
print(securitySplit[1])
listRooms = [securitySplit[i].split('\n\n') for i in range(len(securitySplit))]
listPlaces = []
listHours = []
listIns = []
listOuts = []
for i in range(len(listRooms)):
    for j in range(len(listRooms[i])-2):
        listPlaces.append(listRooms[i][0])
        listHours.append(str(listRooms[i][j+1]).split('\n')[0])
        inOutSplit = str(listRooms[i][j+1]).split('\n')
        if(len(inOutSplit) == 2):
            if('in' in inOutSplit[1].split(': ')[0]):
                listIns.append(inOutSplit[1].split(': ')[1])
                listOuts.append('NaN')
            elif('out' in inOutSplit[1].split(': ')[0]):
                listIns.append('NaN')
                listOuts.append(inOutSplit[1].split(': ')[1])
            else:
                listIns.append('NaN')
                listOuts.append('NaN')
        elif(len(inOutSplit) == 3):
            listIns.append(inOutSplit[1].split(': ')[1])
            listOuts.append(inOutSplit[2].split(': ')[1])

## make DataFrame
securityDf = pd.DataFrame({
    'Room':listPlaces,
    'Hours':listHours,
    'PeopleIn':listIns,
    'PeopleOut':listOuts
})
print(securityDf)

## read Sequence
sequenceDf = pd.read_csv('place_sequence.txt', skiprows=0, names=['Sequence'])
print(sequenceDf)
sequenceList = [seq for seq in sequenceDf['Sequence']]

## Find place sequence for every person
namesList = []
for i in range(len(sequenceList)):
    for j in range(len(securityDf)):  
        namesInSplit = securityDf['PeopleIn'][j].split(', ') 
        namesOutSplit = securityDf['PeopleOut'][j].split(', ')
        if securityDf['Room'][j] in sequenceList[i]:
            for name in namesInSplit:
                if 'NaN' not in name:
                    namesList.append(name)  
            for name in namesOutSplit:
                if 'NaN' not in name:
                    namesList.append(name)
for j in range(len(securityDf)): 
    namesInSplit = securityDf['PeopleIn'][j].split(', ') 
    namesOutSplit = securityDf['PeopleOut'][j].split(', ')
    if securityDf['Room'][j] not in sequenceList:
        for name in namesInSplit:
            if name in namesList:
                namesList = list(filter((name).__ne__,namesList))
        for name in namesOutSplit:
            if name in namesList:
                namesList = list(filter((name).__ne__,namesList))
print(namesList, len(namesList))

## filter duplicates
names = [item for item, count in collections.Counter(namesList).items() if count > 1]
print(names, len(names))

## Read population processed
populationDf = pd.read_csv('population_processed.txt',skiprows=0)
print(populationDf['Name'])
## calculate sum
sum = 0
for i in range(len(populationDf)):
    for name in names:
        if name in populationDf['Name'][i]:
            sum = sum + int(populationDf['ID'][i])

print('The sum of the IDs of all people with sequence: ',sum) 

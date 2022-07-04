# 1.1 Pico-Bots, Generation 1
# Robots have become smaller and smaller. The smallest ones, called pico-bots, are used as body enhancements: 
# they are injected into a persons blood circuit to fight off diseases and to increase the oxygen transport.
# Under the current galactic law, the injection of pico-bots is illegal.
# You have obtained a complete database of the inhabitants of the galaxy, see population.txt on the left. 
# In this register, you also find a blood sample of each person.
# Under the microscope, a blood sample is represented as a matrix of characters. 
# Beside empty space (denoted by a space character), there are four different types of cells
# represented by the characters p, i, c and o. Here is an example:
# +--------+
# | o  o pc|
# |   c ii |
# |p   oic |
# |ccp  ooc|
# |p o    c|
# | ocip   |
# +--------+    
# The first generation of pico-bots consists of the cells pico, in a straight line, in this order.
#  A pico-bot can lie in a blood sample horizontally or vertically in any of the four directions (up, down, left, right):
#  o  pico   p 
#  c         i 
#  i   ocip  c 
#  p         o    
# Example: The following blood sample has one of these bots in the second-to-last column, from bottom up.
#   oo
# p cc
# c i 
# pppc
# A friend from the galactic bio-lab has sent you two sets of blood samples. 
# You can download them on the left. lab_blood_clean.txt contains 25 blood 
# samples without pico-bots and lab_blood_gen1.txt contains 25 blood samples with pico-bots of generation 1. 
# These files are for debugging and testing purposes. For the solution of the puzzles, they are not needed.
# The security guards have told you that Jelly Jones moved at super-human speed, a typical effect of injecting pico-bots of generation 1.
#  Identify all blood samples (in the population register) that contain one or more pico-bots of generation 1.
# Solution code: the sum of the IDs of all people in question.
import collections
from statistics import mean
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sqlalchemy import column
from sympy import Plane, Point, Point3D

## Open file
population = open('population.txt').read()
populationSplit = population.split("\n\n")
print(populationSplit[0]) 

## Procesing of data
populationNameList = []
populationIDList = []
populationHomePlanetList = []
populationBloodSampleList = []
print(len(populationSplit))
for i in range(len(populationSplit)-1):
    plist = populationSplit[i].lstrip().split("\n")
    plist[3:15]=[''.join(plist[3:15])]
    populationNameList.append(plist[0].split(":")[1])
    populationIDList.append(plist[1].split(":")[1])
    populationHomePlanetList.append(plist[2].split(":")[1])
    populationBloodSampleList.append(plist[3].split(":")[1])
print(populationNameList[0]) 

## Make DataFrame
populationDf = pd.DataFrame(
    {'Name': populationNameList, 
    'ID': populationIDList, 
    'HomePlanet': populationHomePlanetList, 
    'BloodSample': populationBloodSampleList})
print(populationDf['BloodSample'][12731]) 

## Find pico in Blood Sample
sampleColumns = [str]
idList = []
for i in range(len(populationDf)):
    sampleRows = str(populationDf['BloodSample'][i]).replace('  +--------+  |','').replace('|  +--------+','').split('|  |')
    # if i == 0: print(populationDf['BloodSample'][i], sampleRows)
    sampleColumns.clear()
    for j in range(len(sampleRows[0])):
        sample = ''
        for k in range(len(sampleRows)):
            sample = sample + sampleRows[k][j]
        sampleColumns.append(sample)
        # if j == 0: print(sampleColumns)
    counted = False
    for l in sampleRows:
        if 'pico' in l:
            idList.append(int(populationDf['ID'][i]))
            counted = True
            break
        elif 'ocip' in l:
            idList.append(int(populationDf['ID'][i]))
            counted = True
            break
    if(not counted):
        for m in sampleColumns:
            if 'pico' in m:
                idList.append(int(populationDf['ID'][i]))
                break
            elif 'ocip' in m:
                idList.append(int(populationDf['ID'][i]))
                break
sum = 0
for i in range(len(idList)):
    sum = sum + idList[i]
print('The sum of the IDs of all people with pico: ',sum) 

## find duplicates
print([item for item, count in collections.Counter(idList).items() if count > 1])

# 1.2 Two-Dimensional Galaxy
# In our (fictitous) universe, a galaxy is an almost two-dimensional object. 
# While, in two of its dimensions, planets are spread out very far, in its third dimension, 
# a galaxy is very flat. If we place a two-dimensional plane into the galaxy, then the distance 
# of each planet from this plane is smaller than 2 galactic units (galactic units are length units in our fictitous universe).
# However, not all planets follow this rule. There is a special type of planet, called outlier planet. 
# These planets have a significantly larger distance from the galaxy's plane: they are at least 10 galactic units away from the plane.
# You are given the coordinates of all planets in the galaxy (given as (x,y,z) in galactic units) in
#  file galaxy_map.txt. Unfortunately, due to historic reasons, the universes coordinate system is not aligned with the galaxy's plane.
# Jelly Jones' shoulder tattoo says "We are Outliers! We don't fit!". The space pirate must be living on one of the outlier planets. 
# First, identify all outlier planets (in galaxy_map.txt) and then find all inhabitants that have an outlier planet as their home planet (in population.txt).
# Solution code: the sum of the IDs of all people in question.
def CalculateDistance(point, planePoint, normalVector = np.array([1,1,1])):
    # a plane is a*x+b*y+c*z+d=0
    # [a,b,c] is the normal. Thus, we have to calculate
    # d and we're set
    d = -np.dot(planePoint,normalVector) #
    distance = abs(np.dot(point, normalVector) + d)/math.sqrt(normalVector[0]**2 + normalVector[1]**2 + normalVector[2]**2)
    return distance

galaxiMap = open('galaxy_map.txt')

listPlanetCoord = []
for line in galaxiMap:
    listPlanetCoord.append(line.rstrip().replace(' ','').split(':'))
print(listPlanetCoord[0])
listPlanetNames = []
listXCoord = []
listYCoord = []
listZCoord = []
for coord in listPlanetCoord:
    x,y,z = (str(coord[1]).replace('(','').replace(')','').split(','))
    listPlanetNames.append(coord[0])
    listXCoord.append(float(x))
    listYCoord.append(float(y))
    listZCoord.append(float(z))
print(listXCoord[0], listYCoord[0], listZCoord[0])

## make galaxy dataframe 
galaxyDf = pd.DataFrame({'PlanetName': listPlanetNames, 
    'x': listXCoord, 
    'y': listYCoord, 
    'z': listZCoord})
print(galaxyDf)

# define the plane with point and normal vector
# pointPlane  = np.array([20, 40, 70])
# normaVector = np.array([-10, -20, -50])
plane = Plane(Point3D(25, 35, 65), Point3D(40, 30, 50), Point3D(20, 20, 20))
# print(pointPlane)
## calculate distance from plane
# outlierPlanetList = []
# for i in range(len(galaxyDf)):
#     point = Point(galaxyDf['x'][i],galaxyDf['y'][i],galaxyDf['z'][i])
#     # distance = CalculateDistance(point,pointPlane, normaVector) 
#     distance = float(point.distance(plane))
#     if distance >= 10:
#         # print('calculated distance : ',distance)
#         outlierPlanetList.append(galaxyDf['PlanetName'][i])
# # print(outlierPlanetList)

## find outleirs
# sum = 0
# for i in range(len(populationDf)):
#     for j in range(len(outlierPlanetList)):
#         if populationDf['HomePlanet'][i].replace(' ','') == outlierPlanetList[j]:
#             sum = sum + int(populationDf['ID'][i])
# print('The sum of the IDs of all people with outlier planet: ',sum) 

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

securityDf = pd.DataFrame({
    'Room':listPlaces,
    'Hours':listHours,
    'PeopleIn':listIns,
    'PeopleOut':listOuts
})
print(securityDf)

## Sequence
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

## calculate sum
sum = 0
for i in range(len(populationDf)):
    for name in names:
        if name in populationDf['Name'][i]:
            sum = sum + int(populationDf['ID'][i])

print('The sum of the IDs of all people with sequence: ',sum) 

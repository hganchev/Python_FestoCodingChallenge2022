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
from sympy import Plane, Point, Point3D
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
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
outlierPlanetList = []
for i in range(len(galaxyDf)):
    point = Point(galaxyDf['x'][i],galaxyDf['y'][i],galaxyDf['z'][i])
    # distance = CalculateDistance(point,pointPlane, normaVector) 
    distance = float(point.distance(plane))
    if distance >= 10:
        # print('calculated distance : ',distance)
        outlierPlanetList.append(galaxyDf['PlanetName'][i])
# print(outlierPlanetList)

## Read population processed
populationDf = pd.read_csv('population_processed.txt',skiprows=0)
print(populationDf['Name'])

## find outleirs
sum = 0
for i in range(len(populationDf)):
    for j in range(len(outlierPlanetList)):
        if populationDf['HomePlanet'][i].replace(' ','') == outlierPlanetList[j]:
            sum = sum + int(populationDf['ID'][i])
print('The sum of the IDs of all people with outlier planet: ',sum) 

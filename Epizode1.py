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
import pandas as pd
## Procesing of data
population = open('population.txt').read()
populationSplit = population.split("\n\n")
print(populationSplit[0])

populationList = []
populationNameList = []
populationIDList = []
populationHomePlanetList = []
populationBloodSampleList = []
for i in range(len(populationSplit)-1):
    plist = populationSplit[i].replace(' ','').lstrip().split("\n")
    plist[3:15]=[''.join(plist[3:15])]
    populationList.append(plist)
    populationNameList.append(plist[0].split(":")[1])
    populationIDList.append(plist[1].split(":")[1])
    populationHomePlanetList.append(plist[2].split(":")[1])
    populationBloodSampleList.append(plist[3].split(":")[1])
# print(populationNameList)
## Make DataFrame
populationDf = pd.DataFrame(
    {'Name': populationNameList, 
    'ID': populationIDList, 
    'HomePlanet': populationHomePlanetList, 
    'BloodSample': populationBloodSampleList})
print(populationDf['BloodSample'][0])
import pandas as pd


# samplesFile = open('lab_blood_clean.txt').read()
samplesFile = open('lab_blood_gen1.txt').read()
samplesSplit = samplesFile.split("\n\n")
print(samplesSplit[0]) 
samplesList = []
numberList = []
for i in range(len(samplesSplit)-1):
    sample = samplesSplit[i].split(".\n")
    samplesList.append(sample[1].replace('\n',''))
    numberList.append(sample[0].lstrip())
print(samplesList[0])

sampleDf = pd.DataFrame({
    'SampleNumber': numberList,
    'BloodSample': samplesList
})

print(sampleDf)
sampleColumns = []
for i in range(len(sampleDf)):
    sampleRows = str(sampleDf['BloodSample'][i]).replace('  +--------+  |','').replace('|  +--------+','').split('|  |')
    sampleColumns.clear()
    for j in range(len(sampleRows[0])):
        sample = ''
        for k in range(len(sampleRows)):
            sample = sample + sampleRows[k][j]
        sampleColumns.append(sample)
    counted = False
    for l in sampleRows:
        if 'pico' in l:
            counted = True
            print(sampleDf['SampleNumber'][i])
            break
        elif 'ocip' in l:
            counted = True
            print(sampleDf['SampleNumber'][i])
            break
    if(not counted):
        for m in sampleColumns:
            if 'pico' in m:
                print(sampleDf['SampleNumber'][i])
                break
            elif 'ocip' in m:
                print(sampleDf['SampleNumber'][i])
                break
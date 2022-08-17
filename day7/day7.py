import numpy as np
test = False

if test == True:
    with open('input7_test.txt') as f:
        lines = f.read().split('\n')
else:
    with open('input7.txt') as f:
        lines = f.read().split('\n')

pos = list(map(int,lines[0].split(',')))
sortedPos = sorted(pos)

med = int((sortedPos[int(len(sortedPos)/2)]+sortedPos[int((len(sortedPos)/2)-1)]) / 2)
totalDist = 0
for i in sortedPos:
    totalDist += abs(i-med)

#print(totalDist)


def findFuel(distance):
    return ((distance*distance)+distance) / 2

def findTotalFuel(distPos):
    totalFuel = 0
    for i in sortedPos:
        totalFuel += findFuel(abs(i-distPos))
        #print(i)
        #print(findFuel(abs(i-sortedPos[ind])))
    return totalFuel



fuels = []
for n in range(min(sortedPos),max(sortedPos),1):
    fuels.append(findTotalFuel(n))

print(sorted(fuels)[0])
    



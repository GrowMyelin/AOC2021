import numpy as np

with open('input5.txt') as f:
    lines = f.read().split('\n')

arr = np.zeros((1000,1000))
mx = 0
mn = 100
for ln in lines[:-1]:
    print(ln)
    splitLine = ln.split(' -> ')
    startX = int(splitLine[0].split(',')[0])
    startY = int(splitLine[0].split(',')[1])
    endX = int(splitLine[1].split(',')[0])
    endY = int(splitLine[1].split(',')[1])
    if startX == endX:
        #vertical line
        for y in range(min(startY,endY),max(startY,endY),1):
            arr[startX][y] += 1
    elif startY == endY:
        #horizontal line
        for x in range(min(startX,endX),max(startX,endX),1):
            #print(x)
            arr[x][startY] += 1
    mx = max(mx,startX,startY,endX,endY)
    mn = min(mn,startX,startY,endX,endY)

print(arr[905][85])
print(np.sum(arr > 1))

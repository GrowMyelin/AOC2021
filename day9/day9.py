import numpy as np
with open('input9.txt') as f:
    lines = f.read().split('\n')

print(lines)
board = np.zeros([len(lines),len(lines[0])])

for i,line in enumerate(lines):
    board[i]=list(lines[i])

print(board)
testBoard = board

def checkAdjacent(i,j):
    elevation = 0
    try:
        if board[i,j] >= board[i+1,j]:
            elevation += 1
    except:
        pass
    try:
        if board[i,j] >= board[i-1,j]:
            elevation += 1
    except:
        pass
    try:
        if board[i,j] >= board[i,j+1]:
            elevation += 1
    except:
        pass
    try:
        if board[i,j] >= board[i,j-1]:
            elevation += 1
    except:
        pass
    
    if elevation > 0:
        return False
    else:
        return True

mins = []
blanks = []
minSum = 0
for i,row in enumerate(board):
    for j,val in enumerate(row):
        if checkAdjacent(i,j):
            mins.append((i,j))
            minSum += (board[i][j])+1
            print((i,j))
        elif board[i,j]==9:
            pass
        else:
            blanks.append((i,j))

print(minSum)

def addToBasin(i,j):
    # input point (i,j)
    # output all points inside basin adjacent to input
    newBasin = [(i,j)]
    try:
        if board[i,j+1] < 9:
            newBasin.append((i,j+1))
    except:
        pass
    try:
        if board[i,j-1] < 9 and (j-1 >= 0):
            newBasin.append((i,j-1))
    except:
        pass
    try:
        if board[i+1,j] < 9:
            newBasin.append((i+1,j))
    except:
        pass
    try:
        if board[i-1,j] < 9 and (i-1 >= 0):
            newBasin.append((i-1,j))
    except:
        pass
    return newBasin

testMin = (99,99)

# Basin : check around each low point for 9's include everything that isn't a 9

def findBasins(i,j,currentBasin):
    # input min (i,j,currentBasin)
    for basinPoints in currentBasin:
        newBasin = addToBasin(basinPoints[0],basinPoints[1])
        for newPoint in newBasin:
            if newPoint not in currentBasin:
                currentBasin.append(newPoint)
    return currentBasin

allBasins = []
for m in mins:
    allBasins.append(findBasins(m[0],m[1],[(m[0],m[1])]))
lengths = []
for basins in allBasins:
    lengths.append(len(basins))

ans = sorted(lengths)
#print(ans[-1]*ans[-2]*ans[-3])

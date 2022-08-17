# Advent of Code 2021 - Day 4
import itertools
import numpy as np

with open('input4.txt') as f:
    lines = f.read().split('\n')


inputNums = lines[0].split(',')

boards = [list(y) for x,y in itertools.groupby(lines[1:],lambda z: z=='') if not x]


boardDict = dict()
for n,i in enumerate(boards):
    l = [[],[]]
    for j in i:
        testList = j.split(' ')
        testList = [i for i in testList if i]
        l[0].append(testList)
        l[1].append([0]*5)
    boardDict[n] = l

'''
def checkBoard(boardNum):
    current = boardDict[boardNum][1]
    for row in range(len(current)):
            
    for col in range(len(current)):
'''
winCon = False
i = 0
while winCon == False:
    inp = inputNums[i]
    #print(i)
    for j in range(len(boards)):
        currentBoard = boardDict[j][0]
        #print(currentBoard)
        for row in range(len(currentBoard)):
            for col in range(len(currentBoard[0])):
                if currentBoard[row][col] == inp:
                    boardDict[j][1][row][col] = 1

    
        for row1 in range(len(currentBoard)):
            if boardDict[j][1][row1] == [1]*5:
                print(j)
                print(inputNums[i])
                winner = j
                winCon = True

    if i < len(inputNums)-1:
        #print(inp)
        #print(boardDict[1][1])
        i += 1
    else:
        print('WRONG')

sumNum = 0
for row in range(len(boardDict[winner][1])):
    for col in range(len(boardDict[winner][1][0])):
        if boardDict[winner][1][row][col] == 0:
            sumNum += int(boardDict[winner][0][row][col])

print(finalNum * sumNum)

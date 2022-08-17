import numpy as np
with open('input9_test.txt') as f:
    lines = f.read().split('\n')

board = np.zeros([len(lines),len(lines[0])])

for i,line in enumerate(lines):
    board[i]=list(lines[i])

print(board)

def checkMins(row,col):
    elevation = 0
    try:
        if board[row+1][col] <= board[row][col]:
            elevation += 1

        if board[row-1][col] <= board[row][col]:
            elevation += 1

        if board[row][col+1] <= board[row][col]:
            elevation += 1

        if board[row][col-1] <= board[row][col]:
            elevation += 1
    except:
        pass
    if elevation > 0:
        return False
    else:
        return True

r = 0
for i in range(len(board)):
    for j in range(len(board[0])):
        if checkMins(i,j):
            print(i,j)
            r += (1+board[i][j])

print(r)
print(checkMins(0,4))
print(board[(0,4)])
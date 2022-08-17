import numpy as np
test = True

if test == True:
    with open('input10_test.txt') as f:
        lines = f.read().split('\n')
else:
    with open('input10.txt') as f:
        lines = f.read().split('\n')


print(lines)
def checkLine(ln)
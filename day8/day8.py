import numpy as np
test = True

if test == True:
    with open('input8_test.txt') as f:
        lines = f.read().split('\n')
else:
    with open('input8.txt') as f:
        lines = f.read().split('\n')

out = []
for ln in lines[:-1]:
    out.append(ln.split(' | ')[1])


outs = []
for o in out:
    outs.append(o.split(' '))


lengths = [6,2,5,5,4,5,6,3,7,6] # [0,1,2,3,...,9]


'''
Pt1 solution
count = 0
for o in outs:
    for i in o:
        if len(i) in lengths:
            count += 1

print(count)
'''
# Advent of Code Day 2

with open('input2.txt') as f:
    lines = f.read().split('\n')


vertical = 0
horizontal = 0
aim = 0
for line in lines[:-1]:
    splitLine = line.split(' ')

    if splitLine[0] == 'forward':
        horizontal += int(splitLine[1])
        vertical += (aim*int(splitLine[1]))
    elif splitLine[0] == 'up':
        aim -= int(splitLine[1])
    elif splitLine[0] == 'down':
        aim += int(splitLine[1])

print(horizontal*vertical)

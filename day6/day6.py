with open('input6.txt') as f:
    lines = f.read().split('\n')

lanternFish = list(map(int,lines[0].split(',')))
fishCount = 9*[0]
for n in range(len(fishCount))
    for fish in lanternFish:
        if fish==n:
            fishCount[n]+=1

def passDay(fishArr):
    newCount = fishArr[0]
    for n in range(len(fishArr)-1):
        fishArr[n]=fishArr[n+1]
    fishArr[6] += newCount
    fishArr[8] = newCount
    return fishArr


'''
def passDay(fishArr):
    newCount = 0
    for n,fish in enumerate(fishArr):
        if fish > 0:
            fishArr[n] -= 1
        else:
            newCount += 1
            fishArr[n] = 6
    for i in range(newCount):
        fishArr.append(8)
    return fishArr
'''
def passDays(n):
    finalArr = fishCount
    for x in range(n):
        finalArr = passDay(finalArr)

    return sum(finalArr)

print(passDays(256))

# Advent of Code 2021 - Day 3
with open('input3.txt') as f:
    lines = f.read().split('\n')

counts,gamma,epsilon = [0]*len(lines[0]),[0]*len(lines[0]),[0]*len(lines[0])
for line in lines[:-1]:
    for n,num in enumerate(line):
        counts[n] += int(num)

for n,digits in enumerate(counts):
    if digits > 500:
        gamma[n] = 1
        epsilon[n] = 0
    else:
        gamma[n] = 0
        epsilon[n] = 1


def binaryToDecimal(arr):
    decimal = 0
    for n,digit in enumerate(arr):
        if digit != 0:
            decimal += pow(2,len(arr)-n-1)

    return decimal
# pt 1 answer
print(binaryToDecimal(gamma)*binaryToDecimal(epsilon))


# pt 2 solution

def bitCriteria(arr,idx,isGamma):
    nums = []
    if isGamma:
        for num in arr:
            if list(map(int,str(num)))[idx]==gamma[idx]:
                nums.append(num)
    else:
        for num in arr:
            if list(map(int,str(num)))[idx]==epsilon[idx]:
                nums.append(num)
    return nums

curNums = list(map(int,lines[:-1]))


while(len(curNums)>1 or i==len(lines[0])):
    i = 0
    curNums = bitCriteria(curNums,i,True)
    i += 1

print(curNums)

    

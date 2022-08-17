# Advent of Code Day 1

with open('input1.txt') as f:
    lines = f.read().split('\n')

def slidingWindow(n):
    return nums[n]+nums[n+1]+nums[n+2]

nums = list(map(int,lines[:-1]))
print(lines)
count = 0
count2 = 0
for n,line in enumerate(nums):
    if nums[n] > nums[n-1]:
        count += 1

for n,line in enumerate(nums[:-2]):
    if slidingWindow(n) > slidingWindow(n-1):
        count2 += 1
        
print(count2)


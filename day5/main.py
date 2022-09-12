

import numpy as np

def main(test):
    count = 0
    arr = np.zeros((1000,1000))
    if test:
        with open('testInput.txt') as f:
            lines = f.read().split('\n')
    else:
        with open('input.txt') as f:
            lines = f.read().split('\n')[:-1]

    for ln in lines:
        coords = ln.split(' -> ')
        x1 = int(coords[0].split(',')[0])
        y1 = int(coords[0].split(',')[1])
        x2 = int(coords[1].split(',')[0])
        y2 = int(coords[1].split(',')[1])
        if x1 == x2:
            for y in range(min(y1,y2),max(y1,y2)+1):
                arr[y][x1] += 1
        elif y1 == y2:
            for x in range(min(x1,x2),max(x1,x2)+1):
                arr[y1][x] += 1
        else:
            minx = min(x1,x2)
            maxx = max(x1,x2)
            miny = min(y1,y2)
            maxy = max(y1,y2)
            if x1 < x2 and y1 < y2:
                while minx <= maxx:
                    arr[miny][minx] += 1
                    minx += 1
                    miny += 1
            elif x1 < x2 and y1 > y2:
                while minx <= maxx:
                    arr[maxy][minx] += 1
                    minx += 1
                    maxy -= 1
            elif x1 > x2 and y1 < y2:
                while miny <= maxy:
                    arr[miny][maxx] += 1
                    miny += 1
                    maxx -= 1
            elif x1 > x2 and y1 > y2:
                while minx <= maxx:
                    arr[maxy][maxx] += 1
                    maxx -= 1
                    maxy -= 1
        
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if arr[y][x] > 1:
                count += 1
    print(count)



if __name__ == "__main__":
    main(False)
import numpy as np
import copy 
from collections import defaultdict

def xlevel():
    return defaultdict(lambda: '.')

def ylevel():
    return defaultdict(xlevel)

def zlevel():
    return defaultdict(ylevel)

def fourdim():
    return defaultdict(zlevel)


# x y z represent the coordinate to find neighbours to
def neighbourscube(cube, xcoord, ycoord, zcoord):
    out = []
    for z in range(zcoord-1, zcoord + 2):
        plane = []
        for y in range(ycoord-1, ycoord + 2):
            row = []
            for x in range(xcoord-1, xcoord + 2):
                if any([x != xcoord, y != ycoord, z != zcoord]):
                    row.append(cube[z][y][x])
            out += row
    return out

# x y z represent the coordinate to find neighbours to
def neighbours4dim(pocketdim, xcoord, ycoord, zcoord, wcoord):
    out = []
    for w in range(wcoord-1, wcoord + 2):
        cube = []
        for z in range(zcoord-1, zcoord + 2):
            plane = []
            for y in range(ycoord-1, ycoord + 2):
                row = []
                for x in range(xcoord-1, xcoord + 2):
                    if any([x != xcoord, y != ycoord, z != zcoord, w != wcoord] ):
                        #print(f"{x=},{y=},{z=},{w=}, {cube=}")
                        row.append(pocketdim[w][z][y][x])
                out += row
    return out

def solution1(data):
    cube = zlevel()
    for yindex,yval in enumerate(data):
        for xindex, xval in enumerate(yval):
            cube[0][yindex][xindex] = xval

    previousCube = copy.deepcopy(cube)
    newCube = zlevel()
    dimZ = (min(cube.keys())-1,max(cube.keys())+2)
    dimY = (min(cube[0].keys())-1,max(cube[0].keys())+2)
    dimX = (min(cube[0][0].keys())-1,max(cube[0][0].keys())+2)
    for i in range(6):
        #print(f"{dimX=}, {dimY=}, {dimZ=}")
        newdimX = [None, None]
        newdimY = [None, None]
        newdimZ = [None, None]
        active = 0
        for zindex in list(range(*dimZ)):
            for yindex in list(range(*dimY)):
                for xindex in list(range(*dimX)):
                    neighbours = neighbourscube(previousCube, xindex, yindex, zindex)
                    if previousCube[zindex][yindex][xindex] == "#"                         and neighbours.count("#") == 2:
                            newCube[zindex][yindex][xindex] = "#"
                    elif neighbours.count("#") == 3:
                            newCube[zindex][yindex][xindex] = "#"
                    else:
                            newCube[zindex][yindex][xindex] = "."
                    if newCube[zindex][yindex][xindex] == "#":
                        #print(f"{xindex=}, {yindex=}, {zindex=}")
                        active += 1
                        newdimX[0] = xindex if newdimX[0] is None or newdimX[0] > xindex else newdimX[0]
                        newdimX[1] = xindex if newdimX[1] is None or newdimX[1] < xindex else newdimX[1]
                        newdimY[0] = yindex if newdimY[0] is None or newdimY[0] > yindex else newdimY[0]
                        newdimY[1] = yindex if newdimY[1] is None or newdimY[1] < yindex else newdimY[1]
                        newdimZ[0] = zindex if newdimZ[0] is None or newdimZ[0] > zindex else newdimZ[0]
                        newdimZ[1] = zindex if newdimZ[1] is None or newdimZ[1] < zindex else newdimZ[1]
        #print(found)
        #print(visited)
        newdimX[1] += 1
        newdimY[1] += 1
        newdimZ[1] += 1
        #print(f"{newdimX=}, {newdimY=}, {newdimZ=}")
        for zindex in list(range(*newdimZ)):
            #print(f"zindex = {zindex}")
            for yindex in list(range(*newdimY)):
                xstring = ""
                for xindex in list(range(*newdimX)):
                    xstring += newCube[zindex][yindex][xindex]
                #print(f"{yindex}: {xstring}")
            #print("")
        newdimX[0] -= 1
        newdimY[0] -= 1
        newdimZ[0] -= 1
        newdimX[1] += 1
        newdimY[1] += 1
        newdimZ[1] += 1
        dimZ = (newdimZ[0],newdimZ[1])
        dimY = (newdimY[0],newdimY[1])
        dimX = (newdimX[0],newdimX[1])
        previousCube = copy.deepcopy(newCube)
        newCube = zlevel()
    return active


def solution2(data):
    pocketdim = fourdim()
    newdimX = [None, None]
    newdimY = [None, None]
    newdimZ = [0, 0]
    newdimW = [0, 0]
    for yindex,yval in enumerate(data):
        for xindex, xval in enumerate(yval):
            pocketdim[0][0][yindex][xindex] = xval
            newdimX[0] = xindex if newdimX[0] is None or newdimX[0] > xindex else newdimX[0]
            newdimX[1] = xindex if newdimX[1] is None or newdimX[1] < xindex else newdimX[1]
            newdimY[0] = yindex if newdimY[0] is None or newdimY[0] > yindex else newdimY[0]
            newdimY[1] = yindex if newdimY[1] is None or newdimY[1] < yindex else newdimY[1]

    previousCube = copy.deepcopy(pocketdim)
    newCube = fourdim()
    for i in range(6):
        #print(f"{dimX=}, {dimY=}, {dimZ=}")
        newdimX[0] -= 1
        newdimY[0] -= 1
        newdimZ[0] -= 1
        newdimW[0] -= 1
        newdimX[1] += 2
        newdimY[1] += 2
        newdimZ[1] += 2
        newdimW[1] += 2
        dimW = (newdimW[0],newdimW[1])
        dimZ = (newdimZ[0],newdimZ[1])
        dimY = (newdimY[0],newdimY[1])
        dimX = (newdimX[0],newdimX[1])
        newdimX = [None, None]
        newdimY = [None, None]
        newdimZ = [None, None]
        newdimW = [None, None]
        active = 0
        for windex in list(range(*dimW)):
            for zindex in list(range(*dimZ)):
                for yindex in list(range(*dimY)):
                    for xindex in list(range(*dimX)):
                        neighbours = neighbours4dim(previousCube, xindex, yindex, zindex, windex)
                        if previousCube[windex][zindex][yindex][xindex] == "#"                             and neighbours.count("#") == 2:
                                newCube[windex][zindex][yindex][xindex] = "#"
                        elif neighbours.count("#") == 3:
                                newCube[windex][zindex][yindex][xindex] = "#"
                        else:
                                newCube[windex][zindex][yindex][xindex] = "."
                        if newCube[windex][zindex][yindex][xindex] == "#":
                            #print(f"{xindex=}, {yindex=}, {zindex=}")
                            active += 1
                            newdimX[0] = xindex if newdimX[0] is None or newdimX[0] > xindex else newdimX[0]
                            newdimX[1] = xindex if newdimX[1] is None or newdimX[1] < xindex else newdimX[1]
                            newdimY[0] = yindex if newdimY[0] is None or newdimY[0] > yindex else newdimY[0]
                            newdimY[1] = yindex if newdimY[1] is None or newdimY[1] < yindex else newdimY[1]
                            newdimZ[0] = zindex if newdimZ[0] is None or newdimZ[0] > zindex else newdimZ[0]
                            newdimZ[1] = zindex if newdimZ[1] is None or newdimZ[1] < zindex else newdimZ[1]
                            newdimW[0] = windex if newdimW[0] is None or newdimW[0] > windex else newdimW[0]
                            newdimW[1] = windex if newdimW[1] is None or newdimW[1] < windex else newdimW[1]
        previousCube = copy.deepcopy(newCube)
        newCube = fourdim()
    return active

def main():
    data = open('testdata', 'r').readlines()
    data = np.char.strip(data).tolist()
    assert solution1(data) == 112, "test failed"
    assert solution2(data) == 848, "test failed"

    data = open('input', 'r').readlines()
    data = np.char.strip(data).tolist()

    return [solution1(data), solution2(data)]

if __name__ == "__main__":
    answers = main()
    print(f"Answer to question1: {answers[0]}")
    print(f"Answer to question2: {answers[1]}")
    
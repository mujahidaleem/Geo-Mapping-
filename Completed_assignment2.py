from typing import List

def get_average_elevation(m: List[List[int]]) -> float:
    """
    Returns the average elevation across the elevation map m.

    Examples
    >>> get_average_elevation([])
    0
    >>> m = [[1,2,3],[4,5,6],[7,8,9]]
    >>> get_average_elevation(m)
    5.0
    >>> m = [[1,2,2,5],[4,5,4,8],[7,9,9,1],[1,2,1,4]]  
    >>> get_average_elevation(m)
    4.0625
    """
    newlst = []
    for lst in m:
        for element in lst:
            newlst.append(element)
    if len(newlst) == 0:
        return 0
    else:
        return sum(newlst)/len(newlst)
    #Take all elements and add them to a counter and then divide them by the number of elements there are
    #Your code goes here
    

def find_peak(m: List[List[int]]) -> List[int]:
    """
    Given an non-empty elevation map m, returns the cell of the
    highest point in m.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,2,3],
             [9,8,7],
             [5,4,6]]
    >>> find_peak(m)
    [1,0]
    >>> m = [[6,2,3],
             [1,8,7],
             [5,4,9]]
    >>> find_peak(m)
    [2,2]
    """
    largest = 0
    lstresult = []
    for lst in m:
        for element in lst:
            if largest < float(element):
                largest = element
                largestposSub = m.index(lst)
                largestposSub2 = lst.index(largest)
    lstresult.append(largestposSub)
    lstresult.append(largestposSub2)
    return lstresult
    #Loop and set the highest element to the checker number, then if check if there is a larger number...
    #Your code goes here
    

def is_sink(m: List[List[int]], c: List[int]) -> bool:
    """
    Returns True if and only if c is a sink in m.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,2,3],
             [2,3,3],
             [5,4,3]]
    >>> is_sink(m, [0,0])
    True
    >>> is_sink(m, [2,2])
    True
    >>> is_sink(m, [3,0])
    False
    >>> m = [[1,2,3],
             [2,1,3],
             [5,4,3]]
    >>> is_sink(m, [1,1])
    True
    """
    X=len(m)-1
    Y=len(m)-1
    x = c[0]
    y = c[1]
    newlist = []
    #Adjacent addition/check
    for x2 in range(x-1,x+2):
        for y2 in range(y-1,y+2):
            if (-1 < x <= X and
                -1 < y <= Y and
                (x != x2 or y != y2) and
                (0 <= x2 <= X) and
                (0 <= y2 <= Y)):
                newlist.append(m[x2][y2])
    if newlist == []:
        return False
    return all(i >= m[c[0]][c[1]] for i in newlist)

    #sink iff the element sink is less than all the elements adjacent to it m[c] < m[adjacent]
    #Check for dimentions in m and c first
    #Check i
    #Check c in i
    #If c in i; True, else False
    #Your code goes here
    

def find_local_sink(m: List[List[int]], start: List[int]) -> List[int]:
    """
    Given a non-empty elevation map, m, starting at start,
    will return a local sink in m by following the path of lowest
    adjacent elevation.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[ 5,70,71,80],
             [50, 4,30,90],
             [60, 3,35,95],
             [10,72, 2, 1]]
    >>> find_local_sink(m, [0,0])
    [3,3]
    >>> m = [[ 5,70,71,80],
             [50, 4, 5,90],
             [60, 3,35, 2],
             [ 1,72, 6, 3]]
    >>> find_local_sink(m, [0,3])
    [2,3]
    >>> m = [[9,2,3],
             [6,1,7],
             [5,4,8]]
    >>> find_local_sink(m, [1,1])
    [1,1]
    """
    X=len(m)-1
    Y=len(m)-1
    endposX = start[0]
    endposY = start[1]
    finalPosition = []
    
    while True:
        x = endposX
        y = endposY
        lowest = m[x][y]
        #Adjacent addition/check
        for x2 in range(x-1,x+2):
            lst = []
            for y2 in range(y-1,y+2):
                if (-1 < x <= X and
                    -1 < y <= Y and
                    (x != x2 or y != y2) and
                    (0 <= x2 <= X) and
                    (0 <= y2 <= Y)):
                        if m[x2][y2] < m[endposX][endposY]:
                            lst.append(m[x2][y2])
                        if lowest > m[x2][y2]:
                            lowest = m[x2][y2]
                            endposX = x2 
                            endposY = y2                      
        if lst == []: 
            finalPosition.append(endposX)
            finalPosition.append(endposY)
            return finalPosition
        

    
def can_hike_to(m: List[List[int]], s: List[int], d: List[int], supplies: int) -> bool:
    """
    Given an elevation map m, a start cell s, a destination cell d, and
    the an amount of supplies returns True if and only if a hiker could reach
    d from s using the strategy dscribed in the assignment .pdf. Read the .pdf
    carefully. Assume d is always south, east, or south-east of s. The hiker
    never travels, north, west, nor backtracks. 

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,4,3],
             [2,3,5],
             [5,4,3]]
    >>> can_hike_to(m, [0,0], [2,2], 4)
    True
    >>> can_hike_to(m, [0,0], [0,0], 0)
    True
    >>> can_hike_to(m, [0,0], [2,2], 3)
    False
    >>> m = [[1,  1,100],
             [1,100,100],
             [1,  1,  1]]
    >>> can_hike_to(m, [0,0], [2,2], 4)
    False
    >>> can_hike_to(m, [0,0], [2,2], 202)
    True
    """  
    X=len(m)-1
    Y=len(m)-1

    posX = s[0]
    posY = s[1]
    endposX = d[0]
    endposY = d[1]
    finalPosition = []
    while True:
        x = posX
        y = posY
        finalPosition = []
        #Indexcheccker
        #EAst
        if y+1 > Y:
            East = 0
        else:
            East = m[x][y+1]
        #South
        if x+1 > X:
            South = 0
        else:
            South = m[x+1][y]
                
        if East < South and East != 0 or South == 0:
            distance = (abs(East-m[posX][posY]))
            supplies = supplies - distance
            if supplies <= 0:
                if posX == endposX and posY == endposX:
                    return True
                else:
                    return False
            if posX == endposX and posY == endposX:
                return True
            posY = y+1
        elif South < East and South != 0 or East == 0 or South == East:
            distance = (abs(East-m[posX][posY]))
            supplies = supplies - distance
            if supplies <= 0:
                if posX == endposX and posY == endposX:
                    return True
                else:
                    return False
            if posX == endposX and posY == endposX:
                return True
            posX = x+1
                
        
            
    #Same concept but only limited to going down or right, 
    #Your code goes here


def rotate_map(n: List[List[int]]) -> None:
    """
    Rotates the orientation of an elevation map m 90 degrees counter-clockwise.
    See the examples to understand what's meant by rotate.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,2,3],
             [2,3,3],
             [5,4,3]]
    >>> rotate_map(m)
    >>> m
    [[3,3,3],
     [2,3,4],
     [1,2,5]]
    >>> m = [[5,9,1,8],
             [2,4,5,7],
             [6,3,3,2],
             [1,7,6,3]]
    >>> rotate_map(m)
    >>> m
    [[8,7,2,3],
     [1,5,3,6],
     [9,4,3,7],
     [5,2,6,1]]
    """
    rotate = [list(element) for element in zip(*(reversed(sublist) for sublist in n))]
    global m
    m = rotate
    #Your code goes here
    #Take last elements of a list to make a new list, etc


"""
You are not required to understand or use the code below. It is there for
curiosity and testing purposes.
"""
def create_real_map()-> List[List[int]]:
    """
    Creates and returns an elevation map from the real world data found
    in the file elevation_data.csv.

    Make sure this .py file and elevation_data.csv are in the same directory
    when you run this function to ensure it works properly.
    """
    data = open("elevation_data.csv")
    m = []
    for line in data:
        m.append(line.split(","))
    data.close()
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = int(m[i][j])
    return m
    
    










    

# Geo-Mapping-

Consider a section of the Earth’s surface from a birds-eye-view. The elevation may vary greatly
across this section. See the Figures below as an example. If one were interested in analysing this
area based on elevation, one could represent the section of Earth as a matrix of numerical values,
where each cell of the matrix would indicate the elevation of the Earth at that particular location.
For example, an area the size of 1 square kilometer of Earth could be encoded as a 1000x1000 matrix, where each cell is the elevation of a single square meter; here, the value at cell (500,500) of
the matrix, would be the elevation at approximately the middle of the original 1 square kilometer
section.


For this task, I implemented several functions that utilized matrices (with values) to preform meaningful anaylysis on the area of the Earth's surface - which the matrix represents.

The following functions were implemented:
1. get average elevation(List[List[int]]) -> float
The first parameter is an elevation map, m. Returns the average elevation across all the land
in m.

2. find peak(List[List[int]]) -> List[int]
The first parameter is an elevation map, m. Returns the cell which contains the highest
elevation point in m. For the purposes of us testing this function, you may assume that all
values of m are unique (no two locations have equal elevations).

3. is sink(List[List[int]], List[int]) -> bool
The first parameter is an elevation map, m, the second parameter is a cell, c. Returns True
if and only if c is a sink in m. Note if c does not exist in m (the values are outside m’s
dimensions), this function returns False. See the previous section for the definition of a sink.

4. find local sink(List[List[int]], List[int]) -> List[int]
The first parameter is an elevation map, m, the second parameter is a cell, c, which exists in m.
Returns the local sink of c. A local sink of c is the cell which water would flow to if it started
at c. Assume if the current location isn’t a sink, water will always flow to the adjacent cell
with the lowest elevation. You may also assume for the purposes of us testing this function,
that all values of m are unique (no two locations have equal elevations). See the docstring for
some examples.

5. can hike to(List[List[int]], List[int], List[int], int) -> bool
The first parameter is an elevation map, m, the second is start cell, s which exists in m, the
third is a destination cell, d, which exists in m, and the forth is the amount of available supplies.
Under the interpretation that the top of the elevation map is north, you may assume that d is
to the south-east of s (this means it could also be directly south, or directly east). The idea
2
is, if a hiker started at s with a given amount of supplies could they reach f if they used the
following strategy. The hiker looks at the cell directly to the south and the cell directly to the
east, and then travels to the cell with the lower change in elevation. They keep repeating this
stratagem until they reach d (return True) or they run out of supplies (return False). Assume
to move from one cell to another takes an amount of supplies equal to the change in elevation
between the cells. See the docstring for some examples. If the change in elevation is the same
between going East and going South, the hiker will always go East. Also, the hiker will never
choose to travel South, or East of d (they won’t overshoot their destination). That is, if d is
directly to the East of them, they will only travel East, and if d is directly South, they will
only travel South.

6. rotate map(List[List[int]]) -> None
The parameter is an elevation map, m. Under the interpretation that the top of m is north,
the function mutates m such that the top of m would now be viewed as east. See the docstring
for some examples.

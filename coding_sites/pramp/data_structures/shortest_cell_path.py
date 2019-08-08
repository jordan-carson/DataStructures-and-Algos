from collections import deque


def isValid(row, col, grid) -> bool:
    return (row >= 0) and (row < len(grid)) and (col >= 0) and (col < len(grid[0])) and (grid[row][col] == 1)


def shortestCellPath(grid, sr, sc, tr, tc):
    """
    @param grid: int[][]
    @param sr: int
    @param sc: int
    @param tr: int
    @param tc: int
    @return: int
    """
    # we will traverse using BFS
    # distance = 0
    queueNode = {(sr, sc), 0}
    q = deque()

    q.append(queueNode)

    visited = {(sr, sc): True}
    rowNum = [-1, 0, 0, 1]
    colNum = [0, -1, 1, 0]
    valid = zip(rowNum, colNum)

    while not len(q):

        # find the current node
        current = q.pop()
        x, y, distance = current[0], current[1]

        # have we reached the destination cell?
        if x == tr and y == tc:
            return distance

        for i in range(4):
            row = x + valid[i][0]
            col = y + valid[i][1]

            if isValid(row, col, grid) and grid[row][col] and not visited[row][col]:
                # mark the cells as visited and then add it to our queue
                visited[(row, col)] = True
                q.appendleft((row, col), distance + 1)

    return -1



grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr = 0
sc = 0
tr = 2
tc = 0
print()



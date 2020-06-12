# Find if the number already existed in the row
def findRow(table, n, index):
    for i in range(0, 9):
        if(table[index][i] == n):
            return True
    return False


# Find if the number already existed in the column
def findColumn(table, n, index):
    for i in range(0, 9):
        if(table[i][index] == n):
            return True
    return False


# Find if the number already existed in the box
def findBox(table, n, indexR, indexC):
    
    indexRow = 0
    indexColumn = 0
        
    if(indexR >= 0 and indexR <= 3 and indexC >= 0 and indexC <= 3):
        indexRow = 0
        indexColumn = 0
    if(indexR >= 3 and indexR <= 6 and indexC >= 0 and indexC <= 3):
        indexRow = 3
        indexColumn = 0
    if(indexR >= 6 and indexR <= 9 and indexC >= 0 and indexC <= 3):
        indexRow = 6
        indexColumn = 0
    if(indexR >= 0 and indexR <= 3 and indexC >= 3 and indexC <= 6):
        indexRow = 3
        indexColumn = 3
    if(indexR >= 3 and indexR <= 6 and indexC >= 3 and indexC <= 6):
        indexRow = 3
        indexColumn = 3
    if(indexR >= 6 and indexR <= 9 and indexC >= 3 and indexC <= 6):
        indexRow = 3
        indexColumn = 3
    if(indexR >= 0 and indexR <= 3 and indexC >= 6 and indexC <= 9):
        indexRow = 6
        indexColumn = 6
    if(indexR >= 3 and indexR <= 6 and indexC >= 6 and indexC <= 9):
        indexRow = 6
        indexColumn = 6
    if(indexR >= 6 and indexR <= 9 and indexC >= 6 and indexC <= 9):
        indexRow = 6
        indexColumn = 6
    
    for i in range(indexRow, indexRow+3):
        for j in range(indexColumn, indexColumn+3):
            if(table[i][j] == n):
                return True
    return False


def findAll(table, n, indexR, indexC):
    if (findRow(table, n, indexR) or findColumn(table, n, indexC) or findBox(table, n, indexR, indexC)):
        return True
    else:
        return False
    
###############################################################


def solver(t):
    row = 0
    col = 0
    while(row < 8 or col < 8):
        if(t[row][col] == 0):
            for i in range(1, 9):
                if not(findAll(t, i, row, col)):
                    t[row][col] = i
                    col += 1
                    if(col > 7):
                        col = 0
                        row += 1
                    if(row > 8):
                        return t
    
    
    return t

def solver2(t):
    r = 0
    c = 0
    def solve(t, row, col):
        while(row < 8 or col < 8):
            if(t[row][col] == 0):
                for i in range(1, 10):
                    if not(findAll(t, i, row, col)):
                        t[row][col] = i
                        if(col > 8):
                            return solve(t, row+1, 0)
                        else:
                            return solve(t, row, col+1)
        return t
    
    
    return solve(t, r, c)

def solver3(t):
    r = 0
    c = 0
    def solve(t, row, col):
        if(row >= 8 and col >= 8):
            return t
        
        if(t[row][col] == 0):
            for i in range(1, 10)
    
    
    return solve(t, r, c)

for i in range(1, 10):
    print(table1[8][8])



table1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]


result = solver2(table1)
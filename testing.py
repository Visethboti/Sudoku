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
        indexRow = 0
        indexColumn = 3
    if(indexR >= 3 and indexR <= 6 and indexC >= 3 and indexC <= 6):
        indexRow = 3
        indexColumn = 3
    if(indexR >= 6 and indexR <= 9 and indexC >= 3 and indexC <= 6):
        indexRow = 6
        indexColumn = 3
    if(indexR >= 0 and indexR <= 3 and indexC >= 6 and indexC <= 9):
        indexRow = 0
        indexColumn = 6
    if(indexR >= 3 and indexR <= 6 and indexC >= 6 and indexC <= 9):
        indexRow = 3
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

def solver(table):
    for row in range(0, 9):
        for column in range (0, 9):
            if(table[row][column] == 0):
                for i in range(1, 9):
                    if not(findAll(table, i, row, column)):
                        table[row][column] = i
                        
    return table

def solver2(table):
    def solve(table, row):
        
        def solve2(table2, col):
            
            def solve3(table3, i):
                
                if not(findAll(table3, i, row, col)):
                    table3[row][col] = i
                    return table3
                        
                if(i > 8):
                    return table3
                else:
                    return solve3(table3, i+1)
                
            if(table2[row][col] == 0):
                table2 = solve3(table2, 1)
            
            if(col > 7):
                return table2
            else:
                return solve2(table2, col+1)
            
        table = solve2(table, 0)
        
        if(row > 7):
            return table
        else:
            return solve(table, row+1)
    
    return solve(table, 0)


def solver3(table):
    def solve(table, row):
        
        def solve2(table2, col):
            
            def solve3(table3, i):
                
                if not(findAll(table3, i, row, col)):
                    table3[row][col] = i
                    return table3
                        
                if(i > 8):
                    return table3
                else:
                    return solve3(table3, i+1)
                
            if(table2[row][col] == 0):
                table2 = solve3(table2, 1)
            
            if(col > 7):
                return table2
            else:
                return solve2(table2, col+1)
            
        table = solve2(table, 0)
        
        if(row > 7):
            return table
        else:
            return solve(table, row+1)
    
    return solve(table, 0)


def solver4(table):
    row = 0
    col = 0
    
    while(row < 8 and col < 8):
        for i in range(1, 9):
            if not(findAll(table, i, row, col)):
                table[row][col] = i
    
    
    for row in range(0, 9):
        for column in range (0, 9):
            if(table[row][column] == 0):
                for i in range(1, 9):
                    if not(findAll(table, i, row, column)):
                        table[row][column] = i
    return table


def solver5(table):
    def solve(table2, row, col):
        for i in range(1, 9):
            if(row > 7):
                return table2
            
            if not(findAll(table, i, row, col)):
                table2[row][col] = i
                if(col < 7):
                    return solve(table2, row, col+1)
                else:
                    if(col >= 7):
                        return solve(table2, row+1, 0)
        
    
    return solve(table, 0, 0)

###########################

def solver6(t):
    row = 0
    col = 0
    while(row < 8 or col < 8):
        if(t[row][col] == 0):
            for i in range(1, 9):
                if not(findAll(t, i, row, col)):
                    t[row][col] = i
                    col += 1
                    if(col > 8):
                        col = 0
                        row += 1
                    if(row > 8):
                        return t
    
    
    return t

def solver7(t):
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

def solver8(t2):
    r = 0
    c = 0
    def solve(t, row, col):
        if(row >= 8 and col >= 8):
            return t
        
        if(t[row][col] == 0):
            for i in range(1, 10):
                if not(findAll(t, i, row, col)):
                    t[row][col] = i
                    if(col >= 8):
                        return solve(t, row+1, 0)
                    else:
                        return solve(t, row, col+1)
    
    
    t2 = solve(t2, r, c)
    return t2

# The working one
def solver9(t):
    r = 0
    c = 0
    def solve(row, col):
        if(row >= 8 and col >= 8):
            t[row][col] = 'Done'
            return
        
        if(t[row][col] == 0):
            for i in range(1, 10):
                if not(findAll(t, i, row, col)):
                    t[row][col] = i
                    if(col >= 8):
                        solve(row+1, 0)
                    else:
                        solve(row, col+1)
            if not(t[8][8] == 0):
                return
            t[row][col] = 0
            return
        else:
            if(col >= 8):
                solve(row+1, 0)
            else:
                solve(row, col+1)
    
    
    solve(r, c)
    return t



def solver10(t):
    result_table = t
    r = 0
    c = 0
    def solve(row, col):
        if(row >= 8 and col >= 8):
            t[8][8] = 'Done'
            result_table = t
            return
        
        if(t[row][col] == 0):
            for i in range(1, 10):
                if not(findAll(t, i, row, col)):
                    t[row][col] = i
                    if(col >= 8):
                        solve(row+1, 0)
                    else:
                        solve(row, col+1)
            if not(t[8][8] == 0):
                return
            if(row >= 8 and col >= 8):
                return
            
            #t[row][col] = 0
            return
        else:
            if(col >= 8):
                solve(row+1, 0)
            else:
                solve(row, col+1)
    
    
    solve(r, c)
    return result_table

def solver11(inputTable):
    
    def solve(t, row, col):
        if(row >= 8 and col >= 8):
            return t
        
        if(t[row][col] == 0):
            for i in range(1, 10):
                if(findAll(t, i, row, col)):
                    t[row][col] = i
                if(col >= 8):
                    t = solve(t, row+1, 0)
                else:
                    t = solve(t, row, col+1)
            t[row][col] = 0
            return t
        else:
            if(col >= 8):
                t = solve(t, row+1, 0)
            else:
                t = solve(t, row, col+1)
            
    
    return solve(inputTable, 0, 0)


###########################################
table0 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

table1 = [[0, 0, 0, 0, 0, 0, 9, 0, 0],
         [7, 0, 0, 9, 0, 0, 0, 3, 0],
         [0, 0, 0, 0, 3, 0, 1, 0, 7],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [4, 0, 3, 1, 0, 0, 2, 5, 0],
         [0, 0, 6, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 7, 0, 0, 3],
         [0, 9, 7, 5, 8, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 4 ,0, 0]]

table2 =[[0, 0, 0, 2, 6, 0, 7, 0, 1],
         [6, 8, 0, 0, 7, 0, 0, 9, 0],
         [1, 9, 0, 0, 0, 4, 5, 0, 0],
         [8, 2, 0, 1, 0, 0, 0, 4, 0],
         [0, 0, 4, 6, 0, 2, 9, 0, 0],
         [0, 5, 0, 0, 0, 3, 0, 2, 8],
         [0, 0, 9, 3, 0, 0, 0, 7, 4],
         [0, 4, 0, 0, 5, 0, 0, 3, 6],
         [7, 0, 3, 0, 1, 8, 0, 0, 0]]

table9 = [[0, 0, 0, 8, 0, 7, 6, 5, 4],
         [0, 8, 0, 0, 0, 0, 0, 0, 0],
         [9, 7, 0, 0, 0, 0, 0, 0, 0],
         [0, 3, 0, 0, 0, 0, 0, 0, 0],
         [4, 2, 0, 0, 0, 0, 0, 0, 0],
         [5, 6, 0, 0, 0, 0, 0, 0, 0],
         [6, 9, 0, 0, 0, 0, 0, 0, 0],
         [7, 5, 0, 0, 0, 0, 0, 0, 0],
         [8, 4, 3, 0, 0, 0, 0, 0, 0]]

if(findBox(table9, 4, 1, 7)):
    print("found")
else:
    print("not found")


result = solver4(table2)
for i in range(0, 9):
    print(result[i])
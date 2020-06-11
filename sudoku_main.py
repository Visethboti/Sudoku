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
###############################################        


def solver(table):
    for row in range(0, 9):
        for column in range (0, 9):
            if(table[row][column] == 0):
                for i in range(1, 9):
                    if not(findAll(table, i, row, column)):
                        table[row][column] = i
    return table



def solver2(table):
    
    def solRow(table, currentRow):
        def solColumn(table, currentColumn):
            
            if(table[currentRow][currentColumn] == 0):
                for i in range(1, 9):
                    if(findAll(table, i, currentRow, currentColumn))
                        table[currentRow][currentColumn] = i
            
            if (currentColumn > 8):
                return
            solColumn(table, currentColumn+1)
        if (currentRow > 8):
            return 
        solRow(table, currentRow+1)
        
    return table



def solver3(table):
    
    def solColumn(table, currentColumn):
        if(currentColumn > 8)
            return
        return solColumn(table, currentColumn+1):
    
    def solRow(table, currentRow):
        if(currentRow > 8):
            return 
        return solRow(table, currentRow+1):
    
    currentRow = 0
    currentColumn = 0
    
    solRow()
    
    
    #for row in range(0, 9):
    #    for column in range (0, 9):
    #        if(table[row][column] == 0):
    #            for i in range(1, 9):
    #                if not(findRow(table, i, row) or findColumn(table, i, column) or findBox(table, i, row, column)):
    #                    table[row][column] = i
    #return table


def solver4(table):
    def solve(table, row):
        
        def solve2(table2, col):
            
            def solve3(table3, i):
                
                if(table3[row][col] == 0):
                    if not(findAll(table3, i, row, col)):
                        table3[row][col] = i
                
                if(i > 8):
                    return table3
                else:
                    return solve3(table3, i+1)
                
            
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

"""
def solver4(table):
    def solve(table, row):
        
        def solve2(table2, col):
            if(col > 8):
                return table2
            else:
                return solve2(table2, col+1)
            
        table = solve2(table, 0)
        
        if(row > 8):
            return table
        else:
            return solve(table, row+1)
    
    return solve(table, 0)
"""          

###############################################    

table1 = [[0, 0, 0, 0, 0, 0, 9, 0, 0],
         [7, 0, 0, 9, 0, 0, 0, 3, 0],
         [0, 0, 0, 0, 3, 0, 1, 0, 7],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [4, 0, 3, 1, 0, 0, 2, 5, 0],
         [0, 0, 6, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 7, 0, 0, 3],
         [0, 9, 7, 5, 8, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 4 ,0, 0]]

table2 = [[0, 0, 0, 0, 0, 0, 9, 0, 0],
         [7, 0, 0, 9, 0, 0, 0, 3, 0],
         [0, 0, 0, 0, 3, 0, 1, 0, 7],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [4, 0, 3, 1, 0, 0, 2, 5, 0],
         [0, 0, 6, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 7, 0, 0, 3],
         [0, 9, 7, 5, 8, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 4 ,0, 0]]

output_table = solver(table2)
for i in range(0, 9):
    print(output_table[i])


    


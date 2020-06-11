def findRow(n, index):
    for i in range(0, 9):
        if(table[index][i] == n):
            return True
    return False

def findColumn(n, index):
    for i in range(0, 9):
        if(table[i][index] == n):
            return True
    return False
            
def findBox(n, indexR, indexC):
    
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

###############################################            

table2 = [[0, 0, 0, 0, 0, 0, 9, 0, 0],
         [7, 0, 0, 9, 0, 0, 0, 3, 0],
         [0, 0, 0, 0, 3, 0, 1, 0, 7],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [4, 0, 3, 1, 0, 0, 2, 5, 0],
         [0, 0, 6, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 7, 0, 0, 3],
         [0, 9, 7, 5, 8, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 4 ,0, 0]]

table = [[0, 0, 0, 0, 0, 0, 9, 0, 0],
         [7, 0, 0, 9, 0, 0, 0, 3, 0],
         [0, 0, 0, 0, 3, 0, 1, 0, 7],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [4, 0, 3, 1, 0, 0, 2, 5, 0],
         [0, 0, 6, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 7, 0, 0, 3],
         [0, 9, 7, 5, 8, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 4 ,0, 0]]

print(findBox(2, 0 , 0))




if(findColumn(3, 0)):
    print("found it")
else:
    print("not found")
    
    
switcher = {
        1: "Hello"
    }
print(switcher.get(1))
    


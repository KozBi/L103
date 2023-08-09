import random

def print_board(matrix):
    line=[2,5]
    for y in range(9):
        print(end="\n")
        if y==3 or y==6 :
            print(end="\n")
        for x in range(9):
            print (f"[{matrix[x][y]}]", end=" ")
            if x in line:
                print ("|",end=" ")

def get_board():
    board = [[None] * 9 for _ in range(9)]
    for xsquare_num in [0,3,6]:
        for ysquare_num in [0,3,6]:
            small_square=[]
            for x in range(3):
                for y in range(3):
                    while True:
                        value = random.randint(1,9)
                        if value not in small_square:
                            board[x+xsquare_num][y+ysquare_num]=value
                            small_square.append(value)
                            break

    return board

def check(marix_9):
    rules_ok=True
    error=[]

    for x in range(9): # check columns
        column=[]
        if not rules_ok:
            break
        for y in range(9): 
            _value=marix_9[x][y]
            if _value in column:                   
                rules_ok=False
                error=["Error in column", x,y]
                break
            else: column.append(_value)
    
    if rules_ok: # Check rows
        for y in range(9):
            row=[]
            if not rules_ok:
                break
            for x in range(9): 
                _value=marix_9[x][y]
                if _value in row:                   
                    rules_ok=False
                    error=["Error in row",x,y,]
                    break
                else: row.append(_value)
    if rules_ok: # check small squares 3x3
        for xsquare_num in [0,3,6]:
            for ysquare_num in [0,3,6]:
                small_square=[]
                for x in range(3):
                    for y in range(3):
                        _value=marix_9[x+xsquare_num][y+ysquare_num]
                        if _value in small_square:                   
                            rules_ok=False
                            error=["Error in squre",x,y]
                            break
                        else: row.append(_value)
    print(end="\n")
    if rules_ok:
        print("Board is OK")
    else:
        print(f"Board is not OK \n{error}")



board=get_board()
print_board(board)
check(board)
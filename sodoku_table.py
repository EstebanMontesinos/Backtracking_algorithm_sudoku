board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
def validspot(bo, num, pos):
    # Check row
    for x in range(len(bo[0])):
        if bo[pos[0]][x] == num and pos[1] != x:#It will check through every element in the row and will check if its = to the number we inserted and then checks for the position that was just inserted.
            return False

    # Check column
    for y in range(len(bo)):
        if bo[y][pos[1]] == num and pos[0] != y:#This will go down loooping through every row checking if the curent column value is the same value as the number inserted and the checks if that position is the one we just inserted and ignores it
            return False

    # Check box
    box_x = pos[1] // 3 #to get position inside blocks of 3 by 3 columns
    box_y = pos[0] // 3 #to get position inside blocks of 3 by 3 in terms of rows.

    for i in range(box_y*3, box_y*3 + 3):#We multiply position by 3 once we have checked which box we are in to get our actual position and then add 3 to check the rest of the columns since the  for loop does not go till the last element.
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True #Once all tests are passed it will return true.
def print_board(bo):
    for y in range(len(bo)):
        if y % 3 ==0 and y !=0:
            print("- - - - - - - - - - - - -")#printing when i is divisible by 3 cause every 3 rows we want to print that line.

        for x in range(len(bo[0])): #bo[0] basically just the size of each row
            if x % 3 == 0 and x != 0: #check individual numbers inside the first segment to create the perpencicular lines accordingly
                print(" | ", end="")# we use end("")to not go to a new line \n until we iterate succesfuly  over i
            if x == 8:
                print(bo[y][x])  #No extra space needed
            else:
                print(str(bo[y][x]) + " ", end="")

def find_empty(bo):
    for y in range(len(bo)):
        for x in range(len(bo[0])):
            if bo[y][x]== 0:
                return(y,x)# returns a tuple containing  row and column
    return None

def backtrack(bo):
    find = find_empty(bo)
    if not find: #  if not find !=True
        return True #stops the program when done
    else:
        row, col = find

    for i in range(1, 10):
        if validspot(bo, i, (row, col)):
            bo[row][col] = i

            if backtrack(bo):
                return True

            bo[row][col] = 0

    return False # makes if backtrack(bo): false therefore calling bo[row][col] = 0


print_board(board)
backtrack(board)
print('\n')
print_board(board)
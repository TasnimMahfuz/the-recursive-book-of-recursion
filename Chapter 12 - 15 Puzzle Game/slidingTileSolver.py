#Setting up the program's constants

import random, time

DIFFICULTY =  40 #Number of random slides at the starting of the puzzle
SIZE = 4 #Board dimension 4 by 4
random.seed(1)

BLANK = 0
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def displayBoard(board):
    """To display the tiles stored in the board on the screen"""
    for y in range(SIZE):  #row iteration
        for x in range(SIZE): #column iteration
            if board[y*SIZE + x] == BLANK:
                print('__ ', end='')
            else:
                print(str(board[y*SIZE + x]).rjust(2)+' ', end='')
        print()
            
def getNewBoard():
    """Returns a solved puzzle representing list"""
    
    board = []
    for i in range(1, SIZE*SIZE):
        board.append(i)
    board.append(BLANK)
    
    #board[9] = BLANK
    return board

#displayBoard(getNewBoard())

def findBlankSpaceMyFunc(board):
    """Returns an [x,y] list of the blank space's location"""
    
    for i in range(SIZE*SIZE):
        if board[i] == BLANK:
            index = i
            break
        
    x = index//SIZE
    y = index - (x*SIZE)
    
    return [y, x]

    
def findBlankSpace(board):
    for x in range(SIZE):
        for y in range(SIZE):
            if board[x + y*SIZE] == BLANK:
                return [x,y]
    
#print(findBlankSpace(getNewBoard()))
#print(findBlankSpaceMyFunc(getNewBoard()))

def makeMove(board, move):
    bx, by = findBlankSpace(board)
    blankIndex = bx + by*SIZE
    
    if move == UP:
        tileIndex = (by+1)*SIZE + bx
    elif move == DOWN:
        tileIndex = (by -1)*SIZE + bx
    elif move == RIGHT:
        tileIndex = by*SIZE + bx -1
    elif move == LEFT:
        titlIndex = by*SIZE + bx + 1
        
    board[blankIndex], board[tileIndex] = board[tileIndex], board[blankIndex]
    
    
def undoMove(board, move):
    if move == UP:
        makeMove(board, DOWN)
    elif move == DOWN:
        makeMove(board, UP)
    elif move == RIGHT:
        makeMove(board, LEFT)
    elif move == LEFT:
        makeMove(board, RIGHT)
        
        
def getValidMoves(board, prevMove = None):
    """Return a list of valid moves.
    If prev move included, Do not return it, as it will undo a valid move"""
    
    blankx, blanky = findBlankSpace(board)
    validMoves = []
    
    
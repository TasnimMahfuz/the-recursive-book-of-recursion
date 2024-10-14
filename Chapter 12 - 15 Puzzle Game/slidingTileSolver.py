#Setting up the program's constants

import random, time

DIFFICULTY =  200 #Number of random slides at the starting of the puzzle
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
        tileIndex = by*SIZE + bx + 1
        
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
        
def undoMoveMyFunc(board, move):
    makeMove(board, findOppositeMove(move))
        
def findOppositeMove(board, move):
    if move ==UP:
        return DOWN
    elif move == DOWN:
        return UP
    elif move == LEFT:
        return RIGHT
    elif move == RIGHT:
        return LEFT
    
def getValidMovesMyFunc(board, prevMove = None):
    """Return a list of valid moves
    Do not include the previous move's opposite, as it will just undo the progress"""   
    blankx, blanky = findBlankSpace(board)
    validMoves = [UP, DOWN, LEFT, RIGHT]
    
    if blankx == 0:
        validMoves.remove(RIGHT)
    elif blankx == (SIZE - 1):
        validMoves.remove(LEFT)
    elif blanky == 0:
        validMoves.remove(DOWN)
    elif blanky == (SIZE - 1):
        validMoves.remove(UP)
        
    validMoves.remove(findOppositeMove(prevMove))
    
    return validMoves
    
def getValidMoves(board, prevMove = None):
    """Return a list of valid moves.
    If prev move included, Do not return its opposite, as it will undo a valid move"""
    
    blankx, blanky = findBlankSpace(board)
    validMoves = []
    
    if blanky != SIZE - 1 and prevMove != DOWN:
        validMoves.append(UP)
        
    if blankx != SIZE - 1 and prevMove != RIGHT:
        validMoves.append(LEFT)
    
    if blanky != 0 and prevMove != UP:
        validMoves.append(DOWN)
        
    if blankx != 0 and prevMove!= LEFT:
        validMoves.append(RIGHT)
        
    return validMoves
    
    
def getNewPuzzle():
    board = getNewBoard()
    for i in range(DIFFICULTY):
        validMoves = getValidMoves(board)
        makeMove(board, random.choice(validMoves))
        
    return board

displayBoard(getNewPuzzle())
    
    
def solve(board, maxMoves):
    
    print(f"Attempting to solve the puzzle in {maxMoves} moves")
    solutionMoves = []
    
    solved = attemptMove(board, solutionMoves, maxMoves, None)
    
    if solved:
        displayBoard(board)
        
        for move in solutionMoves:
            print('Move:', move)
            makeMove(board, move)
            print()
            
            displayBoard(board)
            print()
            
        print('Solved in', len(solutionMoves), 'moves: ')
        print(', '.join(solutionMoves))
        return True
    else:
        return False
    
    

def attemptMove(board, movesMade, movesRemaining, prevMove):
    if movesRemaining < 0:
        return False
    
    if board == SOLVED_BOARD:
        return True
    
    
    for move in getValidMoves(board, prevMove):
        makeMove(board, move)
        movesMade.append(move)
    
        if attemptMove(board, movesMade, movesRemaining - 1, move):
            undoMove(board, move)
            return True
        undoMove(board, move)
        movesMade.pop()
        
    return False


SOLVED_BOARD = getNewBoard()
puzzleBoard = getNewPuzzle()
displayBoard(puzzleBoard)
print('-------------------------')
startTime = time.time()

maxMoves = 10

while(True):
    if solve(puzzleBoard, maxMoves):
        break
    maxMoves += 1
    
print('Run in', round(time.time() - startTime, 3), 'seconds.')
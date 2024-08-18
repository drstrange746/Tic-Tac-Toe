board = [ "_", "_", "_", 
        "_", "_", "_", 
        "_", "_", "_" ]

currentPlayer = "X"
winner = None
gameRunning = True

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("__________")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("__________")
    print(board[6] + " | " + board[7] + " | " + board[8])

def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <=9 and board[inp-1] == "_":
        board[inp-1] = currentPlayer
    else:
        print("Choose another spot!")

def checkHorizontal(board):
    global winner 
    if board[0] == board[1] == board[2] and board[1] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[4]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "_":
        winner = board[7]
        return True
    
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True
    
    elif board[1] == board[4] == board[2] and board[7] != "_":
        winner = board[7]
        return True
    
    elif board[2] == board[5] == board[8] and board[8] != "_":
        winner = board[8]
        return True
    
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    
    elif board[2] == board[4] == board[6] and board[6] != "_":
        winner = board[6]
        return True

def checkTie(board):
    if "_" not in board:
        printBoard(board)
        print("!Tie!")
        gameRunning = False

def SwitchPlayer(board):
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
    
def Checkwin(board):
    global gameRunning
    if checkDiag(board) or checkHorizontal(board) or checkRow(board):
        print(f"The winner is {winner}")
        gameRunning = False



while gameRunning:
    printBoard(board)
    playerInput(board)
    Checkwin(board)
    checkTie(board)
    SwitchPlayer(board)
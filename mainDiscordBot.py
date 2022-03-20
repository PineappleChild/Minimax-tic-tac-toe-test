
class ticTacBoard:
    board = [["_","_","_"],["_","_","_"],["_","_","_"]]
    player, opponent = "O", "X"
    def __init__(self, mode):
        self.mode = mode

    def getBoard(self):
        return self.board

    def printBoard(self):
        for x in range(3):
            print(self.board[x])

    def changePos(self, row, col, side):
        if side == "x":
            self.board[row][col] = self.player
        elif side == "o":
            self.board[row][col] = self.opponent


    def takenPositions(self, arr):
        takenPos = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] != "_":
                    takenPos.append([row,col])
        if arr in takenPos:
            return False
        return True

    def movesLeft(self, board):
        for row in range(3):
            for col in range(3):
                if board[row][col] == "_":
                    return True
        return False

    def evaluate(self, b):

        for row in range(3):
            if (b[row][0] == b[row][1] and b[row][1] == b[row][2]):
                if (b[row][0] == self.player):
                    return 1
                elif (b[row][0] == self.opponent):
                    return -1

        for col in range(3):
            if (b[0][col] == b[1][col] and b[1][col] == b[2][col]):
                if (b[0][col] == self.player):
                    return 1
                elif (b[0][col] == self.opponent):
                    return -1

        if (b[0][0] == b[1][1] and b[1][1] == b[2][2]):
            if (b[0][0] == self.player):
                return 1
            elif (b[0][0] == self.opponent):
                return -1

        if (b[0][2] == b[1][1] and b[1][1] == b[2][0]):
            if (b[0][2] == self.player):
                return 1
            elif (b[0][2] == self.opponent):
                return -1

        return 0

    def minimax(self, board, depth, isMaximized):
        scoreVAl = self.evaluate(board)

        if scoreVAl == 1:
            return scoreVAl
        if scoreVAl == -1:
            return scoreVAl
        if self.movesLeft(board) == False:
            return 0

        if isMaximized:
            best = -10

            for row in range(3):
                for col in range(3):
                    if (board[row][col] == '_'):
                        board[row][col] = self.player
                        evalVal = self.minimax(board, depth + 1, False)
                        best = max(best, evalVal)
                        #
                        # alpha = max(alpha, evalVal)
                        # if beta <= alpha:
                        #     break
                        board[row][col] = '_'

            return best

        else:
            best = 10

            for row in range(3):
                for col in range(3):
                    if (board[row][col] == '_'):
                        board[row][col] = self.opponent
                        evalVal = self.minimax(board, depth + 1, True)
                        best = min(best, evalVal)
                        #
                        # beta = min(beta, evalVal)
                        # if beta <= alpha:
                        #     break
                        board[row][col] = '_'
            return best

    def bestMove(self, board):
        bestVal = -10
        bestPos = []

        for row in range(3):
            for col in range(3):
                if (board[row][col] == '_'):
                    board[row][col] = self.player
                    moveVal = self.minimax(board, 0, False)
                    board[row][col] = '_'
                    # print("calculated: " ,moveVal, "current: ", bestVal, row, col)
                    if (moveVal > bestVal):
                        bestVal = moveVal
                        bestPos = [row,col]
        return bestPos

    def mainProcess(self):
        endGame = False
        while not endGame:
            print("Please enter a number from 1-9 that corresponds to the tic-tac-toe grid:")
            playerResponse = input()
            if self.canBeInt(playerResponse) and int(playerResponse) < 10 and int(playerResponse) > 0:
                moveArr = self.convertToArrVal(int(playerResponse))
                if self.takenPositions(moveArr):
                    self.changePos(moveArr[0], moveArr[1], "o")
                    aiArr = self.bestMove(self.board)
                    if self.movesLeft(self.board) != False:
                        self.changePos(aiArr[0], aiArr[1], "x")
                else:
                    print("Invalid Move")
            if self.evaluate(self.board) == 1 or self.evaluate(self.board) == -1 or self.movesLeft(self.board) == False:
                endGame = True
            if playerResponse == "STOP":
                endGame = True
            self.printBoard()
        if self.evaluate(self.getBoard()) == 1:
            print("X is the winner!")
        elif self.evaluate(self.getBoard()) == -1:
            print("O is the winner!")
        elif self.movesLeft(self.board) == False:
            print("There was a tie")


    def canBeInt(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    def convertToArrVal(self, value):
        positions = {
            1:[0,0],
            2:[0,1],
            3:[0,2],
            4:[1,0],
            5:[1,1],
            6:[1,2],
            7:[2,0],
            8:[2,1],
            9:[2,2]
        }
        return positions[value]
x = ticTacBoard("e")

x.mainProcess()

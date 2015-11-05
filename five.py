from random import randint


class Board(object):
    def __init__(self):
        self.board = []
        self.flipboard = []
        for x in range(0,9):
            self.board.append(['-', '-', '-', '-', '-', '-', '-', '-', '-'])
            self.flipboard.append(['-', '-', '-', '-', '-', '-', '-', '-', '-'])

    ## Constructs a board reflected across the diagonal to test for horizontal win
    def flip(self):
        for x in range(0,9):
            for y in range(0,9):
                self.flipboard[x][y] = self.board[y][x]

    def printout(self):
        for x in range(9):    
            if x == 0:
                print "_____________________________________ ", "\n"
            for y in range(9):
                if y == 0:
                    print "| ",
                print self.board[x][y] + " |",
            print "\n", "_____________________________________ "
    
    def has_player_won(self, last_row, last_column):
        if self.check_hor_and_vert():
            return True
        elif self.check_diags(last_row, last_column):
            return True
        else:
            return False

    def check_hor_and_vert(self):
        if "OOOOO" in self.board or "XXXXX" in self.board:
            return True
        elif "OOOOO" in self.flipboard or "XXXXX" in self.flipboard:
            return True
        else:
            return False
    

    # checks the diagonals for a possible win
    def check_diags(self, last_row, last_column):
    
        # check the symbol to be tested
        mark = self.board[last_row][last_column]

        # lists for the diagonals surrounding input point
        temp1 = []
        temp2 = []
       
        # booleans for determining list direction
        NE = True
        NW = True
        SW = True
        SE = True


        # checks for a SW win
        for x in range(0,5):
            new_row = last_row + x
            new_column = last_column - x

            SW = self.dirSW(new_row, new_column)

            if board.board[new_row][new_column] == mark:
                temp1.append("X")
        
            if not SW:
                break    

        # checks for a NE win
        for x in range(0,5):
            new_row = last_row - x
            new_column = last_column + x

            NE = self.dirNE(new_row, new_column)

            if board.board[new_row][new_column] == mark and x != 0:
                temp1.append("X")

            if not NE:
                break

        # checks for a NW win
        for x in range(0,5):
            new_row = last_row - x
            new_column = last_column - x

            NW = self.dirNW(new_row, new_column)

            if board.board[new_row][new_column] == mark:
                temp2.append("X")
 
            if not NW:
                break    

        # checks for a SE win
        for x in range(0,5):
            new_row = last_row + x
            new_column = last_column + x

            SE = self.dirSE(new_row, new_column)

            if board.board[new_row][new_column] == mark and x != 0:
                temp2.append("X")
 
            if not SE:
                break

        if "XXXXX" in "".join(temp1) or "XXXXX" in "".join(temp2):
            return True
        else:
            return False

    # takes a point as an input and decides which directions it could 
    # possibly have a win in
    def dirNE(self, row, column):
        if row == 0 or column ==8:
            return False
        else:
            return True

    def dirNW(self, row, column):
        if row == 0 or column == 0:
            return False
        else:
            return True

    def dirSE(self, row, column):
        if row == 8 or column == 8:
            return False
        else:
            return True

    def dirSW(self, row, column):
        if row == 8 or column == 0:
            return False
        else:
            return True



class Computer(object):
    def __init__(self, symbol):
        self.symbol = symbol

    def take_turn(self, board):
        while True:
            row = randint(0,8)
            column = randint(0,8)
            if board.board[row][column] == '-':               
                return (row, column)
                break


###################Main Body#########################
print "Welcome to five in a row!"


# determine whether the user wants x or o
while True:
    print "X goes first."
    print "Would you like to be X or O?"
    symbol = raw_input("???").upper()

    if symbol == "O":
        comp_symbol = "X"
        compturn = True
        break
    elif symbol == "X":
        comp_symbol = "O"
        compturn = False
        break
    else:
        print "Please enter either X or O"

comp = Computer(comp_symbol)
board = Board()

board.printout()

# play the game
while True:

    if compturn:
        print "Here is the computer's move."
        row, column = comp.take_turn(board)
        board.board[row][column] = comp_symbol
        compturn = False
    else:
        print "In which row would you like to place your %s?" % symbol
        row = int(raw_input("???"))
        print "In which column would you like to place your %s?" % symbol
        column = int(raw_input("???"))
        board.board[int(row)][int(column)] = "%s" % symbol
        compturn = True

    board.flip()

    if board.has_player_won(row, column):
        print "We have a win!"
        board.printout()
        break

    for a in board.board:
        if "-" not in a:
            print "There are no spaces to play in left!"

    board.printout()

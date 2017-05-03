# Python Tic Tac Toe
#Make note that Tic Tac Toe is comprised of 9 Squares
#3x3
#I used X's and O's as place holders
#create the board (as list)
import random
board = [0,1,2,
         3,4,5,
         6,7,8]

#display the board as 3 horizontal, 3 vertical 
def displayboard():
    print board[0],'|',board[1],'|',board[2]
    print '----------'
    print board[3],'|',board[4],'|',board[5]
    print '----------'
    print board[6],'|',board[7],'|',board[8]
    print '----------'

#function to check winner
def check(char,place1,place2,place3):
    if board[place1] == char and board[place2] == char and board[place3] == char:
        return True

#check all possible ways of wiining
def compareall(char):
    #winner horizontally
    if check(char,0,1,2):
        return True
    if check(char,3,4,5):
        return True
    if check(char,6,7,8):
        return True

    
    #winner vertically   
    if check(char,0,3,6):
        return True
    if check(char,1,4,7):
        return True
    if check(char,2,5,8):
        return True

    
    #Winner disagonally
    if check(char,0,4,8):
        return True
    if check(char,6,4,2):
        return True

#call displayboard to show initial position of fresh game
displayboard()

while True:
    print 'Choose from 0 - 8'
    #pause the loop for raw iput
    input = raw_input("Selection:  ")
    print "\n"
    #if they type letter, it will be cast into int
    input = int(input)
    #if not x or o, add x
    if board[input] !='x' and board[input] !='o':
        board[input] = 'x'

        if compareall('x') == True:
            print "----You win!---"
            break;
    # Have computer randomly generate a place
    # create a loop
    openspot = True

    while openspot:
        random.seed()
        computer = random.randint(0,8)
        # if not o or x, the add o
        if board[computer] != 'o' and board[computer] != 'x':
            board[computer] = 'o'

            if compareall('o')== True:
                print "Computer Wins! You lose!"
                break;
            #false to jump out of while loop 
            openspot = False

    #validate they dont choose the same number twice
    # if its twice, they display error
    else:
        print 'Invalid entry, spot taken'
    #after all done, display the updated board.
    displayboard()

    

#####################################################
# Simple Tic Tac Toe Game                           #
# Made By Jose Hernandez                            #
#                                                   #
#                   0 | 1 | 2                       #
#                    ---------                      #
#                   3 | 4 | 5                       #
#                   ---------                       #
#                   6 | 7 | 8                       #
#                                                   #
#####################################################


#Make note that Tic Tac Toe is comprised of 9 Squares
#3x3
#I used X's and O's as place holders
#create the board (as list)
import random
board = [0,1,2,
         3,4,5,
         6,7,8]
whos_go = random.randint(1,2)
def AI_Attacking():
	global attacking
	global computer
	attacking = False

	#-Horizontal Attack-#

	
	if(board[0] == "O" and board[1] == "O" and board[2] == " "):
		computer = 2
		attacking = True
	elif(board[1] == "O" and board[2] == "O" and board[0] == " "):
		computer = 0
		attacking = True
	elif(board[0] == "O" and board[2] == "O" and board[1] == " "):
		computer = 1
		attacking = True

	
	if(board[3] == "O" and board[4] == "O" and board[5] == " "):
		computer = 5
		attacking = True
	elif(board[4] == "O" and board[5] == "O" and board[3] == " "):
		computer = 3
		attacking = True
	elif(board[3] == "O" and board[5] == "O" and board[4] == " "):
		computer = 4
		attacking = True

	
	if(board[6] == "O" and board[7] == "O" and board[8] == " "):
		computer = 8
		attacking = True
	elif(board[7] == "O" and board[8] == "O" and board[6] == " "):
		computer = 6
		attacking = True
	elif(board[6] == "O" and board[8] == "O" and board[7] == " "):
		computer = 7
		attacking = True



         #Vertical	
	if(board[0] == "O" and board[3] == "O" and board[6] == " "):
		computer = 6
		attacking = True
	elif(board[3] == "O" and board[6] == "O" and board[0] == " "):
		computer = 0
		attacking = True
	elif(board[0] == "O" and board[6] == "O" and board[3] == " "):
		computer = 3
		attacking = True

	#vertical
	if(board[1] == "O" and board[4] == "O" and board[7] == " "):
		computer = 7
		attacking = True
	elif(board[4] == "O" and board[7] == "O" and board[1] == " "):
		computer = 1
		attacking = True
	elif(board[1] == "O" and board[7] == "O" and board[4] == " "):
		computer = 4
		attacking = True

	#vertical
	if(board[2] == "O" and board[5] == "O" and board[8] == " "):
		computer = 8
		attacking = True
	elif(board[5] == "O" and board[8] == "O" and board[2] == " "):
		computer = 2
		attacking = True
	elif(board[2] == "O" and board[8] == "O" and board[5] == " "):
		computer = 3
		attacking = True

	

	#Diagnoal attack
	if(board[0] == "O" and board[4] == "O" and board[8] == " "):
		computer = 8
		attacking = True
	elif(board[4] == "O" and board[8] == "O" and board[0] == " "):
		computer = 0
		attacking = True
	elif(board[0] == "O" and board[8] == "O" and board[4] == " "):
		computer = 4
		attacking = True

	#diagnol attack
	if(board[2] == "O" and board[4] == "O" and board[6] == " "):
		computer = 6
		attacking = True
	elif(board[4] == "O" and board[6] == "O" and board[2] == " "):
		computer = 2
		attacking = True
	elif(board[2] == "O" and board[6] == "O" and board[4] == " "):
		computer = 4
		attacking = True

	return attacking, computer


def AI_Defending():
	global defending
	global computer
	defending = False

	

	#block across
	if(board[0] == "X" and board[1] == "X" and board[2] == " "):
		computer = 2
		defending = True
	elif(board[1] == "X" and board[2] == "X" and board[0] == " "):
		computer = 0
		defending = True
	elif(board[0] == "X" and board[2] == "X" and board[1] == " "):
		computer = 1
		defending = True

	#block across
	if(board[3] == "X" and board[4] == "X" and board[5] == " "):
		computer = 5
		defending = True
	elif(board[4] == "X" and board[5] == "X" and board[3] == " "):
		computer = 3
		defending = True
	elif(board[3] == "X" and board[5] == "X" and board[4] == " "):
		computer = 4
		defending = True

	#block across
	if(board[6] == "X" and board[7] == "X" and board[8] == " "):
		computer = 8
		defending = True
	elif(board[7] == "X" and board[8] == "X" and board[6] == " "):
		computer = 6
		defending = True
	elif(board[6] == "X" and board[8] == "X" and board[7] == " "):
		computer = 7
		defending = True

	

	#Vertical block
	if(board[0] == "X" and board[3] == "X" and board[6] == " "):
		computer = 6
		defending = True
	elif(board[3] == "X" and board[6] == "X" and board[0] == " "):
		computer = 0
		defending = True
	elif(board[0] == "X" and board[6] == "X" and board[3] == " "):
		computer = 3
		defending = True

	#vertical block
	if(board[1] == "X" and board[4] == "X" and board[7] == " "):
		computer = 7
		defending = True
	elif(board[4] == "X" and board[7] == "X" and board[1] == " "):
		computer = 1
		defending = True
	elif(board[1] == "X" and board[7] == "X" and board[4] == " "):
		computer = 4
		defending = True

	#vertical block
	if(board[2] == "X" and board[5] == "X" and board[8] == " "):
		computer = 8
		defending = True
	elif(board[5] == "X" and board[8] == "X" and board[2] == " "):
		computer = 2
		defending = True
	elif(board[2] == "X" and board[8] == "X" and board[5] == " "):
		computer = 3
		defending = True

	

	#block diagnol
	if(board[0] == "X" and board[4] == "X" and board[8] == " "):
		computer = 8
		defending = True
	elif(board[4] == "X" and board[8] == "X" and board[0] == " "):
		computer = 0
		defending = True
	elif(board[0] == "X" and board[8] == "X" and board[4] == " "):
		computer = 4
		defending = True

	#block diagnol
	if(board[2] == "X" and board[4] == "X" and board[6] == " "):
		computer = 6
		defending = True
	elif(board[4] == "X" and board[6] == "X" and board[2] == " "):
		computer = 2
		defending = True
	elif(board[2] == "X" and board[6] == "X" and board[4] == " "):
		computer = 4
		defending = True

	return defending, computer

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
    global whos_go
    print 'Choose from 0 - 8'
    #pause the loop for raw iput
    input = raw_input("Selection:  ")
    print "\n"
    #if they type letter, it will be cast into int
    input = int(input)
    #if not x or o, add x
    if board[input] !='X' and board[input] !='O':
        board[input] = 'X'

        if compareall('X') == True:
            print "----You win!---"
            break;
    # Have computer randomly generate a place
    # create a loop
    openspot = True

    computer = int
    attacking = False
    defending = False
    
    if board[4] == " ":
        board[4] = "O"
    else:
        AI_Attacking()
        if attacking == True:
            board[computer] = 'O'
        elif attacking == False:
                AI_Defending()
                if defending == True:
                    board[computer] = 'O'
                elif defending == False:
                    while openspot: 
                        random.seed()
                        computer = random.randint(0,8)
                        #if not O or X the add O
                        if board[computer] !='O' and board[computer] != 'X':
                            board[computer] = 'O'
                            if compareall('O') == True:
                                print "Computer Wins! You Lose!"
                                break;
                            openspot = False
                        

    #validate they dont choose the same number twice
    # if its twice, they display error
    #after all done, display the updated board.
    displayboard()

    

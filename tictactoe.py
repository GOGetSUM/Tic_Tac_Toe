from clear_screen import clear


#--------------------------------------Welcome Screen----------------------------------------------------------------------
print('''         .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.                                                 
        | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |                                                
        | | _____  _____ | || |  _________   | || |   _____      | || |     ______   | || |     ____     | || | ____    ____ | || |  _________   | |                                                
        | ||_   _||_   _|| || | |_   ___  |  | || |  |_   _|     | || |   .' ___  |  | || |   .'    `.   | || ||_   \  /   _|| || | |_   ___  |  | |                                                
        | |  | | /\ | |  | || |   | |_  \_|  | || |    | |       | || |  / .'   \_|  | || |  /  .--.  \  | || |  |   \/   |  | || |   | |_  \_|  | |                                                
        | |  | |/  \| |  | || |   |  _|  _   | || |    | |   _   | || |  | |         | || |  | |    | |  | || |  | |\  /| |  | || |   |  _|  _   | |                                                
        | |  |   /\   |  | || |  _| |___/ |  | || |   _| |__/ |  | || |  \ `.___.'\  | || |  \  `--'  /  | || | _| |_\/_| |_ | || |  _| |___/ |  | |                                                
        | |  |__/  \__|  | || | |_________|  | || |  |________|  | || |   `._____.'  | || |   `.____.'   | || ||_____||_____|| || | |_________|  | |                                                
        | |              | || |              | || |              | || |              | || |              | || |              | || |              | |                                                
        | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |                                                
         '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'                                                 
                                                     .----------------.  .----------------.                                                                                                         
                                                    | .--------------. || .--------------. |                                                                                                        
                                                    | |  _________   | || |     ____     | |                                                                                                        
                                                    | | |  _   _  |  | || |   .'    `.   | |                                                                                                        
                                                    | | |_/ | | \_|  | || |  /  .--.  \  | |                                                                                                        
                                                    | |     | |      | || |  | |    | |  | |                                                                                                        
                                                    | |    _| |_     | || |  \  `--'  /  | |                                                                                                        
                                                    | |   |_____|    | || |   `.____.'   | |                                                                                                        
                                                    | |              | || |              | |                                                                                                        
                                                    | '--------------' || '--------------' |                                                                                                        
                                                     '----------------'  '----------------'                                                                                                         
 .----------------.  .----------------.  .----------------.          .----------------.  .----------------.  .----------------.          .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. |        | .--------------. || .--------------. || .--------------. |        | .--------------. || .--------------. || .--------------. |
| |  _________   | || |     _____    | || |     ______   | |        | |  _________   | || |      __      | || |     ______   | |        | |  _________   | || |     ____     | || |  _________   | |
| | |  _   _  |  | || |    |_   _|   | || |   .' ___  |  | |        | | |  _   _  |  | || |     /  \     | || |   .' ___  |  | |        | | |  _   _  |  | || |   .'    `.   | || | |_   ___  |  | |
| | |_/ | | \_|  | || |      | |     | || |  / .'   \_|  | |        | | |_/ | | \_|  | || |    / /\ \    | || |  / .'   \_|  | |        | | |_/ | | \_|  | || |  /  .--.  \  | || |   | |_  \_|  | |
| |     | |      | || |      | |     | || |  | |         | |        | |     | |      | || |   / ____ \   | || |  | |         | |        | |     | |      | || |  | |    | |  | || |   |  _|  _   | |
| |    _| |_     | || |     _| |_    | || |  \ `.___.'\  | |        | |    _| |_     | || | _/ /    \ \_ | || |  \ `.___.'\  | |        | |    _| |_     | || |  \  `--'  /  | || |  _| |___/ |  | |
| |   |_____|    | || |    |_____|   | || |   `._____.'  | |        | |   |_____|    | || ||____|  |____|| || |   `._____.'  | |        | |   |_____|    | || |   `.____.'   | || | |_________|  | |
| |              | || |              | || |              | |        | |              | || |              | || |              | |        | |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |        | '--------------' || '--------------' || '--------------' |        | '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'          '----------------'  '----------------'  '----------------'          '----------------'  '----------------'  '----------------'  ''')



Start_ = input('Would you like to play a GAME?: (y/n) ').upper()


#--------------------------------------Game Start Second Screen----------------------------------------------------------------------

if Start_=='Y':
    mode_ =input('Please select a mode, Single or 2 Player(1/2):\n')
else:
    clear()


#--------------------------------------Game Board and First Move----------------------------------------------------------------------
#Mode : Two Player
if mode_ == "2":
    print(""" Please See Board below, positions will be chosen based on respective number (1-9), 
    
              1 |  2  | 3
            --------------
              4 |  5  | 6
            --------------
              7 |  8  | 9   
              
             Player 'X' will be first. 
              """)

    board_ = '''
              1 |  2  | 3
            --------------
              4 |  5  | 6
            --------------
              7 |  8  | 9   
    '''

# ------------------------Request,Check and Print Move per players turn-----------------------------------------------------------------------------------
turn= 2
x_moves=[]
y_moves=[]
drawn = False
player_wins = False
game_over=False
def Move():
    position_allowed = False
    global turn
    global board_
    global x_moves
    global y_moves, game_over,drawn, player_wins,hits_d
    if turn %2 == 0:
        while position_allowed == False:
            print("'X' turn")
            _move = input("Player 'X', please choose your move: (1-9)")
            try:
                board_.index(_move) #checks if move is allowed

            except ValueError:
                print("Position is not allowed")
            else:
                board_ = board_.replace(_move, "X") #replaces index
                turn += 1
                x_moves.append(_move)
                Check(x_moves,board_)
                if hits_d >=9:
                    print('Game is a Draw!')
                    game_over=True
                elif player_wins==True:
                    print("player X wins!")
                    game_over = True
                return turn, board_
                print(turn)
                position_allowed = True
    else:
        while position_allowed == False:
            print("'O' turn")
            _move = input("Player 'O', please choose your move: (1-9)")
            try:
                board_.index(_move)

            except ValueError:
                print("Position is not allowed")
            else:
                board_ = board_.replace(_move, "O")
                turn += 1
                y_moves.append(_move)
                Check(y_moves,board_)
                if hits_d >=9:
                    print('Game is a Draw!')
                    game_over=True
                elif player_wins==True:
                    print("player Y wins!")
                    game_over = True
                return turn, board_
                print(turn)
                position_allowed = True


# ------------------------Check if game is over if not continue, ask if they woud like to run a new game-----------------------------------------------------------------------------------


def Check(moves,board_):
    global drawn,player_wins,hits_d
    hits_d = 0
    wins_ = {
        '1': {1: ['1', '2', '3'],
              2: ['1', '4', '7'],
              3: ['1', '5', '9']},
        '2': {1: ['2', '1', '3'],
              2: ['2', '5', '8']},
        '3': {1: ['3', '1', '2'],
              2: ['3', '6', '9'],
              3: ['3', '5', '8']},
        '4': {1: ['4', '5', '6'],
              2: ['4', '1', '7']},
        '5': {1: ['5', '1', '9'],
              2: ['5', '3', '7'],
              3: ['5', '2', '8'],
              4: ['5', '4', '6']},
        '6': {1: ['6', '5', '4'],
              2: ['6', '3', '9']},
        '7': {1: ['7', '1', '4'],
              2: ['7', '5', '3'],
              3: ['7', '9', '8']},
        '8': {1: ['8', '5', '2'],
              2: ['8', '7', '9']},
        '9': {1: ['9', '3', '6'],
              2: ['9', '5', '1'],
              3: ['9', '8', '7']}
    }
    if len(moves) >= 4:
        tmov = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for mov in tmov:
            try:
                board_.index(mov)
            except ValueError:
                hits_d += 1
            else:
                hits_d=0

    for mov in moves:
        win_op = wins_[f'{mov}']
        for key in win_op:
            list_ = win_op[key]
            hits = 0
            for x in moves:
                try:
                    list_.index(x)  #checks if theres a 3 in a row match.
                except ValueError:
                    pass
                else:
                    hits += 1
                if hits == 3:
                    player_wins = True
    return player_wins,hits_d

# Game should be checked only after turn 4




# ------------------------Run the App-----------------------------------------------------------------------------------

while game_over == False:
    Move()
    print(board_)



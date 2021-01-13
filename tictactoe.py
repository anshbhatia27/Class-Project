def game_board():  #command for game board 
    print(l[0]+'|'+l[1]+'|'+l[2])
    print(l[3]+'|'+l[4]+'|'+l[5])
    print(l[6]+'|'+l[7]+'|'+l[8])
    
def player_move():
    while True:
        ch=int(input("choose location from 1 to 9: "))
        if (ch>=1 and ch<=9) :
            if l[ch-1]!='-':
                print("its already occupied, pick another location")
            else:
                break
        else:
            print("enter again not a valid location")
    l[ch-1]=symbol         # place symbol at that location
    game_board()       
    
def change_player(): # change player and its symbol
    global player  
    global symbol
    if player==1:
        player=2
        symbol='O'
    else:
        player=1
        symbol='X'
        
def check_win():
    if l[0]==l[4]==l[8]==symbol or l[2]==l[4]==l[6]==symbol:#checking diagonals
        return True
    elif l[0]==l[1]==l[2]==symbol or l[3]==l[4]==l[5]==symbol or l[6]==l[7]==l[8]==symbol: #checking rows
        return True
    elif l[0]==l[3]==l[6]==symbol or l[1]==l[4]==l[7]==symbol or l[2]==l[5]==l[8]==symbol:#checking columns
        return True
    else:
        return False
        
l=['-','-','-','-','-','-','-','-','-']
chance=True
player=1
symbol='X'
game_board()
while True: 
    player_move() 
    if check_win(): 
        print("player {} has won".format(player))
        break
    else:
        if '-' not in l:
            print("Its a draw")
            break
    change_player() 
        
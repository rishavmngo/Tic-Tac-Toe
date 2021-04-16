board = [['A','B','C'],['D','E','F'],['G','H','I']]
toss = 0
full = 0
full_bool = True
sets = ['0','X']

def display():
    i = 0
    horizontal = 1
    while i < 3:
        j = 1
        for some in board[i]:
            print(some,end=' '*2)
            if j < 3:
                print('|',end=' ' * 2)
                j += 1
        if horizontal < 3:
            print("\n-------------")
            horizontal += 1
        i = i + 1
    print("\n")


def toss_():
    global toss
    x = 5
    while x > 0:
        player = input("Who would like to start first(0,X): ")
        player = player.upper()
        print(f"you choose {player}\n")
        if player == 'X':
            toss = 1
            break
        elif player == '0':
            toss = 0
            break
        else:
            print("Invalid Choice\n")


def insert(elem,position):
    global full
    global full_bool
    full_bool = True
    if position == 'a' and (board[0][0] not in sets):
        board[0][0] = elem
    elif position == 'b' and (board[0][1] not in sets):
        board[0][1] = elem
    elif position == 'c' and (board[0][2] not in sets):
        board[0][2] = elem
    elif position == 'd' and (board[1][0] not in sets):
        board[1][0] = elem
    elif position == 'e' and (board[1][1] not in sets):
        board[1][1] = elem
    elif position == 'f' and (board[1][2] not in sets):
        board[1][2] = elem
    elif position == 'g' and (board[2][0] not in sets):
        board[2][0] = elem
    elif position == 'h' and (board[2][1] not in sets):
        board[2][1] = elem
    elif position == 'i' and (board[2][2] not in sets):
        board[2][2] = elem
    else:
        print("Illegal Move!\nChoose again\n")
        full_bool = False
    if full_bool:
        full += 1









def winner_check():
    global board
    #######row####
    i = 0
    while i < 3 :
        list1 = [x for x in board[i]]
        if (list1.count(list1[0]) == len(list1)):
            print(f"Player {list1[0]} is winner!!!\n")
            return True
        i = i + 1
    #######column#####
    i = 0
    list1 = []
    while i < 3:
        j = 0
        while j < 3:
            list1.append(board[j][i])
            j = j + 1
        if (list1.count(list1[0]) == len(list1)):
            print(f"Player {list1[0]} is winner!!!\n")
            return True
        list1 = []
        i = i + 1
    #######diagonal#####
    list1 = []
    i = 0
    j = 0
    while i < 3 and j < 3:
        list1.append(board[i][j])
        i += 1
        j += 1
    if (list1.count(list1[0]) == len(list1)):
            print(f"Player {list1[0]} is winner!!!\n")
            return True
    ######dig2#####
    list1 = []
    i = 0
    j = 2
    while i < 3:
        list1.append(board[i][j])
        i += 1
        j -= 1
    if (list1.count(list1[0]) == len(list1)):
            print(f"Player {list1[0]} is winner!!!\n")
            return True
    ####draw######
    if full >= 9:
        print(f"Match Draw!!!!")
        return True
    return False



def input_board():
    ##toss fucnction to decide who will enter first
    global toss
    global board
    global full
    global full_bool
    toss_()
    display()
    while True:
        if toss % 2 == 0:
            player = '0'
            toss = toss + 1
        else:
            player = "X"
            toss = toss + 1
        print(f"Player {player}:\nEnter the position : ",end=' ')
        position = input().lower()
        insert(player,position)
        print("\n"*100)
        display()
        if(winner_check()):
            print("\nPlay Again(y or n):",end=' ')
            decide = input().lower()
            print("\n")
            if decide == 'y':
                board = [['A','B','C'],['D','E','F'],['G','H','I']]
                toss = 0
                full = 0
                full_bool = True
                continue
            else:
                break



input_board()


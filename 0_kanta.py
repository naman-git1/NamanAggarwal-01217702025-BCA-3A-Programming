



def board(xT,yT):
    print(f"{'X' if xT[0] else('O' if yT[0] else 0)} | {'X' if xT[1] else('O' if yT[1] else 1)} | {'X' if xT[2] else('O' if yT[2] else 2)}")
    print(f"---------")
    print(f"{'X' if xT[3] else('O' if yT[3] else 3)} | {'X' if xT[4] else('O' if yT[4] else 4)} | {'X' if xT[5] else('O' if yT[5] else 5)}")
    print(f"---------")
    print(f"{'X' if xT[6] else('O' if yT[6] else 6)} | {'X' if xT[7] else('O' if yT[7] else 7)} | {'X' if xT[8] else('O' if yT[8] else 8)}")
def check_win(xT,yT):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for element in wins:
        if (xT[element[0]] + xT[element[1]] + xT[element[2]]) == 3:
            return 1
        if (yT[element[0]] + yT[element[1]] + yT[element[2]]) == 3:
            return 2



turn = 1
xstate = [0,0,0,0,0,0,0,0,0]
ystate = [0,0,0,0,0,0,0,0,0]
print("welcome to tic tac toe")
while True:
    board(xstate,ystate)
    if turn == 1:
        print("X turn")
        value = int(input("choose a position on board : "))
        xstate[value] = 1
        turn -= 1
    else:
        print("Y turn")
        value = int(input("choose a position on board : "))
        ystate[value] = 1
        turn += 1
    end_game = check_win(xstate,ystate)
    if end_game == 1 :
        print("x WINS")
        break
    elif end_game == 2 :
        print("y WINS")
        break


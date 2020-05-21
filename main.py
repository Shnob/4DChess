board = []

SIZE = 4

def makeClearBoard():
    global SIZE
    global board

    board = []
	
    for x in range(SIZE):
        board.append([])
        for y in range(SIZE):
            board[x].append([])
            for w in range(SIZE):
                board[x][y].append([])
                for z in range(SIZE):
                    #print("{} {} {} {}".format(x,y,w,z))
                    square = 0
                    board[x][y][w].append(square)
					
def textBoard():
    for z in range(len(board[0][0][0])):
        print("-----------------------------------------------------")
        #print("\n\n")
        for y in range(len(board[0])):
            line = ""
            for w in range(len(board[0][0])):
                line += "|"
                for x in range(len(board)):
                    curr = str(board[x][y][w][z])
                    line += curr
                    line += " " * (3 - len(curr))
            line += "|"
            print(line)
    print("-----------------------------------------------------")

def distanceFrom

makeClearBoard()
textBoard()
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
                    square = "_"
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

def distanceFrom(s1, s2):
    dist = abs(s1[0] - s2[0]) + abs(s1[1] - s2[1]) + abs(s1[2] - s2[2]) + abs(s1[3] - s2[3])
    return dist

def testFunc():
    global board
    for x in range(len(board)):
        for y in range(len(board[0])):
            for w in range(len(board[0][0])):
                for z in range(len(board[0][0][0])):
                    #board[x][y][w][z] = distanceFrom((x, y, w, z), (1, 1, 1, 1))
                    if abs(x - 1) <= 1 and abs(y - 1) <= 1 and abs(w - 1) <= 1 and abs(z - 1) <= 1:
                        board[x][y][w][z] = 1
                        if distanceFrom((x, y, w, z), (1, 1, 1, 1)) == 0:
                            board[x][y][w][z] = "K"

makeClearBoard()
testFunc()
textBoard()
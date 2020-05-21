board = []

SIZE = 5

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
                    square = "."
                    board[x][y][w].append(square)
					
def textBoard():
    for z in range(len(board[0][0][0])):
        print("-" * (SIZE*SIZE*3+SIZE+1))
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
    print("-" * (SIZE*SIZE*3+SIZE+1))

def distanceFrom(s1, s2):
    dist = 0
    for i in range(len(s1)):
        dist += abs(s1[i] - s2[i])
    return dist

def queenFunc(s1, s2):
    dim = []

    for i in range(len(s1)):
        if s1[i] - s2[i] != 0:
            dim.append(abs(s1[i] - s2[i]))

    if len(dim) == 0:
        return False
    if len(dim) == 1:
        return True
    
    n = dim[0]

    for i in range(1, len(dim)):
        if dim[i] != n:
            return False
    return True

def nD1(s1, s2, n):
    dim = []

    for i in range(len(s1)):
        if s1[i] - s2[i] != 0:
            dim.append(abs(s1[i] - s2[i]))

    if n != len(dim):
        return False
    if len(dim) == 0:
        return False
    if len(dim) == 1:
        return True
    
    n = dim[0]

    for i in range(1, len(dim)):
        if dim[i] != n:
            return False
    return True

testFocus = (2, 2, 2, 2)

def testFunc():
    global board
    n = 0
    board[testFocus[0]][testFocus[1]][testFocus[2]][testFocus[3]] = "F"
    for x in range(len(board)):
        for y in range(len(board[0])):
            for w in range(len(board[0][0])):
                for z in range(len(board[0][0][0])):
                    #board[x][y][w][z] = distanceFrom((x, y, w, z), (2, 2, 2, 2))
                    #if abs(x - 2) <= 1 and abs(y - 2) <= 1 and abs(w - 2) <= 1 and abs(z - 2) <= 1:
                    #    board[x][y][w][z] = 1
                    #    if distanceFrom((x, y, w, z), (2, 2, 2, 2)) == 0:
                    #        board[x][y][w][z] = "K"
                    if nD1((x, y, w, z), testFocus, 2):
                        n += 1
                        board[x][y][w][z] = "#"
    print(n)

makeClearBoard()
testFunc()
textBoard()
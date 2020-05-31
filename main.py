import copy

board = []

SIZE = 4

class Piece():
    def __init__(self, empty, team, mvmt):
        self.team = team
        self.mvmt = mvmt
        self.empty = empty

    def display(self):
        if self.empty:
            return "."
        if self.team == 0:
            return "0"
        if self.team == 1:
            return "1"
        

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
                    square = Piece(True, None, None)
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
                    curr = str(board[x][y][w][z].display())
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

def nD2(s1, s2, n):
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
                    if nD2((x, y, w, z), testFocus, 1):
                        n += 1
                        board[x][y][w][z] = "#"
    print(n)

def mvmt_1D1(pCurr, pCheck):
    n = 0
    for i in range(len(pCurr)):
        a = abs(pCurr[i] - pCheck[i])
        if a > 1:
            return False
        if a == 1:
            n += 1
    
    if n == 1:
        return True

score = [0, 0]

def setupBoard():
    global board

    for x in range(len(board)):
        for y in range(len(board[0])):
            for w in range(len(board[0][0])):
                for z in range(len(board[0][0][0])):
                    if x < 2 and w == 0:
                        board[x][y][w][z] = Piece(False, 0, mvmt_1D1)
                        score[0] += 1
                    if x > 1 and w == 3:
                        board[x][y][w][z] = Piece(False, 1, mvmt_1D1)
                        score[1] += 1
                        

makeClearBoard()
setupBoard()

turn = 0
game = True

while game:
    while True:
        if score[0] < 1 or score[1] < 1:
            game = False
            break

        textBoard()
        print("Turn: {}   Scores:   {}   {}".format(turn, score[0], score[1]))

        inp = input().split()
        if len(inp) != 8:
            print("incorrect input length")
            continue
        pCurr = (int(inp[0]), int(inp[1]), int(inp[2]), int(inp[3]))
        pCheck = (int(inp[4]), int(inp[5]), int(inp[6]), int(inp[7]))

        curr = board[pCurr[0]][pCurr[1]][pCurr[2]][pCurr[3]]
        check = board[pCheck[0]][pCheck[1]][pCheck[2]][pCheck[3]]

        if curr.empty == True:
            print("curr empty")
            continue
        if curr.team != turn:
            print("piece wrong team")
            continue
        if not curr.mvmt(pCurr, pCheck):
            print("illegal move")
            continue
        if check.empty == False:
            if check.team == curr.team:
                print("can't move ontop of self")
                continue
            score[(turn + 1) % 2] -= 1
        board[pCheck[0]][pCheck[1]][pCheck[2]][pCheck[3]] = copy.copy(curr)
        board[pCurr[0]][pCurr[1]][pCurr[2]][pCurr[3]] = Piece(True, None, None)
        
        print(check)
        print(board[pCheck[0]][pCheck[1]][pCheck[2]][pCheck[3]])

        print("done")
        break

    turn = (turn + 1) % 2

if score[0] < 1:
    print("0 Wins")
else:
    print("1 Wins")

input("Press Any Key...")
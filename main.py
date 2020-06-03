import pygame, time, sys, math

import copy

pygame.init()
pygame.display.set_caption('4D Peasants')
screen = pygame.display.set_mode((555,585))

board = []

SIZE = 4

class Piece():
    def __init__(self, empty, team, mvmt):
        self.team = team
        self.mvmt = mvmt
        self.empty = empty
        self.marked = 0

    def display(self):
        if self.empty:
            return "."
        if self.team == 0:
            return "0"
        if self.team == 1:
            return "1"
        
def mapFromTo(x,a,b,c,d):
   y=(x-a)/(b-a)*(d-c)+c
   return y

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

def clearMarked():
    for z in range(len(board[0][0][0])):
        for y in range(len(board[0])):
            for w in range(len(board[0][0])):
                for x in range(len(board)):
                    board[x][y][w][z].marked = False

def textBoard():
    for z in range(len(board[0][0][0])):
        print("-" * (SIZE*SIZE*2+SIZE+1))
        #print("\n\n")
        for y in range(len(board[0])):
            line = ""
            for w in range(len(board[0][0])):
                line += "|"
                for x in range(len(board)):
                    curr = str(board[x][y][w][z].display())
                    line += curr
                    line += " " * (2 - len(curr))
            line += "|"
            print(line)
    print("-" * (SIZE*SIZE*2+SIZE+1))

def drawBoard():
    screen.fill((0, 0, 0))
    offsety = 15
    for z in range(len(board[0][0][0])):
        for y in range(len(board[0])):
            offsetx = 15
            for w in range(len(board[0][0])):
                for x in range(len(board)):
                    colour = (255, 255, 255)

                    if not board[x][y][w][z].empty:
                        if board[x][y][w][z].team == 0:
                            colour = (255, 50, 50)
                        else:
                            colour = (50, 50, 255)

                    if board[x][y][w][z].marked == 0:
                        pygame.draw.rect(screen, colour, (offsetx + 30 * x, offsety + 30 * y, 28, 28))
                    elif board[x][y][w][z].marked == 1:
                        pygame.draw.rect(screen, colour, (offsetx + 30 * x, offsety + 30 * y, 28, 28))
                        pygame.draw.rect(screen, (0, 0, 0), (offsetx + 30 * x + 10, offsety + 30 * y + 10, 10, 10))
                    else:
                        #pygame.draw.rect(screen, (50, 50, 50), (offsetx + 30 * x, offsety + 30 * y, 28, 28))
                        pygame.draw.rect(screen, colour, (offsetx + 30 * x + 4, offsety + 30 * y + 4, 20, 20))
                    
                    if turn == 0 :
                        pygame.draw.rect(screen, (255, 255, 255), (15, 575, 254, 4))
                    else:
                        pygame.draw.rect(screen, (255, 255, 255), (15 + 15 + 255, 575, 254, 4))

                    pygame.draw.rect(screen, (50, 50, 50), (15, 555, 254, 15))
                    pygame.draw.rect(screen, (255, 50, 50), (15, 555, mapFromTo(score[0]/32, 0, 1, 0, 254), 15))

                    pygame.draw.rect(screen, (50, 50, 50), (15 + 15 + 255, 555, 254, 15))
                    pygame.draw.rect(screen, (50, 50, 255), (15 + 15 + 255 + mapFromTo(score[1]/32, 0, 1, 254, 0), 555, mapFromTo(score[1]/32, 0, 1, 0, 254), 15))

                offsetx += 15 + 30 * SIZE
        offsety += 15 + 30 * SIZE


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
                        
def checkClick(pos):
    w = mapFromTo(pos[0], 15, 540, 0, 4)
    z = mapFromTo(pos[1], 15, 540, 0, 4)
    if w > 0 and w < 4 and z > 0 and z < 4:
        offsetx = 15 + 135 * math.floor(w)
        offsety = 15 + 135 * math.floor(z)
        x = mapFromTo(pos[0], offsetx, offsetx + 30*4, 0, 4)
        y = mapFromTo(pos[1], offsety, offsety + 30*4, 0, 4)
        return (math.floor(x), math.floor(y), math.floor(w), math.floor(z))

def markPossible(pos):
    piece = board[pos[0]][pos[1]][pos[2]][pos[3]]
    piece.marked = 2
    for x in range(len(board)):
        for y in range(len(board[x])):
            for w in range(len(board[x][y])):
                for z in range(len(board[x][y][w])):
                    if piece.mvmt((pos[0],pos[1],pos[2],pos[3]), (x, y, w, z)):
                        check = board[x][y][w][z]
                        if check.team != piece.team:
                            board[x][y][w][z].marked = True


makeClearBoard()
setupBoard()

turn = 0

game = False

turn = 0
turnType = 0

selPos = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print(event.pos)
            pos = checkClick(event.pos)
            piece = board[pos[0]][pos[1]][pos[2]][pos[3]]
            if turnType == 0:
                if piece.team == turn:
                    markPossible(pos)
                    selPos = pos
                    turnType = (turnType + 1) % 2
            else:
                if piece.marked == 1:
                    if not piece.empty:
                        score[(turn+1)%2] -= 1
                    board[pos[0]][pos[1]][pos[2]][pos[3]] = copy.copy(board[selPos[0]][selPos[1]][selPos[2]][selPos[3]])
                    board[selPos[0]][selPos[1]][selPos[2]][selPos[3]] = Piece(True, None, None)
                    clearMarked()
                    turnType = (turnType + 1) % 2
                    turn = (turn + 1) % 2

    drawBoard()
    pygame.display.update()
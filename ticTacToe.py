import pygame
from pygame.locals import *

pygame.init()

#Screen Width and Height:
screenWidth = 600
screenHeight = 600

#Game Screen:
screen = pygame.display.set_mode(( screenWidth, screenHeight))

#Colors:
green = (0,250,0)
red = (250,0,0)
blue = (0,142,204)
black = (0,0,0)
beige = (245,245,220)
white = (250, 250, 250)

#Font: 
font =  pygame.font.SysFont("Times New Roman", 50, True, False)

#Line Width:
lineWidth = 15

#Board:
board = [[0,0,0],[0,0,0],[0,0,0]]

#Game Control variables:
global winner
global gameOver
winner = 0
gameOver = False
gameOn = True
currentPlayer = 1
currentRound = 0
againBox = Rect(150, 300, 300, 100)
click = False

#Display Board:
def displayBoard():
    screen.fill(beige)
    for i in range (1,3):
        #Horizontal lines:
        pygame.draw.line(screen, black, (0,i * 200), (600, i * 200), lineWidth)
        #Vertical lines:
        pygame.draw.line(screen, black, (i * 200, 0), (i * 200, 600), lineWidth)

#Display moves:
def displayMoves():
    currentRow = 0
    for row in board:
        currentBox = 0
        for box in row:
            if (box == 1):
                pygame.draw.line(screen, red, (currentRow * 200 + 30, currentBox * 200 + 30),(currentRow * 200 + 170, currentBox *200 + 170), lineWidth)
                pygame.draw.line(screen, red, (currentRow * 200 + 170, currentBox * 200 + 30),(currentRow * 200 + 30, currentBox * 200 +170), lineWidth)
            if (box == -1):
                pygame.draw.circle(screen, blue, (currentRow * 200 + 100, currentBox * 200 + 100), 76, lineWidth)
            currentBox += 1
        currentRow += 1

#Checking result after each round:
def checkWin(player):
    global winner
    global gameOver
    for i in range(0,2):
        #checking rows:
        if (sum(board[i]) == player * 3):
            winner = player
            gameOver = True
        #checking columns:
        if (board[0][i] + board[1][i] + board [2][i] == player * 3):
            winner = player
            gameOver = True
    #Checking diagonals:
    if (board[0][0] + board[1][1] + board[2][2] == 3*player or board[0][2] + board[1][1] + board[2][0] == 3*player):
        winner = player
        gameOver = True

#Display Game Ending:
def displayEnd(winner):
    if (winner == 0):
        endingText = "Game is Tied"
    if (winner == 1):
        endingText = "Player 1 Won!"
    if (winner == -1):
        endingText = "Player 2 Won!"
    #Result message
    endingImg = font.render(endingText, True, black)
    pygame.draw.rect(screen, green, (100, 180, 400, 100))
    screen.blit(endingImg,(150, 200))
    #Play again option
    againText = "Reset"
    againImg = font.render(againText, True, black)
    pygame.draw.rect(screen, white, againBox)
    screen.blit(againImg, (230,320))

while (gameOn == True):
    displayBoard()
    displayMoves()        
                
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
        if event.type == pygame.MOUSEBUTTONDOWN and (click == False):
            click = True
        if event.type == pygame.MOUSEBUTTONDOWN and (click == True):
            click = False
            currentPosition = pygame.mouse.get_pos()
            currentX = currentPosition[0] // 200
            currentY = currentPosition[1] // 200

            if board[currentX][currentY] == 0:
                board[currentX][currentY] = currentPlayer
                currentRound += 1  
                checkWin(currentPlayer) 
                currentPlayer *= -1  
                #check for tie
                if (currentRound == 9 and winner == 0):
                    gameOver = True
    if gameOver == True:
        displayEnd(winner)
        if event.type == pygame.MOUSEBUTTONDOWN and (click == False):
            click = True
        if event.type == pygame.MOUSEBUTTONDOWN and (click == True):
            click = False
            currentPosition = pygame.mouse.get_pos()
            if againBox.collidepoint(currentPosition):
                gameOver = False
                currentPlayer = 1
                currentPosition = (0,0)
                winner = 0
                board = [[0,0,0],[0,0,0],[0,0,0]]
                currentRound = 0
    pygame.display.update()
pygame.quit()

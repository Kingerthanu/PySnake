import sys
import pygame
import random

SCREEN = pygame.display.set_mode((900,900))
SCREEN.fill(pygame.Color("White"))
pygame.display.set_caption("PySnake")
pygame.init()
squareSize = 45
LASTSPOT = tuple()
moveEvent = pygame.USEREVENT+1
pygame.time.set_timer(moveEvent, 100)
DIRECTION = "D"
listOfBerries = []
class Strawberry:
    def __init__(self):
        self.x = int(random.randint(0, 19)*squareSize)
        self.y = int(random.randint(0, 19)*squareSize)
        self.StrawBerryObj = pygame.Rect(self.x, self.y, squareSize,squareSize)
        self.renderBerry()
    def renderBerry(self):
        pygame.draw.rect(SCREEN, pygame.Color("Red"), self.StrawBerryObj)
class Snake:
    def __init__(self):
        self.SnakeBody = [pygame.Rect(3*squareSize, 3*squareSize, squareSize,squareSize), pygame.Rect(3*squareSize, 2*squareSize, squareSize,squareSize),pygame.Rect(3*squareSize, 1*squareSize, squareSize,squareSize)]      
        self.xDir = 0
        self.yDir = 0
    def createPosition(self):
        HOSTx = self.SnakeBody[0].x
        HOSTy = self.SnakeBody[0].y
        if DIRECTION == "U":
                self.SnakeBody[0].x += self.xDir *squareSize
                self.SnakeBody[0].y += self.yDir *squareSize
                if self.SnakeBody[0].y < 0:
                    self.SnakeBody[0].y = 855
        elif DIRECTION == "D":
                self.SnakeBody[0].x += self.xDir *squareSize
                self.SnakeBody[0].y += self.yDir *squareSize
                if self.SnakeBody[0].y > 855:
                    self.SnakeBody[0].y = 0
        elif DIRECTION == "L":
            self.SnakeBody[0].x += self.xDir *squareSize
            if self.SnakeBody[0].x < 0:
                    self.SnakeBody[0].x = 855
        elif DIRECTION == "R":
            self.SnakeBody[0].x += self.xDir *squareSize
            if self.SnakeBody[0].x > 855:
                    self.SnakeBody[0].x = 0
        for ber in listOfBerries:
         if self.SnakeBody[0].x == ber.x and self.SnakeBody[0].y == ber.y:
            del ber
            listOfBerries.pop(0)
            self.SnakeBody.append(pygame.Rect(-50, -50, squareSize,squareSize))
            listOfBerries.append(Strawberry())
        for ind,each in enumerate(self.SnakeBody[1:]):
            if each.x == self.SnakeBody[0].x and each.y == self.SnakeBody[0].y:
                self.SnakeBody = self.SnakeBody[:3]
            OLDHOSTx = each.x
            OLDHOSTy = each.y
            each.x = HOSTx
            each.y = HOSTy
            HOSTx = OLDHOSTx
            HOSTy = OLDHOSTy
        SNAKE_ENTITY.repaintSnake()
    def move(self):
        if DIRECTION == "D" and self.yDir != -1:
             self.xDir = 0
             self.yDir = 1
        elif DIRECTION == "U" and self.yDir != 1:
            self.xDir = 0
            self.yDir = -1
        elif DIRECTION == "R" and self.xDir != -1:
            self.xDir = 1
            self.yDir = 0
        elif DIRECTION == "L" and self.xDir != 1:
            self.xDir = -1
            self.yDir = 0
        self.createPosition()
    def repaintSnake(self):
        SCREEN.fill("Black")
        for each in self.SnakeBody:
            pygame.draw.rect(SCREEN, pygame.Color("Green"), each)
        for berry in listOfBerries:
         pygame.draw.rect(SCREEN, pygame.Color("Red"), berry.StrawBerryObj)
SNAKE_ENTITY = Snake()
STRAWBERRY_ENTITY = Strawberry()
listOfBerries.append(STRAWBERRY_ENTITY)
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                DIRECTION = "U"
            elif event.key == pygame.K_DOWN:
                DIRECTION = "D"
            elif event.key == pygame.K_RIGHT:
                DIRECTION = "R"
            elif event.key == pygame.K_LEFT:
                DIRECTION = "L"
        elif event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == moveEvent:
            SNAKE_ENTITY.move()
    pygame.display.update()

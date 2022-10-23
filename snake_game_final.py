
from tkinter import *
import random


###CONSTANTS CLASS

class Cons:

    BACKGROUND_COLOR = "#283030"
    SNAKE_HEAD_COLOR = "#550885"
    SNAKE_BODY_COLOR = "E6E6FA"

    STARTING_SEGMENT_NUMBER = 3

    POISONED_SNAKE_HEAD_COLOR = "#cc2978"
    POISONED_SNAKE_BODY_COLOR = "#bd7209"

    APPLE_COLOR = "#FF0000"
    POISON_APPLE_COLOR = "#11ff00"

    POISON_PERCENTAGE_CHANCE = 15 ##IN PERCENT CHANCE OF FOOD BEING "POISON"

    FONT_COLOR = "#8c8c8c"
    FONT = "century"
    FONT_SIZE = 30

    BOARD_HEIGHT = 500
    BOARD_WIDTH = 500
    TILE_SIZE = 10



    TEXT_TITLE = "Snake Game"
    TEXT_GAMEOVER = "Game Over"
    TEXT_SCORE = "Score: "

    SPEED = 200 #tick rate in milliseconds

    DIRECTIONS = ( "up", "down", "left", "right", "STATIONARY" )

class Node:
    def __init__(self, value=None):
        self.value = value
        self.nextNode = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        elif self.tail:
            self.tail.nextNode = new_node
            self.tail = new_node
        else:
            self.head.nextNode = new_node
            self.tail = new_node

    def append(self, new_data):
 
        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)
 
        # 4. If the Linked List is empty, then make the
        #    new node as head
        if self.head is None:
            self.head = new_node
            return
 
        # 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next
 
        # 6. Change the next of last node
        last.next =  new_node



linkedList = LinkedList()

for num in range(1,101):

    linkedList.insert(randint(1,99))


print(linkedList)

print(linkedList.tail)

    


class Food:



    def __init__(self):

        x = random.randomint((0, (Cons.BOARD_WIDTH / Cons.TILE_SIZE ) -1) * Cons.TILE_SIZE)

        y = random.randint((0, (Cons.BOARD_WIDTH / Cons.TILE_SIZE) -1) * Cons.TILE_SIZE)

        self.coordinates = [x,y]


        if Cons.POISON_PERCENTAGE_CHANCE >= random.randrange(1,101):

            #poisoned logic
            Canvas.create_oval(x, y, x+ Cons.TILE_SIZE, y+ Cons.TILE_SIZE, fill= Cons.POISON_APPLE_COLOR, tag= "poison apple")


        else:

            #not poison logic
            Canvas.create_oval(x, y, x+ Cons.TILE_SIZE, y+ Cons.TILE_SIZE, fill= Cons.APPLE_COLOR, tag= "apple")



    def isPoison(poison_percent):

        poisonPercentage = (poison_percent / 100)
        randomPercent = random.random()

        if poisonPercentage >= randomPercent:
            return True

        return False

    def spawnNewFood (coordinates, isPoison):

        x,y = coordinates[0], coordinates[1]


        if isPoison(Cons.POISON_PERCENTAGE_CHANCE) is True:

            Canvas.create_oval(x, y, x+ Cons.TILE_SIZE, y+ Cons.TILE_SIZE, fill= Cons.POISON_APPLE_COLOR, tag= "poison apple")

        else:
            Canvas.create_oval(x, y, x+ Cons.TILE_SIZE, y+ Cons.TILE_SIZE, fill= Cons.APPLE_COLOR, tag= "apple")




#TODO:
# make singly linked list to represent snake
# keep reference to both head and tail of snake
# 
class Snake:

    def __init__ (self):

        self.bodySize = Cons.STARTING_SEGMENT_NUMBER

    class Node:

        def __init__ (self, dataValue = None):
            self.dataValue = dataValue
            self.nextValue = None


    
    class SnakeBody:

        #need to keep a pointer to the tail(last) value
        def __init__ (self):

            self.headValue = None

    snake = SnakeBody
    snake.headValue = Node()
        


    def snake_Growth(currentSnake, nextBodyPiece):

        currentSnake.append(nextBodyPiece)

        ## create reference to "tail" of snake
        return nextBodyPiece







        ##NEED TO CREATE REVERSAL FOOD --Done
        ### PROBABLY JUST NEED TO USED DIFFERENT TAG.. AND DIFFERENT COLOR --Done


                ## HANDLE SNAKE'S REVERASAL IN THE MOVEMENT FUNCTION  (NOT DONE)



def checkCollisions(snake_body):


        ###????
    x,y = snake_body.coordinates[0]

    ''' commenting out collision code, adding to other function (isoutofbounds)
    if x < 0 or x >= Cons.BOARD_WIDTH:
        return True

    elif y < 0 or y > Cons.BOARD_HEIGHT:
        return True
        '''

    for segment in snake_body.length:
        if x == segment[0] and y == segment[1]:
            return True
    
    return False

def isOutOfBounds(snake_body):

    x,y = snake_body.coordinates[0]

    if x < 0 or x >= Cons.BOARD_WIDTH:
        return True

    elif y < 0 or y > Cons.BOARD_HEIGHT:
        return True


def isValidDirection():

    '''
    False if opposite of current direction
    false button pressed is not WASD, or [up, down, left, right]
    otherwise returns true
    '''

    #if button pressed is opposite of currenct direction

    #if button pressed is not valid key



    return True
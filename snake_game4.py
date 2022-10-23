

from termios import PARODD
from tkinter import *
import random




from termios import PARODD
from tkinter import *
import random





class Cons:

    BACKGROUND_COLOR = "#283030"
    SNAKE_HEAD_COLOR = "#550885"
    SNAKE_BODY_COLOR = "E6E6FA"

    POISONED_SNAKE_HEAD_COLOR = "#cc2978"
    POISONED_SNAKE_BODY_COLOR = "#bd7209"

    APPLE_COLOR = "#FF0000"
    POISON_APPLE_COLOR = "#11ff00"

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



class SnakeSegment:

    def __init__(self, data):

        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class SnakeGrowth:

    #NEED A REFERENCE TO THE LAST NODE IN THE LINKED LIST


    def __init__ (self):
        
        self.head = None ###NEEDS FIXED

    def __repr__ (self):

        node = self.head
        nodes = []

        while node is not None:

            nodes.append(node.data)







        #### NEED TO ADD LOGIC FOR RANDOM POISON FOOD PERCENTAGE)   
class Food:


    def __init__(self):

        x = random.randomint((0, (Cons.BOARD_WIDTH / Cons.TILE_SIZE ) -1) * Cons.TILE_SIZE)

        y = random.randint((0, (Cons.BOARD_WIDTH / Cons.TILE_SIZE) -1) * Cons.TILE_SIZE)

        self.coordinates = [x,y]

        Canvas.create_oval(x, y, x+ Cons.TILE_SIZE, y+ Cons.TILE_SIZE, fill= Cons.APPLE_COLOR, tag= "apple")



    


    def checkAppleCollision(self):
            #checks to see if snake head collides with food piece


        apple = self.find_withtag("apple" or "poison apple")

        head = self.find_withtag("head")

        x1,y1, x2,y2 = self.bbox("head")

        overlap = self.find_overlapping(x1,y1, x2,y2)


        for ovr in overlap:

            if apple[0] == ovr:

                pass



class Snake:

    def __init__ (self):

        pass

    class Node:

        def __init__ (self, data):

            self.data = data
            self.next = None


        def __repr__ (self):
            return self.data


    class SinglyLinkedList:

        def __init__(self):

            self.head = None


        def __repr__(self):

            node = self.head
            nodes = []

            while node is not None:

                nodes.append(node.data)
                node = node.next

            nodes.append("None")
                return " ".join(nodes)

        def add_last (self, node):
            if self.head is None:
                self.head = node
                return


            for current_node in self:
                pass

            curret_node.next = node

            


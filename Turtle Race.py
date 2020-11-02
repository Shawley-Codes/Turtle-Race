#Homwrok 7
#Scott Hawley

#libraries used
import random
import turtle
import time

class turtleRace():
    #create turtles
    def __init__(self, col, coll):
        self.col = col
        self.coll = coll
        #create and add a list of colored turtles
        for x in range(len(self.col)):
            print(self.col[x])
            #print(coll[x])
            self.col[x] = turtle.Turtle()
            self.col[x].color(self.coll[x])
            self.col[x].shape('turtle')


        
    #create the board for the game
    def turtleBoard(self):
        #print numbers on turtle board
        turtle.speed(0)
        turtle.pensize(3)
        for s in range(21):
            turtle.write(s)
            turtle.forward(40)
        #turtle will create lines under the numbers
        for x in range(21):
            turtle.penup()
            turtle.forward((x*40)-40)
            turtle.right(90)
            turtle.forward(10)
            turtle.pendown()
            turtle.forward(400)
            turtle.penup()
            turtle.setx(-450)
            turtle.sety(0)
            #if it needs to be turned after returned to home
            turtle.left(90)

    #creates multiple turtles to race across the map
    def turtleCross (self):
        turtle.penup()

        #run through and set up each turtle starting point
        for x in range(len(self.col)):
            self.col[x].penup()
            self.col[x].pensize(4)
            self.col[x].setx(-450)
            self.col[x].right(90)
            self.col[x].forward(100*x + 100)
            self.col[x].left(90)
            self.col[x].speed(3)
            self.col[x].pendown()

        #run through and move each turtles position to race to the end
        noWinner = True
        while noWinner:
            for x in range(len(self.col)):
                #get a random value to move turtle
                distance = random.randint(20,80)
                self.col[x].forward(distance)
                #check if after move turtle wins race, then exit
                if self.col[x].xcor() > 350:
                    noWinner = False

    #initialize basic values
    def initialize(self):
        #seed random function
        random.seed(time.time())
        #set spacing
        window = turtle.Screen()
        turtle.penup()
        turtle.backward(450)
        turtle.pendown()
    
#main function
def main ():
    #create class
    col = ['red', 'blue', 'green']
    coll = ['red', 'blue', 'green']
    game = turtleRace(col, coll)
    game.initialize()
    game.turtleBoard()
    game.turtleCross()

    col2 = ['orange', 'black']
    coll2 = ['orange', 'black']
    game2 = turtleRace(col2,coll2)
    game2.turtleCross()
    
    return

#run main
main()
turtle.done()
    

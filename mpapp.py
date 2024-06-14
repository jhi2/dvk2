import turtle as t
import random as rand
from pathlib import Path
dadpth = f"{Path.cwd()}\\player.gif"
badpth = f"{Path.cwd()}\\bad.gif"
def gotoRandPos(turtle):
    turtle.penup()
    turtle.goto(rand.randint(0,360),rand.randint(0,360))
print("Icon by icons8.com")
screen = t.Screen()
screen.title("Dad vs. the Kaisers")
screen.register_shape(dadpath)
screen.register_shape(badpath)
screen.screensize(360,360)
screen.cv._rootwindow.resizable(False, False)
screen.bgcolor("skyblue")
dad = t.Turtle("player.gif")
bad = t.Turtle(shape="bad.gif")
gotoRandPos(dad)
gotoRandPos(bad)
bad.speed(1)
dad.speed(1)
dadhits = 0
badhits = 0
def shoot(player):
    global dadhits,badhits
    if player == bad:
        hittingPlayer = dad
    else:
        hittingPlayer = bad
    playerX = player.pos()[0]
    hittingPlayerX = hittingPlayer.pos()[0]
    hittingPlayerY = hittingPlayer.pos()[1]
    def determineHit(player):
        hitrightcords = []
        playerleftx = player.pos()[0] - (player.width() / 2)
        hitrightcords.append(playerleftx)
        hitrightcords.append(playerleftx + player.width())
        if player.pos()[0] > hitrightcords[0] and playerX < hitrightcords[1]:
            return True
        else:
            return False
    if determineHit(hittingPlayer):
        fireball = t.Turtle(shape="circle")
        fireball.ht()
        fireball.teleport(player.pos()[0],player.pos()[1])
        fireball.penup()
        fireball.speed(2)
        fireball.st()
        fireball.color("red")
        fireball.goto(hittingPlayerX,hittingPlayerY)
        fireball.ht()
        if hittingPlayer == dad:
            dadhits = dadhits + 1
        if hittingPlayer == bad:
            badhits = badhits + 1
        print(f"Dad:{str(dadhits)} Kaiser:{str(badhits)}\nIcon by Icons8")
        
        
    
        
def up():
    dad.setheading(90)
    dad.forward(100)

def down():
    dad.setheading(270)
    dad.forward(100)

def left():
    dad.setheading(180)
    dad.forward(100)

def right():
    dad.setheading(0)
    dad.forward(100)
def dadShoot():
    shoot(bad)
        
def bup():
    bad.setheading(90)
    bad.forward(100)

def bdown():
    bad.setheading(270)
    bad.forward(100)

def bleft():
    bad.setheading(180)
    bad.forward(100)

def bright():
    bad.setheading(0)
    bad.forward(100)
def badShoot():
    shoot(dad)


        
screen.listen()

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(dadShoot,"space")
screen.onkey(bup, "w")
screen.onkey(bdown, "s")
screen.onkey(bleft, "a")
screen.onkey(bright, "d")
screen.onkey(badShoot,"x")
bad.penup()
dad.penup()

    

screen.mainloop()


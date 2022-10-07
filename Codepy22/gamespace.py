#This Game is build by Nitesh lakra
#This is the First Part:

import turtle
import math
import random

window = turtle.Screen()
window.setup(width=600, height=600)
window.title("Space War Game by Nitesh Lakra")
window.bgcolor("black")

window.tracer(0)

vertex = ((0,15),(-15,0),(-18,5),(-18,-5),(0,0),(18,-5),(18, 5),(15, 0))
window.register_shape("player", vertex)

asVertex = ((0, 10), (5, 7), (3,3), (10,0), (7, 4), (8, -6), (0, -10), (-5, -5), (-7, -7), (-10, 0), (-5, 4), (-1, 8))
window.register_shape("asteroids", asVertex)

#This is the Second Part:

class Game(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)

        self.speed(0)
        self.penup()


def game1(t1, t2):
    x1 = t1.xcor()
    y1 = t1.ycor()
    
    x2 = t2.xcor()
    y2 = t2.ycor()
    
    var1 = math.atan2(y1 - y2, x1 - x2)
    var1 = var1 * 180.0 / 3.14159
    
    return var1


player = Game()
player.color("yellow")
player.shape("player")
player.score = 0

#This is the Third Part

missiles = []
for _ in range(3):
    missile = Game()
    missile.color("white")
    missile.shape("classic")
    missile.speed = 1
    missile.state = "ready"
    missile.hideturtle()
    missiles.append(missile)

board = Game()
board.color("blue")
board.hideturtle()
board.goto(0, 250)
board.write("Score: 0", False, align = "center", font = ("Arial", 24, "normal"))

#This is the Fourth Part

Rock = []

for _ in range(5):   
    asteroids = Game()
    asteroids.color("red")
    asteroids.shape("turtle")

    asteroids.speed  = random.randint(2, 3)/50
    asteroids.goto(0, 0)
    var1 = random.randint(0, 260)
    distance = random.randint(300, 400)
    asteroids.setheading(var1)
    asteroids.fd(distance)
    asteroids.setheading(game1(player, asteroids))
    Rock.append(asteroids)

#This is the Functions for Defence Part

def moveL():
    player.lt(20)
    
def moveR():
    player.rt(20)
    
def fire_missile():
    for missile in missiles:
        if missile.state == "ready":
            missile.goto(0, 0)
            missile.showturtle()
            missile.setheading(player.heading())
            missile.state = "fire"
            break


window.listen()
window.onkey(moveL, "Left")
window.onkey(moveR, "Right")
window.onkey(fire_missile, "space")

#This is the Functioning the Code Part-1

var2 = False
while True:

    window.update()
    player.goto(0, 0)
    

    for missile in missiles:
        if missile.state == "fire":
            missile.fd(missile.speed)
        
        if missile.xcor() > 300 or missile.xcor() < -300 or missile.ycor() > 300 or missile.ycor() < -300:
            missile.hideturtle()
            missile.state = "ready"

    for asteroids in Rock:    
        asteroids.fd(asteroids.speed)
        
        for missile in missiles:
            if asteroids.distance(missile) < 20:
                var1 = random.randint(0, 260)
                distance = random.randint(600, 800)
                asteroids.setheading(var1)
                asteroids.fd(distance)
                asteroids.setheading(game1(player, asteroids))
                asteroids.speed += 0.01
                
                missile.goto(600, 600)
                missile.hideturtle()
                missile.state = "ready"
                
                player.score += 10
                board.clear()
                board.write("Score: {}".format(player.score), False, align = "center", font = ("Arial", 24, "normal"))

    
        #This is the Functioning the Code Part-2

        if asteroids.distance(player) < 20:
            var1 = random.randint(0, 260)
            distance = random.randint(600, 800)
            asteroids.setheading(var1)
            asteroids.fd(distance)
            asteroids.setheading(game1(player, asteroids))
            asteroids.speed += 0.005
            var2 = True
            player.score -= 30
            board.clear()
            board.write("Score: {}".format(player.score), False, align = "center", font = ("Arial", 24, "normal"))
    if var2 == True:
        player.hideturtle()
        missile.hideturtle()
        for a in Rock:
            a.hideturtle()
        board.clear()
        break

window.mainloop()

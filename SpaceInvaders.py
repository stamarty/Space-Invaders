#Space Invaders
#Thanks to Christian Thompson for this tutorial:
#http://christianthompson.com/node/45

import turtle
import os
import math
import random
import winsound

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")

turtle.register_shape("invader.gif")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range (4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 275)
scorestring = "Score: %s " %score
score_pen.write(scorestring, False, align = "left", font = ("Arial", 14, "normal"))
score_pen.hideturtle()

player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()
player.speed(0)
player.setposition(0, -280)
player.setheading(90)

playerSpeed = 15


number_of_enemies = 5
enemies = []

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemySpeed = 2

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("turtle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.setposition(0, -400)
bullet.shapesize(0.50, 0.50)
bullet.hideturtle()

bulletSpeed = 20
bulletState = "ready"

def fire_bullet():
    global bulletState
    if bulletState == "ready":
        bulletState = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

def move_left():
    x = player.xcor()
    x -= playerSpeed
    if x < -285:
        x = -285
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerSpeed
    if x > 285:
        x = 285
    player.setx(x)


turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")


while True:
    for enemy in enemies:
        x = enemy.xcor()
        x += enemySpeed
        enemy.setx(x)

        if enemy.xcor() > 285:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemySpeed *= -1

        if enemy.xcor() < -285:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemySpeed *= -1

        if isCollision(bullet, enemy):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            bullet.hideturtle()
            bulletState = "ready"
            bullet.setposition(0, 400)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            score += 10
            scorestring = "Score: %s " % score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))


        if isCollision(player, enemy):
            enemy.hideturtle()
            print("Game Over")
            break

    if bulletState == "fire":
        y = bullet.ycor()
        y += bulletSpeed
        bullet.sety(y)

    if bullet.ycor() > 280:
        bullet.setposition(0, 400)
        bullet.hideturtle()
        bulletState = "ready"

turtle.mainloop
delay = input("press enter to finish")
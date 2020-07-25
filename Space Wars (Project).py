import turtle
import math
import random

#background
sc=turtle.Screen()
sc.bgcolor("black")
sc.title("SPACE WARS")
sc.bgpic("C:/Users/pranjal/Desktop/Space Wars/bgpic.gif")

#adding enemy & player shape to the screen 
sc.addshape("C:/Users/pranjal/Desktop/Space Wars/player.gif")
sc.addshape("C:/Users/pranjal/Desktop/Space Wars/enemy.gif")

#drawing border
proj=turtle.Turtle()
proj.speed(0)
proj.color("yellow")
proj.penup()
proj.setposition(-700,-350)
proj.pendown()
proj.pensize(5)
proj.fd(1400)
proj.lt(90)
proj.fd(700)
proj.lt(90)
proj.fd(1400)
proj.lt(90)
proj.fd(700)
proj.hideturtle()

#creating player
player=turtle.Turtle()
player.color("red")
player.shape("C:/Users/pranjal/Desktop/Space Wars/player.gif")
player.turtlesize(1.5)
player.penup()
player.speed(10)
player.setposition(0,-330)
player.setheading(90)

playerspeed=20

#creating bullet
bullet=turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed=50

bulletstate="ready"

#creating enemies
number_of_enemies=6
enemies=[]

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())
        
for enemy in enemies:
    enemy.color("green")
    enemy.shape("C:/Users/pranjal/Desktop/Space Wars/enemy.gif")
    enemy.penup()
    x=random.randint(-670,670)
    y=random.randint(150,320)
    enemy.setposition(x,y)
    
enemyspeed=10

#Scores
score="0"

score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.penup()
score_pen.color("white")
score_pen.setposition(-700,360)
write_score="SCORE:"+score
score_pen.pendown()
score_pen.write(write_score,move=False,align="Left",font=("Arial",20,"bold"))
score_pen.hideturtle()

#Game over text
game_over=turtle.Turtle()
game_over.penup()
game_over.color("white")
game_over.setposition(0,0)
game_over.hideturtle()

#defining functions 

#moving player left, right, up and down
def move_left():
    x=player.xcor()
    if x>-670:
        x=x-playerspeed
        player.setx(x)

def move_right():
    x=player.xcor()
    if x<670:
        x=x+playerspeed
        player.setx(x)

def move_up():
    y=player.ycor()
    if y<320:
        y=y+playerspeed
        player.sety(y)

def move_down():
    y=player.ycor()
    if y>-320:
        y=y-playerspeed
        player.sety(y)
    
        
#firing bullets
def fire_bullet():
    global bulletstate
    if bulletstate=="ready":
        bulletstate="fire"
        x=player.xcor()
        y=player.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle()

#collision checking
def collision_happens(a,b):
    distance=math.sqrt(math.pow((a.xcor()-b.xcor()),2)+math.pow((a.ycor()-b.ycor()),2))
    if distance<60:
        return True
    else:
        return False


#keyboard bindings
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(move_up,"Up")
turtle.onkey(move_down,"Down")
turtle.onkey(fire_bullet,"space")


#main loop of the game
while True:
    for enemy in enemies:
        x=enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)

        #moving the enemy
        if enemy.xcor()>670 or enemy.xcor()<-670:
            for i in enemies:
                y=i.ycor()
                y-=40
                i.sety(y)
            enemyspeed*=-1
    
        if enemy.ycor()<-330:
            enemy.hideturtle()
            x=random.randint(-670,670)
            y=random.randint(150,320)
            enemy.setposition(x,y)
            enemy.showturtle()
            

        #collision checking between enemy & bullet              
        if collision_happens(bullet,enemy):
            bullet.hideturtle()
            bulletstate="ready"
            bullet.setposition(-750,360)

            enemy.hideturtle()
            x=random.randint(-670,670)
            y=random.randint(150,320)
            enemy.setposition(x,y)
            enemy.showturtle()

            #updating score
            s=eval(score)
            s=s+10
            score=str(s)
            write_score="SCORE:"+score
            score_pen.clear()
            score_pen.write(write_score,move=False,align="Left",font=("Arial",20,"bold"))
            score_pen.hideturtle()
            
       
    #moving bullet
    y=bullet.ycor()
    y+=bulletspeed
    bullet.sety(y)
       
    #border checking bullet
    if bullet.ycor()>330:
        bullet.hideturtle()
        bulletstate="ready"

 

    #collision checking between player & enemy
    if collision_happens(player,enemy):
        enemy.hideturtle()
        player.hideturtle()
        game_over.write("GAME OVER",move=False,align="center",font=("Arial",30,"bold"))
        game_over.hideturtle()
        break


#bibliography
#Christian Thompson, youtube.com
#Programmers' Colloqouy, youtube.com
#Zamzar.com, file conversion
#resizeimage.net, Online Image Resizer
#kindpng.com
#pixabay.com    





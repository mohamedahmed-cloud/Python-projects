import turtle
screen = turtle.Screen()
screen.setup(800, 600)
screen.title("Ping pong Game Uisng Python")
screen.tracer(0)

turtle.bgcolor("black") 
# first  rod1
rod1 = turtle.Turtle()
rod1.shape("square")
rod1.shapesize(stretch_wid = 5, stretch_len = 1)
rod1.speed(0)
rod1.color('red')
rod1.penup()
x = -screen.window_width() // 2
rod1.goto( x + 35, 0)


# second rod
rod2 = turtle.Turtle()
rod2.shape("square")
rod2.shapesize(stretch_len = 1, stretch_wid= 5)
rod2.color("blue")
rod2.speed(0)
rod2.penup()
x = rod2.screen.window_width() // 2
rod2.goto( x - 35, 0)


# ball 
ball = turtle.Turtle()
ball.shape('square')
ball.speed(0)
ball.color("#fff")
ball.penup()
ball.goto(0, 0)
old = 0
ball.dx = 2
ball.dy = 2
# player in the screen
playerCounter = [0,0]

player1 = turtle.Turtle()
player1.color("white")
player1.hideturtle()
player1.penup()
player1.goto(-200, screen.window_height()  // 2 - 50)
player1.write(f"Player 1 Score : {playerCounter[0]}",font=("Arial", 20, "normal"))

player2 = turtle.Turtle()
player2.color('white')
player2.hideturtle()
# player2.penup()
player2.penup()
player2.goto(50,screen.window_height()  // 2 - 50)
player2.write(f"Player 1 Score : {playerCounter[0]}",font=("Arial", 20, "normal"))




def detectScreenSize():
    global old
    new= screen.window_width()
    if new != old:
        # rod 1
        x = -screen.window_width() // 2
        rod1.goto( x + 35, 0)
        rod1.shapesize(stretch_len = 1, stretch_wid= screen.window_height() // 90)
        # rod 2
        x = rod2.screen.window_width() // 2
        rod2.goto( x - 35, 0)
        rod2.shapesize(stretch_len = 1, stretch_wid= screen.window_height() // 90)

    old = new
    turtle.ontimer(detectScreenSize, 100)
detectScreenSize()

def rod1Up():
    rod1.sety(rod1.ycor() + 20) 
def rod1Down():
    rod1.sety(rod1.ycor() - 20)
def rod2Up():
    rod2.sety(rod2.ycor() + 20)
def rod2Down():
    rod2.sety(rod2.ycor() - 20)

# listen & call
screen.listen()
screen.onkeypress(rod1Up, 'w')
screen.onkeypress(rod1Down, 's')
screen.onkeypress(rod2Up, 'Up')  
screen.onkeypress(rod2Down, 'Down') 


def updateBall():
    global ball
    global playerCounter
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if screen.window_height() < abs(ball.ycor()) * 2 + 20:
        ball.dy *= -1
    if screen.window_width() < abs(ball.xcor()) * 2 + 20:
        ball.sety(0)
        ball.setx(0)
        playerCounter = [0,0]
        ball.dx *= -1
    
    t1 = rod1.shapesize()

    if ball.dx < 0 and ball.distance(rod1) < 40:
        ball.dx *= -1
        playerCounter[0] += 1 
        player1.write(f"Player 1 Score : {playerCounter[0]}",font=("Arial", 20, "normal"))



    t2 = rod2.shapesize()
    if ball.dx > 0 and ball.distance(rod2) < 40:
            ball.dx *= -1
            playerCounter[1] += 1
            player2.write(f"Player 1 Score : {playerCounter[0]}",font=("Arial", 20, "normal"))


    turtle.update()
    turtle.ontimer(updateBall, 10)

updateBall()
turtle.done()





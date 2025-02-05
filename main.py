from  turtle import Turtle,Screen
import random

#number of turtles in the game ...

# list of color in turtle....




screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bate", prompt="enter your colour that turtle going to win the colours are red/blue/green/yellow/purple/pink")
colour = ["red", "blue", "green", "yellow", "purple", "pink"]
y_possiotion = [-70,-40,-10,20,50,80]
all_turtle = []

def starting(turtle_list, user_bets):
    for index_turtle in range(0, 6):
        new_turtle = Turtle("turtle")
        new_turtle.penup()
        new_turtle.color(colour[index_turtle])
        new_turtle.goto(x=-230,y=y_possiotion[index_turtle])
        turtle_list.append(new_turtle)
    if user_bet:
        turtle_on = True
        while turtle_on:
            for turtle in all_turtle:
                if turtle.xcor() > 230:
                    winning_colour = Turtle.pencolor(turtle)
                    if winning_colour == user_bets:
                        print(f"{winning_colour} wins!")
                    else:
                        print(f"{user_bet} loss /{winning_colour} wins!")
                        turtle_on = False
                rand_distance = random.randint(1,10)
                turtle.forward(rand_distance)

starting(all_turtle,user_bet)

screen.exitonclick()
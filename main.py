import turtle
import random

screen = turtle.Screen()
screen.title("Turtle Race!")

turtle1 = turtle.Turtle(shape="turtle")
turtle2 = turtle.Turtle(shape="turtle")

turtle1.penup()
turtle1.color("red")
turtle1.goto(-300,-20)
turtle1.pendown()

turtle2.penup()
turtle2.color("purple")
turtle2.goto(-300,20)
turtle2.pendown()

while turtle1.xcor() < 300 and turtle2.xcor() < 300:
    turtle1.forward(random.randint(1,10))
    turtle2.forward(random.randint(1,10))
    
if turtle1.xcor() > turtle2.xcor():
    print("Red turtle Wins!")
elif turtle1.xcor() < turtle2.xcor():
    print("Purple turtle wins")
else:
    print("It's Tie!")


screen.exitonclick()
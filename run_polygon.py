from polygon import *
from turtle import Turtle

def main():
    t = Turtle()
    t.pencolor("blue")
    t.hideturtle()
    radialPattern(t, 10, 50, shape = square)

    # Keep the window open until it is closed by the user
    t.getscreen().exitonclick()

if __name__ == "__main__":
    main()

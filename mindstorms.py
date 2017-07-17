import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("blue")

    turt = turtle.Turtle()
    turt.shape("turtle")
    turt.color("red")
    turt.speed(100)

    for y in range(0,40):
        for x in range(0,4):
            turt.forward(100)
            turt.right(60)
            turt.forward(100)
            turt.right(120)

        turt.right(10)

    #draw_circle()

    window.exitonclick()

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("yellow")
    angie.circle(100)
    draw_triangle()


def draw_triangle():
    bob = turtle.Turtle()
    bob.shape("triangle")
    bob.color("green")
    bob.speed(1)

    for x in range(0,3):
        bob.forward(60)
        bob.left(120)


draw_square()

import turtle


def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)


def koch_snowflake(t, length, level):
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)


def main():
    level = int(input("Enter the level of recursion: "))
    length = 300

    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    t = turtle.Turtle()
    t.speed(0)

    t.penup()
    t.goto(-length / 2, length / (2 * (3**0.5)))
    t.pendown()

    koch_snowflake(t, length, level)

    turtle.done()


if __name__ == "__main__":
    main()

import turtle

t = turtle.Turtle()
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i in items:
    t.circle(10 * i)
    t.penup()
    t.right(90)

    t.pendown()

turtle.done()
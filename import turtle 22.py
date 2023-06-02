import turtle
t = turtle.Turtle()
for i in range (180):
    t.speed(0)
    t.color('#F2D8D8')
    t.circle(190 - i,90)
    t.left(90)
    t.color('#30A2FF')
    t.circle(190 - i,90)
    t.left(18)

import turtle as t
import random as rd

t.speed(100)
t.Screen().bgcolor('black')
t.hideturtle()
color = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']  # 6


def star(x, y):
    t.up()
    t.setpos(x, y)

    t.fillcolor(rd.choice(color))
    t.begin_fill()
    for i in range(5):
        t.forward(40)
        t.left(144)
    t.end_fill()
    pass


t.Screen().listen()
t.Screen().onclick(star)

t.mainloop()

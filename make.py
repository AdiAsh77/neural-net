import turtle
t = turtle.Turtle()
wn = turtle.Screen()
wn.title("ARMPIT")

def Home():
    t.pu()
    t.home()
    t.bk(170)
    t.lt(90)
    t.bk(50)

t.speed(10)

t.pu()
t.bk(170)
t.lt(90)
t.bk(50)
t.pd()

t.fillcolor("#ffdab3")
t.begin_fill()

t.lt(10)
for i in range(10):
    t.fd(40)
    t.lt(2)
t.fd(5)
t.lt(2)

t.end_fill()
Home()
t.begin_fill()

t.bk(100)
t.lt(90)
t.fd(260)
t.pd()
t.rt(90)
t.lt(20)
for i in range(5):
    t.fd(40)
    t.rt(3)
t.lt(3)
t.fd(200)
t.pu()
t.rt(75)
t.fd(223)

t.end_fill()
Home()
t.begin_fill()

t.bk(100)
t.lt(90)
t.fd(260)
t.pd()
t.rt(95)
t.pu()

for i in range(3):
    t.fd(30)
    t.rt(2)
t.lt(2)
t.pd()
for i in range(10):
    t.bk(30)
    t.lt(2)

t.end_fill()
Home()
t.begin_fill()

t.lt(10)
t.rt(180)
t.pd()
for i in range(20):
    t.fd(1)
    t.lt(2)
# t.lt(45)
for i in range(6):
    t.fd(20)
    t.lt(4)
t.rt(4)
t.fd(220)
for i in range(15):
    t.fd(10)
    t.rt(4)
t.lt(4)
t.fd(50)

t.pu()
t.rt(104)
t.fd(680)

t.end_fill()

turtle.mainloop()

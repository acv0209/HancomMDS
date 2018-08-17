import turtle as t

def draw(n):
    for i in range(n):
        t.forward(100)
        t.left(360/n)

def draw1(n):
    for i in range(n):
        t.forward(100)
        t.left(360*2/n)

draw1(5)

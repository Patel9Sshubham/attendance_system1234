import turtle
t = turtle.Turtle()
t.screen.bgcolor('black')
t.pensize(2)
t.color('green')
t.left(90)
t.backward(1000)
t.speed(100)
t.shape('turtle')

def tree(i):
    if i<50:
        return
    else:
        t.forward(i)
        t.color('red')
        t.circle('brown')
        t.left(80)
        tree(4*i/2)
        t.left(30)
        t.backward(i)

tree(1000)
turtle.done()

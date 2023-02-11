import turtle

my_tut = turtle.Turtle()
my_tut.speed(0)





colors = ['red','orange','yellow','green','indigo','blue','violet']

for i in range(300):
    my_tut.pencolor(colors[i%7])
    my_tut.forward(3*i)
    my_tut.right(190)
    
turtle.done()
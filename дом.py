import turtle
screen = turtle.getscreen()
t = turtle.Turtle()

def user_steni():
    user = False
    while user != True:
        st = int(input("Введите стены (макс 100): "))
        # st = 100
        if st > 100:
            user = False
        else:
            user = True
    return st

class DrawShape:
    def draw(self, sides, angle):
        for distance in sides:
            t.forward(distance)
            t.left(angle)
class Rectangle(DrawShape):
    def __init__(self, sides):
        self.sides = sides
        self.angle = 90

class Triangle(DrawShape):
    def __init__(self, sides):
        self.sides = sides
        self.angle = 120


steni = user_steni()
square = Rectangle([steni] * 4)
square.draw(square.sides, square.angle)
t.penup()
t.left(90)
t.forward(steni)
t.right(90)
t.forward(steni)
t.left(120)
t.pendown()
triangle = Triangle([steni] * 2)
triangle.draw(triangle.sides, triangle.angle)
t.penup()
t.right(90)
t.forward(steni)
t.left(90)
t.forward(steni / 2)
t.pendown()
square = Rectangle([steni / 4] * 4)
square.draw(square.sides, square.angle)

screen.mainloop()
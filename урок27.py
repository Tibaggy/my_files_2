import turtle
screen = turtle.getscreen()
t = turtle.Turtle()
# t.forward(100)
# t.left(90)
# t.forward(100)
# for i in range(360):
#     t.forward(100)
#     t.left(170)
#     t.left(170)
# leonardo = turtle.Turtle()
# raphael = turtle.Turtle()
# miki = turtle.Turtle()

# miki.color('orange')
# miki.left(90)
# miki.forward(90)

# leonardo.color('blue')
# leonardo.forward(90)
# leonardo.left(90)
# leonardo.forward(90)

# raphael.color('red')
# raphael.right(90)
# raphael.forward(90)

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


triangle = Triangle([150, 150, 150])
triangle.draw(triangle.sides, triangle.angle)



screen.mainloop()
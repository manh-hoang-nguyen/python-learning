import turtle
import random
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)

class GuiRectangle(Rectangle):
    def __init__(self, point1, point2):
        super().__init__(point1, point2)
    def draw(self,canvas):
        canvas = turtle.Turtle()
        canvas.penup()
        canvas.goto(self.point1.x,self.point1.y)
        canvas.pendown()
        canvas.forward(self.point2.x-self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y-self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x-self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y-self.point1.y)
        turtle.done()

gui_rec= GuiRectangle(Point(random.randint(0,400),random.randint(0,400)),Point(random.randint(0,400),random.randint(0,400)))
gui_rec.draw(gui_rec)
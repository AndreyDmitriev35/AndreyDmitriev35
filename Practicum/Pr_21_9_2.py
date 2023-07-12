class Rectangle:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


rect_area = Rectangle(5,10)
print(rect_area.area())
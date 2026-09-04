from math import sqrt

class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width
    
    def set_height (self, new_height) :
        self.height = new_height
    
    
    def set_width (self, new_width) :
        self.width = new_width 
    
    def get_area (self) :
        return self.height * self.width
    
    def get_perimeter (self) :
        return 2 * (self.height + self.width)
    
    def get_diagonal (self ):
        return sqrt(self.height ** 2 + self.width ** 2)
    
    def get_picture (self):
        res = ''
        if self.width > 50 or self.height > 50 :
            return "Too big for picture."
        for i in range (self.height) :
            for j in range (self.width ) :
                res += "*"
            res += "\n"
        return res 
    
    def get_amount_inside (self, Shape:object) :
        shape_area = Shape.get_area()
        return self.get_area() // shape_area
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
class Square(Rectangle) :
    def __init__(self, side ) :
        super().__init__(height=side , width=side) 
    def set_height (self, new_height) :
        self.height = new_height
        self.width = new_height 

    
    def set_width (self, new_width) :
        self.width = new_width 
        self.height = new_width

    def set_side (self, new_side) :
        self.height = new_side 
        self.width = new_side
    def __str__(self):
        return f"Square(side={self.width})"
    

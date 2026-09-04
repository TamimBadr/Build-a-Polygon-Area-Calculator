# Build-a-Polygon-Area-Calculator

A simple Python project demonstrating **Object-Oriented Programming (OOP)**, inheritance, and method overriding.

This is the **third project** in the **freeCodeCamp Python certification**.

## Features

### Rectangle

* Set width and height
* Calculate area
* Calculate perimeter
* Calculate diagonal
* Create a text picture
* Calculate how many shapes fit inside
* Display the rectangle as a string

### Square

`Square` inherits from `Rectangle` and:

* Keeps width and height equal
* Can change its side
* Overrides `set_width()` and `set_height()`
* Has its own string representation

## Example

```python
rectangle = Rectangle(10, 5)

print(rectangle.get_area())
print(rectangle.get_perimeter())

square = Square(5)

square.set_side(10)
print(square)
```

## Concepts Used

* Classes and objects
* Constructors
* Inheritance
* Method overriding
* `super()`
* Instance methods
* `__str__`

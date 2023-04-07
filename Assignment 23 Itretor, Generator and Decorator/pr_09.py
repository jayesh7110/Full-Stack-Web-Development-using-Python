# Define a function which takes lengths of three sides of a triangle as arguments and
# display the perimeter or triangle. Define and apply a decorator which checks for the
# validity of the triangle on the basis of lengths of the side. This makes the perimeter to
# be displayed when the triangle can exist with the given lengths of the sides.

def is_valid_triangle(func):
    def wrapper(a, b, c):
        if a+b > c and a+c > b and b+c > a:
            return func(a, b, c)
        else:
            return "Invalid triangle sides"

    return wrapper

@ is_valid_triangle
def triangle(a, b, c):
    return a+b+c


print(triangle(3,4,5))
print(triangle(2,2,5))


"""
1. Create a function that returns the multiplication product of three parameters (x, y, z).  z should have a default value of 1.
    a. Call the function with all positional arguments.
    b. Call the function with all named arguments.  
    c. Call the function with a mix of positional and named arguments.
    d. Call the function with only two arguments and use the default value for z.
"""

def multiply_three_values(x, y, z=1):
    product = x*y*z
    return product

some_number = multiply_three_values(10,10)
print some_number

some_number = multiply_three_values(5, z=10, y=100)
print some_number

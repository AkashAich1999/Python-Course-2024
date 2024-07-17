# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded 
# operators ‘+’ and ‘*’ which adds and multiplies them. 

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __mul__(self, other):
        # (ac - bd) + (ad + bc)i
        # (((self.real * other.real) - (self.imag * other.imag)) + ((self.real * other.imag) + (self.imag * other.real))i) 
        real_part = ((self.real * other.real) - (self.imag * other.imag))
        imag_part = ((self.real * other.imag) + (self.imag * other.real))
        return Complex(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)
print(c1 * c2)
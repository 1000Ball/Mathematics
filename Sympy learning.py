
## Simple tests of SymPy for better understanding

from sympy import *
## Should print mathprint but IDLE Shell does not support
init_printing(use_unicode = True)

## How SymPy initializes variables. Can be named anything
x, y = symbols('x, y')
## Combining "symbols" to make a function
f = 3**x + 4*y

## To evaluate this function, you can use either of these methods.
a = f.subs([(x,2), (y,3)])
b = f.evalf(150, subs={x:2.7, y:1.2}) # Outputs to the specified digit (150 in this case)

## Printing to see how it all looks
print(a)
print(b)
print(f)

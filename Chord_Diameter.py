import numpy as np


def Chord_Diameter(l, h):
    '''Function to determine the diameter / radius of a circle based on
    a chord where the length of the chord is known as well as it's perpendicular
    distance from the center of the circle. Returns diameter.'''

    ## If we consider the height intersecting the chord halfway along it's length,
    ## the hypotenuse of the height/half-length/radius triangle is
    ## the radius of the sliced circle.
    ## What we have is r = sqrt(h^2 + (l/2)^2) = sqrt(4h^2 + l^2)/2
    Diameter = np.sqrt(l**2 + (4*h**2))
    Radius = Diameter / 2

    printout = 'The diameter is {0}\nThe radius is {1}'.format(Diameter, Radius)

    print(printout)
    return Diameter

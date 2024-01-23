import numpy as np

def ang_circ_center(ang, r):
    '''Function that takes angle (degrees) of two lines and a circle of a decided radius
    and returns an angle bisector line length for center of circle to sit
    tangent to both lines as well as the length to point of tangency'''

    center = r/np.sin(0.5*np.deg2rad(ang))
    tangency = r/np.tan(0.5*np.deg2rad(ang))

    sols = {'center':center, 'tangency':tangency}
    return sols

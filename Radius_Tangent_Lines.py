
## A program that will produce the radius of a circle provided
## points (6) along tangent lines (3)

from Cramers_rule import Cramer
import numpy as np
import matplotlib.pyplot as plt

## Class to better hold everything together
class Radius_Tangent:

    def __init__(self):
        self.signs = [['+','+'], ['+','-'], ['-','+'], ['-','-']]
        self.sols = {}
        self.norms = []

    def line_from_points(self, point_a, point_b):
        '''Returns the coefficients for a line in standard form using point-
        slope form and rearranging'''

        ## Standard form is Ax + By = C (with integers, will not solve for integers)
        ## y-y1 = (x-x1)m
        ## mx - mx1 + y1 - y = 0
        ## mx - y -(mx1 - y1) = 0
        ## Parametric distance formula is |Ax+By+C|/sqrt(A^2 + B^2)
        
        slope = (point_b[1] - point_a[1]) / (point_b[0] - point_a[0])
        C = -((slope * point_a[0]) - point_a[1])
        norm = np.sqrt(slope**2 + 1)
        self.norms.append(norm)
        coeff = (-slope/norm, 1/norm, C/norm)
        
        return coeff


    def enter_3(self, points):
        '''Takes list of [tuples or lists] the points necessary for the
        three tangent lines and then stores the line coefficients'''

        self.line_1 = self.line_from_points(*points[0])
        self.line_2 = self.line_from_points(*points[1])
        self.line_3 = self.line_from_points(*points[2])



    def matrix_construct(self, signs):
        '''Takes three lines and a specified combo of sign configuration
        entered with '+' and '-' in a tuple/list to construct a square matrix to be solved.

        The matrix equation will be (2x2)(2x1) = (2x1):
        
        |(n_1,x {+/-} n_2,x)    (n_1,y {+/-} n_2,y)| |x_c| = |c_2 {+/-} c_1|
        |(n_1,x {+/-} n_3,x)    (n_1,y {+/-} n_3,y)| |y_c| = |c_3 {+/-} c_1|

        where n is the coefficient of noted subscript'''
        
        ## A is the (2x2) matrix, B is the solution vector
        A = np.zeros((2,2))
        B = np.zeros((2,1))

        exec('A[0,0] = {0}{1}{2}'.format(self.line_1[0], signs[0], self.line_2[0]))
        exec('A[0,1] = {0}{1}{2}'.format(self.line_1[1], signs[0], self.line_2[1]))
        exec('A[1,0] = {0}{1}{2}'.format(self.line_1[0], signs[1], self.line_3[0]))
        exec('A[1,1] = {0}{1}{2}'.format(self.line_1[1], signs[1], self.line_3[1]))

        exec('B[0,0] = {0}{1}{2}'.format(self.line_1[2], signs[0], self.line_2[2]))
        exec('B[1,0] = {0}{1}{2}'.format(self.line_1[2], signs[1], self.line_3[2]))
        
        self.A = A
        self.B = B



    def solve_it(self, points):
        '''Wrapping it all up, points is a list of tuples, signs is a list of strings'''

        self.mappings = {}
        
        for i in self.signs:
            
            self.enter_3(points)
            self.matrix_construct(i)
            mapping = Cramer(self.A, self.B)
            x_c = mapping['x0']
            y_c = mapping['x1']
            self.mappings[str(i)] = (x_c, y_c)
            
            radius = self.line_2[0]*x_c + self.line_2[1]*y_c - self.line_2[2]
            self.sols[str(i)] = radius

        x = ''
        for i in self.sols:
            x = x + str(i) + ':     ' + str(self.sols[i]) + 'at ' + str(self.mappings[i]) + '\n'
        return x


    

    def plot_it(self):
        '''Plots the potential circles and the tangent lines'''
        ## Limits can be changed for scale of radius. They're small now because of what I've been measuring
        spread = np.linspace(-1, 1, 200)
        plot_lines = []
        plt.figure(figsize=(6,2))

        colors = ['red', 'blue', 'green', 'orange']
        for i,j in enumerate(self.sols):
            plt.gca().add_patch(plt.Circle(self.mappings[j], self.sols[j], color=colors[i], fill=False, label=str(self.sols[j].round(4))))

        plot_lines.append((-self.line_1[0]/self.line_1[1])*spread + self.line_1[2]*self.norms[0])
        plot_lines.append((-self.line_2[0]/self.line_2[1])*spread + self.line_2[2]*self.norms[1])
        plot_lines.append((-self.line_3[0]/self.line_3[1])*spread + self.line_3[2]*self.norms[2])

        
        for i in plot_lines:
            plt.plot(spread, i)
        
        plt.axis('equal')
        plt.legend()
        plt.ylim(-2,2)
        plt.show()

if __name__ == "__main__":
    ## Test cases below
    #collect = [((0,0),(3,0)), ((1,2.7474),(2,5.4948)), ((1,-0.6379469),(2,-2.066095))] ## 0.6096
    #collect = [((-0.00409,0.02181),(-0.02268,-0.00677)), ((0,0.3244),(-.01732,0.01465)), ((-0.00724,0.01465),(-0.02126,-0.00937))]
    #collect = [((0,0),(-0.03977,-0.01433)), ((-0.01150,0.00071),(0.08174,0.02543)), ((0.02544,0.02543),(0.07268,0.00835))] ## 1/32 gage 0.03125
    #collect = [((0,0),(0.03473,0.04268)), ((0.02914,0.04268),(0.00685,0.00425)), ((-0.00110,0.00425),(0.03772,0.04299))]
    collect = [((0,0),(0.05371,0)), ((0.07103,0),(0.09773,-0.03205)), ((-0.05938,0),(-0.24357,-0.03205))] ## 15/64 = 0.234375
    
    
    x = Radius_Tangent()
    print(x.solve_it(collect))
    print(x.plot_it())

import numpy as np
import random
import matplotlib.pyplot as plt
from math import sqrt



class ChaosGame:

    """
    Class for generation and plotting fractals of n-gonesself.
    """

    def __init__(self,n,r = 0.5):
        if type(r) == float and (0 < r and r < 1):
            self.r = r
        else:
            raise ValueError('type has to be float or 0<r<1')
        if type(n)== int and n >= 3:
            self.n = n
        else:
            raise ValueError('type has to be int or n=>3')

    def _generate_ngon(self):

        """
        Creation of corners of the figure
        """

        n = self.n
        theta = np.linspace(0,2*np.pi,n+1)
        corners = []
        for i in theta:
            corners.append([np.sin(i),np.cos(i)])
        self.corners = np.asarray(corners)
        self.theta = theta
        return corners

    def _generate_points(self,N_points):

        """
        Generation of the random points bylinear combination of
        coefficients and random corners
        """

        r = np.random.random(size=(N_points, self.n))
        r_scaled = []
        self.new_r = []
        for i in range(N_points):
            r_scaled.append(1/sum(r[i]))
            self.new_r.append(r_scaled[i]*r[i])
        templist = []
        length = len(self.new_r)
        for i in range(length):
            for j in range(self.n):
                templist.append(self.new_r[i][j]*self.corners[j])
                #print(new_r[i][j],type(self.corners[j]))
        templist = np.asarray(templist)
        templist = np.split(templist, length)
        points = [np.sum(templist[i],axis = 0) for i in range(length)]
        self.points = points
        return self.points

    def _starting_point(self):

        """
        Pick a starting point within a figure
        """

        return self.points[0]

    def iterate(self, steps, discard=5):

        """
        Making points beginning from starting point
        """

        new_points = []
        new_points.append(self._starting_point())
        for i in range(1, steps+1):
            rp = np.random.randint(self.n)
            new_points.append(self.r*new_points[i-1] + (1-self.r) * self.corners[rp])
        del new_points[:discard+1]
        self.new_points = new_points
        return(self.new_points)

    def plot_ngon(self):
        plt.scatter(*zip(*(self.corners)),s=30,marker='.')
        plt.scatter(*zip(*self.points))
        plt.axis('equal')
        plt.axis('off')
        plt.show()

    def show(self):
        plt.scatter(*zip(*(self.new_points)), color='black', s=0.3, marker='.')
        plt.axis('equal')
        plt.axis('off')
        plt.show()

    def savepng(self, outfile):
        plt.scatter(*zip(*(self.new_points)), color='black', s=0.3, marker='.')
        if '.' and not 'png' in outfile:
            raise ValueError("Wrong format was given")
        if '.png' in outfile:
            plt.savefig(outfile, dpi=300, transparent=True)
        else:
            plt.savefig(outfile +'.png', dpi=300, transparent=True)
        plt.axis('equal')
        plt.axis('off')






if __name__ == '__main__':
    a = ChaosGame(3,1/2)
    a._generate_ngon()
    a._generate_points(20)
    a._starting_point()
#    a.plot_ngon()
    a.iterate(10000)
    a.show()
    a.savepng('filename.png')
    print(a.new_r)

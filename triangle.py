import numpy as np
import random
import matplotlib.pyplot as plt
from math import sqrt

np.random.seed(12345)

######## Exercise 1a ############

corners = np.array([[0,0], [0,1], [sqrt(3)/2,0.5]])
#print(corners)

plt.scatter(*zip(*(corners)))
plt.axis('equal')
plt.show()

#### Exercise 1b #########
### Example for a single point #####

def scaling(N_points):
    """
    First scale the coefficients
    """
    r2 = np.random.random(size=(N_points, 3))
    r_scaled = []
    new_r2 = []
    for i in range(N_points):
        r_scaled.append(1/sum(r2[i]))
        new_r2.append(r_scaled[i]*r2[i])
    return(new_r2)

def point_maker(arrays):
    """
    Finding points by calculating the linear combinations of coefficients and
    random corners
    """
    h = []
    length = len(arrays)
    for i in range(length):
        for j in range(3):
            h.append(arrays[i][j]*corners[j])
    h = np.asarray(h)
    h = np.split(h, length)   # since x and y coordinates here are following
    t = []                    # each other, the list is splitted so that
    for i in range(length):   # x and y coordinates would be together in 1 list pair.
        t.append(np.sum(h[i], axis=0))
    return(t)

y = scaling(1000)
u = point_maker(y)

plt.scatter(*zip(*(corners)))
plt.scatter(*zip(*(u)))
plt.axis('equal')
plt.show()

#### Exercise 1c #########

def iterating(size_points):
    new_points = []
    new_points.append(point_maker(scaling(1000))[0])

    for i in range(1,size_points+1):
        rp = np.random.randint(3)
        new_points.append((new_points[i-1] + corners[rp]) / 2)


    #removal of first 6 points (starting point + 5 generated)
    del new_points[:6]
    return(new_points)


g = iterating(10005)
#print(len(g))

#### Exercise 1d#########
def plotting(points):
    plt.scatter(*zip(*(points)),s=0.3,marker='.')
    plt.axis('equal')
    plt.axis('off')
    plt.show()


plotting(g)
#print(u[0])

#### Exercise 1e#########
def iterating_with_colors(size_points):
    new_points = []
    colors = []
    colors.append('red')
    new_points.append(u[0])

    for i in range(1,size_points+1):
        rp = np.random.randint(3)
        new_points.append((new_points[i-1] + corners[rp]) / 2)
        if rp == 0:
            colors.append('red')
        elif rp == 1:
            colors.append('blue')
        else:
            colors.append('green')

    del new_points[:6]
    del colors[:6]
    return(new_points,colors)

def plotting_with_colors(points,colors):
    #for i,j in zip(colors,points):
    plt.scatter(*zip(*(points)),s=0.3,marker='.',c = colors)
    plt.axis('equal')
    plt.axis('off')
    plt.show()

#### Exercise 1f#########
def alternative_colors(new_points_array):
    r0 = [1,0,0]
    r1 = [0,1,0]
    r2 = [0,0,1]
    corner_colors = np.array([r0, r1, r2])
    c0 = [0,0,0]
    new_colors = []
    new_colors.append(c0)
    for i in range(1, len(new_points_array)+1):
        rc = np.random.randint(3)
        new_colors.append((new_colors[i-1] + corner_colors[rc])/2)

    plt.scatter(*zip(*(new_points_array)), c = new_colors, s=0.8)
    plt.axis('equal')
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    p,c = iterating_with_colors(10005)
    plotting_with_colors(p,c)
    alternative_colors(p)

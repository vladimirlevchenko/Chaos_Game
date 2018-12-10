import nose.tools as nt
from chaos_game import ChaosGame
import numpy as np
import random
import matplotlib.pyplot as plt
from math import sqrt

 
@nt.raises(ValueError)
def test_init():

    """
    Check if it raises an error if not proper figure is chosen
    """

    temp = ChaosGame(2)
    temp = ChaosGame(1)

def test_scaled():
    """
    Test scaling vector - sum of the elements should be equal to 0
    """

    temp = ChaosGame(4)
    temp._generate_ngon()
    temp._generate_points(20)
    temp._starting_point()
    temp.iterate(10)
    computed = np.sum(temp.new_r[0])
    assert (1-computed)==0


def test_generate_ngon():

    """
    Checks if value that is passed to cos is in radians, i.e. cos(0) = 1
    """

    temp = ChaosGame(4)
    temp._generate_ngon()
    nt.assert_equal(np.cos(temp.theta[0]), 1)

@nt.raises(ValueError)
def test_savepng():

    """
    Tests if a wrong format of the picture gives error
    """

    temp = ChaosGame(2)
    temp._generate_ngon()
    temp._generate_points(20)
    temp._starting_point()
    temp.iterate(10)
    a.savepng('filename.jpg')

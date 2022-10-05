'''
Contains two functions hypot and distance
'''
import math


def hypotenuse(a, b):
    '''
    Returns hypotenuse of a right angled triangle given the length of its side

    Args:
        a (float): length of the first side
        b (float): length of the second side


    Returns:
        float: length of the hypotenuse
    '''
    return math.sqrt(a**2+b**2)


def distance(p, q):
    '''Determine the euclidean distance between two 2d points p and q

    Args:
        p (tuple): x, y values of first point
        q (tuple): x, y values of first point

    Returns:
        float: distance between the two points
    '''
    return math.sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))

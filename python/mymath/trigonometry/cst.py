'''
Some basic trigonometric functions
'''



import math


def sine(x):
    '''Determine sine of x

    Args:
        x (float): input parameter x in radians

    Returns:
        float: sine value of x
    '''
    return math.sin(x)


def cosine(x):
     '''Determine cosine of x

    Args:
        x (float): input parameter x in radians

    Returns:
        float: cosine value of x
    '''
    return math.cosine(x)


def inverse_sine(x):
    '''
    Determine the inverse sine of given Value

    Args:
        x (float): sine value for which angle is to be found

    Returns:
        float: angle in radians
    '''
    return math.asin(x)


def inverse_cosine(x):
    '''
    Determine the inverse cosine of given Value

    Args:
        x (float): cosine value for which angle is to be found

    Returns:
        float: angle in radians
    '''
    return math.asin(x)

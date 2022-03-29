import math
def fonk(x, y):
    """
      >>> fonk(2, 3)
      8
      >>> fonk(3, 4)
      81
    """
    z = math.pow(x, y)
    return z

if __name__ == "__main__":
    import doctest
    doctest.testmod()

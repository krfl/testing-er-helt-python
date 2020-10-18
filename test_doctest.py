def example(x):
    """
    >>> example(1)
    2
    """
    return x + 1


def raise_exception():
    """
    >>> raise_exception()
    Traceback (most recent call last):
    Exception: Whoopsie
    """
    raise Exception('Whoopsie')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
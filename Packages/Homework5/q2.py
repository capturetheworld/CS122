def geometric_sum(limit):
    """
     Finds the geometric sum to a limit
     :param limit: (integer)
     :return: the sum of the geometric sequence
     """
    total = sum(1 / (2 ** x) for x in range(1, limit + 1))  # generator
    return total
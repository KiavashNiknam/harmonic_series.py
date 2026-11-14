
def harmonic(n: int, r: float = 1) -> float:
    """
    Calculate the generalized harmonic series.

    Args:
        n (int): Number of terms.
        r (float): Power of each denominator.

    Returns:
        float: Sum of the series.
    """

    total = 0.0

    for i in range(1, n + 1):
        total += 1.0 / (i ** r)

    return total


# Example usage
print(harmonic(5))
print(harmonic(5, 2))

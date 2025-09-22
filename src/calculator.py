def fun1(x, y):
    """
    Adds two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Sum of x and y.
    Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x + y


def fun2(x, y):
    """
    Subtracts two numbers.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Difference of x and y.
    Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x - y


def fun3(x, y):
    """
    Multiplies two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Product of x and y.
    Raises:
        ValueError: If either x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x * y


def fun4(x, y, z):
    """
    Adds three numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
        z (int/float): Third number.
    Returns:
        int/float: Sum of x, y and z.
    """
    return x + y + z


def fun5(x, y):
    """
    Divides x by y.
    Args:
        x (int/float): Numerator.
        y (int/float): Denominator.
    Returns:
        float: Quotient of x divided by y.
    Raises:
        ValueError: If inputs are not numbers or y is zero.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


def fun6(x, y):
    """
    Raises x to the power of y.
    Args:
        x (int/float): Base number.
        y (int/float): Exponent.
    Returns:
        int/float: Result of x raised to the power of y.
    Raises:
        ValueError: If inputs are not numbers.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x ** y


if __name__ == "__main__":
    # Demo calls
    print("fun1(2, 3):", fun1(2, 3))
    print("fun2(5, 2):", fun2(5, 2))
    print("fun3(4, 3):", fun3(4, 3))
    print("fun4(2, 3, 4):", fun4(2, 3, 4))
    print("fun5(10, 2):", fun5(10, 2))
    print("fun6(2, 5):", fun6(2, 5))

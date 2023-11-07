def steps(number):
    """Calculate the number of steps required to reach 1 in the Collatz Conjecture.
    
    :param number: int - A positive integer.
    :return: int - The number of steps required to reach 1.

    Raises:
        ValueError: If the given value is zero or a negative integer.

    Function that takes a positive integer as an argument and calculates the number of steps
    required to reach 1 according to the Collatz Conjecture.
    """

    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    steps = 0
    while number != 1:

        number = number // 2 if number % 2 == 0 else number * 3 + 1

        steps+=1

    return steps


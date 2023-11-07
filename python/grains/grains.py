def square(number):
    """Calculate the number of grains on a specific square of a chessboard.

    :param number: int - The number of the square (1 to 64) on the chessboard.
    :return: int - The number of grains on the square.

    Raises:
        ValueError: If the given square is not between 1 and 64.

    This function takes the number of a square on a chessboard and calculates the
    number of grains of wheat on that square based on the doubling pattern.
    """

    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    return 1 << (number - 1)


def total():
    """Calculate the total number of grains on the entire chessboard.

    :return: int - The total number of grains on the chessboard.

    This function calculates the total number of grains on the entire chessboard by
    summing the grains on each square, utilizing the 'square' function.
    """
    return (1 << 64) - 1


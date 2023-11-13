def is_armstrong_number(number):
    """Determine if a number is an Armstrong number.

    :param number: int - The number to check.
    :return: bool - True if the number is an Armstrong number, False otherwise.

    This function checks if a given number is an Armstrong number. An Armstrong
    number is a number that is the sum of its own digits each raised to the power
    of the number of digits.
    """
    digits = [int(digit) for digit in str(number)]

    total = sum(pow(digit, len(digits)) for digit in digits)

    return number == total

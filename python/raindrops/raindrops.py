def convert(number):
    """Convert a number into a string with raindrop sounds based on its factors.

    :param number: int - The input number.
    :return: str - The resulting raindrop sound string.
    """
    drops = ''
    if number % 3 == 0:
        drops += 'Pling'
    if number % 5 == 0:
        drops += 'Plang'
    if number % 7 == 0:
        drops += 'Plong'
    if not drops:
        drops += str(number)

    return drops

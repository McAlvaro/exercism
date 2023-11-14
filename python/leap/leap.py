def leap_year(year):
    """Determine if a given year is a leap year.

    :param year: int - The year to check.
    :return: bool - True if the year is a leap year, False otherwise.

    The function determines if a year is a leap year based on the rules of the Gregorian calendar:
    - Every year that is evenly divisible by 4 is a leap year.
    - However, years that are evenly divisible by 100 are not leap years, unless they are also divisible by 400.
    """
    return year % 4 == 0 and (not (year % 100 == 0) or year % 400 == 0)

def is_triangle_valid(sides):
    """Check if the given lengths form a valid triangle.

    :param sides: list - List of side lengths.
    :return: bool - True if it is a valid triangle, False otherwise.
    """

    return all(side > 0 for side in sides) and all(sum(sides) - side > side for side in sides)

def equilateral(sides):
    """Determine if a triangle is equilateral.

    :param sides: list - List of side lengths.
    :return: bool - True if it is equilateral, False otherwise.
    """

    return is_triangle_valid(sides) and len(set(sides)) == 1


def isosceles(sides):
    """Determine if a triangle is isosceles.

    :param sides: list - List of side lengths.
    :return: bool - True if it is isosceles, False otherwise.
    """

    return is_triangle_valid(sides) and (len(set(sides)) == 2 or len(set(sides)) == 1)



def scalene(sides):
    """Determine if a triangle is scalene.

    :param sides: list - List of side lengths.
    :return: bool - True if it is scalene, False otherwise.
    """

    return is_triangle_valid(sides) and len(set(sides)) == 3

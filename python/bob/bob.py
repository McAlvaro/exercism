def response(hey_bob):
    """Determine Bob's response based on the given remark.

    :param hey_bob: str - The input remark from the user.
    :return: str - Bob's response.

    The function checks the provided remark and returns Bob's
    """
    hey_bob = hey_bob.strip()

    if not hey_bob:
        return "Fine. Be that way!"
    elif hey_bob.isupper() and hey_bob.endswith('?'):
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    elif hey_bob.endswith('?'):
        return "Sure."
    else:
        return "Whatever."

def exchange_money(budget, exchange_rate):
    """Calculate the exchange rate value.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.

    This function should return the value of the exchanged currency.
    """

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """Calculate the amount of money left over from the budget.

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.

    This function should return the amount of money that is left from the budget.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """Calculate the total value of the bills to be refunded.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.

    Your function should return only the total value of the bills (excluding fractional amounts) that the booth would return.
    """

    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """Calculate the number of bills you can receive within the given quantity.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.

    This function should return the number of bills that can be received within the given amount.
    """

    return int(amount // denomination)


def get_leftover_of_bills(amount, denomination):
    """Calculate the remaining amount that cannot be refunded from the initial amount.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.

    This function must return the excess amount that cannot be returned from the 
    initial amount due to the denomination of the banknotes.
    """

    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calculate the maximum value of the new currency.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.

    This function should return the maximum value of the new currency after 
    calculating the exchange rate plus the differential.
    """

    amount = exchange_money(budget, (exchange_rate + (exchange_rate * (spread / 100))))

    number_of_bills = get_number_of_bills(amount, denomination)

    return int( number_of_bills * denomination )

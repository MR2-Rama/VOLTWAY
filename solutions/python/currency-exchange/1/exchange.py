def exchange_money(budget, exchange_rate):
    """exchange from USD to EUR"""
    return budget / exchange_rate

def get_change(budget, exchanging_value):
    """ currency left after exchange """
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """ value of bills """
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """ Number of bills """
    return amount // denomination


def get_leftover_of_bills(amount, denomination):
    """ leftover bills"""
    return amount % denomination



def exchangeable_value(budget, exchange_rate, spread, denomination):
    actual_value = exchange_rate * (1 + spread/100)
    exchanged_money = budget / actual_value
    number_of_bills = int(exchanged_money // denomination)
    actual_money = number_of_bills * denomination
    return actual_money
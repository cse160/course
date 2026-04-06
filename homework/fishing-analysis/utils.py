import matplotlib.pyplot as plt
import os
import math

from sys import platform
if platform == 'darwin':
    import matplotlib  # noqa: E402
    matplotlib.use("macosx")

###############################################################################
# You do not need to change anything in this file! However,                   #
# `plot_linear_prediction` relies on the functions you will implement in this #
# assignment and will not work until you have implemented them.               #
###############################################################################


def plot_linear_prediction(country):
    '''
    A function that takes a country object and then calls
    the `calculate_prediction` function with the production need
    data (from get_production_need) for the given country, and
    plots the best-fit line and prediction.

    NOTE: This is a complete function, you do not need to modify it. However,
    it relies on parse_data, get_production_need, and calculate_prediction to
    be implemented according to the assignment spec.

    You will be asked to run this function in Problem 4b.
    '''
    plt.plot(country.need.keys(), country.need.values(), label='data',
             linestyle='', marker='s')

    prediction = country.predict_need(50)
    plt.plot(prediction['years'], prediction['values'],
             linestyle='--', label='best-fit prediction')

    plt.title('Predicted Production Need For ' + country.name)
    plt.xlabel('Year')
    plt.ylabel('Metric Tonnes')
    plt.legend()
    plt.savefig(os.path.dirname(__file__) + "/" + country.name +
                "_need_prediction.png")
    plt.clf()


def min_year(fields):
    '''
    A helper function that, given a list of values, returns
    the minimum integer.

    You do not have to modify or even use this function, but it is here
    if you want to use it. It is suggested to use it in `parse_data`.
    '''
    return min([int(field) for field in fields
                if type(field) is int or field.isnumeric()])


def max_year(fields):
    '''
    A helper function that, given a list of values, returns
    the maximum integer.

    You do not have to modify or even use this function, but it is here
    if you want to use it. It is suggested to use it in `parse_data`.
    '''
    return max([int(field) for field in fields
                if type(field) is int or field.isnumeric()])


def check_approx_equals(expected, received):
    """
    Checks received against expected, and returns whether or
    not they match (True if they do, False otherwise).
    If the argument is a float, will do an approximate check.
    If the argument is a data structure will do an approximate check
    on all of its contents.

    Arguments:
        expected: the expected value
        received: the received value

    Returns: True if the received match the expected, False otherwise
    """

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    if isinstance(expected, dict):
        return expected.keys() == received.keys() and \
            all(check_approx_equals(expected[k], received[k])
                for k in expected)
    elif isinstance(expected, (list, set)):
        return len(expected) == len(received) and \
            all(check_approx_equals(v1, v2)
                for v1, v2 in zip(expected, received))
    elif isinstance(expected, float):
        return math.isclose(expected, received, abs_tol=0.0001)
    else:
        return expected == received


def assert_equals(expected, received):
    """
    Checks received against expected, throws an AssertionError
    if they don't match. If the argument is a float, will do an approximate
    check. If the argument is a data structure will do an approximate check
    on all of its contents.

    Arguments:
        expected: the expected value
        received: the received value
    """

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    assert check_approx_equals(expected, received), \
        f'Expected {pformat(expected)},\n\tbut received {pformat(received)}'

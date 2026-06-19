"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This module contains helper functions to calculate preparation,
baking, and elapsed time for making lasagna.
"""

# Constants
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time in minutes.

    The function takes the number of minutes the lasagna has already
    been baking and returns the number of minutes left based on the
    EXPECTED_BAKE_TIME constant.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.

    Returns:
        int: The total preparation time in minutes.

    Each layer takes PREPARATION_TIME minutes to prepare.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time.

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The total elapsed time in minutes.

    The total elapsed time is the sum of the preparation time and
    the elapsed baking time.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
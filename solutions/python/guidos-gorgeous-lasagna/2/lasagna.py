"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """
    Calculate the bake time remaining.

    Input: parameter elapsed_bake_time - baking time already elapsed (int).
    Output: return remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME' (int).

    The function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the preparation time remaining.

    Input: parameter number_of_layers - How many layers will the lasagna have? (int).
    Output: return the preparation time based on the number of layers. (int).

    The function will take PREPARATION_TIME multiplied by number_of_layers
    """
    
    return number_of_layers * PREPARATION_TIME

#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate the total time used (prepping + baking).

    Input:
    - parameter number_of_layers - How many layers will the lasagna have? (int).
    - parameter elapsed_bake_time - How long has the lasagna been in the oven? (int).
    Output: return the total time used (int).
    """
    
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    
    
# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)

#!/usr/bin/env python3
"""
This script contains a function that creates a
function to multiply a number by a given multiplier.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a float as a multiplier
    and returns a function that multiplies its input by this multiplier.

    Parameters:
    multiplier (float): The multiplier to be used in the returned function.

    Returns:
    Callable[[float], float]: A function that multiplies
    its input by the given multiplier.
    """
    def callback(val: float) -> float:
        return (val * multiplier)

    return (callback)

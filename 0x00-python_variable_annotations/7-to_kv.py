#!/usr/bin/env python3
"""
This script contains a function that takes
a string and a number (integer or float),
squares the number, and returns a tuple
with the string and the squared number.
"""


from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function takes a string and a number
    (integer or float), squares the number,
    and returns a tuple with the string and the squared number.

    Parameters:
    k (str): The string to be included in the tuple.
    v (Union[int, float]): The number to be squared and included in the tuple.

    Returns:
    tuple: A tuple containing the string and the squared number.
    """

    return k, v**2

#!/usr/bin/env python3
"""
This script contains a function that calculates the sum of
all numbers in a mixed list of integers and floats.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function takes a list of mixed integers and float
    numbers as input and returns their sum.

    Parameters:
    mxd_lst (List[Union[int, float]]): The list of numbers to be summed.

    Returns:
    float: The sum of all numbers in the input list.
    """
    a: float = 0
    for val in mxd_lst:
        a = val + a
    return (a)

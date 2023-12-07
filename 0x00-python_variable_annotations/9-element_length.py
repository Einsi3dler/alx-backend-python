#!/usr/bin/env python3
"""
This script contains a function that takes
an iterable of sequences as input and returns a list of tuples,
where each tuple contains a sequence from the input and its length.
"""


from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function takes an iterable of
    sequences as input and returns a list of tuples,
    where each tuple contains a sequence from the input and its length.

    Parameters:
    lst (Iterable[Sequence]): The iterable of sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples,
    where each tuple contains a sequence from the input and its length.
    """
    return [(i, len(i)) for i in lst]

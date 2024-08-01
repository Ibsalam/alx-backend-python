#!/usr/bin/env python3
'''Module containing the element_length function.
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Returns a list of tuples, each containing a string from the input list and its length.
    '''
    return [(i, len(i)) for i in lst]

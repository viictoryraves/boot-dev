from typing import List


def sum_nested_list(lst):
    total = 0
    for elem in lst:
        if isinstance(elem, List):
            total = total + sum_nested_list(elem)
        if isinstance(elem, int):
            total = total + elem
    return total

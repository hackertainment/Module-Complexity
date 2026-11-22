from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

    Time complexity: n*n = n^2 = O(n^2)
    Space complexity: 1+n = n+1 = O(n)
    Optimal time complexity: n+n = 2n = O(n)
    """
    unique_items = list(dict.fromkeys(values))  # dic.fromkeys() preserving the order of the values
    #unique_items = []

    #for value in values:
    #    is_duplicate = False
    #    for existing in unique_items:
    #        if value == existing:
    #            is_duplicate = True
    #            break
    #    if not is_duplicate:
    #        unique_items.append(value)

    return unique_items

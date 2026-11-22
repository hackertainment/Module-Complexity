from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity: n*n = n^2 = O(n^2)
    Space Complexity: n+n = 2n = O(n)
    Optimal time complexity: n+n+2n+2n = 6n = O(n)
    """
    #common_items: List[ItemType] = []
    #for i in first_sequence:
    #    for j in second_sequence:
    #        if i == j and i not in common_items:
    #            common_items.append(i)
    common_items = list(set(first_sequence+second_sequence))
    return common_items

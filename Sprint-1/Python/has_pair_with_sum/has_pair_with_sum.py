from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity: (n-1)+(n-2)+...+1 = (n(n-1))/2 = O(n^2)
    Space Complexity: 1 = 1 = O(1)
    Optimal time complexity: n+n+n = 3n = O(n)
    """
    #for i in range(len(numbers)):
    #    for j in range(i + 1, len(numbers)):
    #        if numbers[i] + numbers[j] == target_sum:
    #            return True
    seen = set()
    for num in numbers:
        if (target-num) in seen:  # Operation Complexity x in s => O(1) https://docs.python.org/3/builtins/time-complexity.html#set-frozenset
            return True
        seen.add(num)
    return False

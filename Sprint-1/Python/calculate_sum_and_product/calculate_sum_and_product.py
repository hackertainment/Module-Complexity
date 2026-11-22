from typing import Dict, List


def calculate_sum_and_product(input_numbers: List[int]) -> Dict[str, int]:
    """
    Calculate the sum and product of integers in a list.

    Note: the sum is every number added together
    and the product is every number multiplied together
    so for example: [2, 3, 5] would return
    {
        "sum": 10, // 2 + 3 + 5
        "product": 30 // 2 * 3 * 5
    }
    Time Complexity:  n+n = 2n = O(n)
    Space Complexity: 1+1 = 2 = O(1)
    Optimal time complexity: O(n) because to find the sum (and product) of all elements, it must visit each number in the array at least once (or twice).
    """
    # Edge case: empty list
    if not input_numbers:
        return {"sum": 0, "product": 1}

    sum = 0
    for current_number in input_numbers:
        sum += current_number

    product = 1
    for current_number in input_numbers:
        product *= current_number

    return {"sum": sum, "product": product}

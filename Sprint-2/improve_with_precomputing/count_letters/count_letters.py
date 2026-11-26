def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    only_upper = set(s)-set("abcdefghijklmnopqrstuvwxyz")
    for letter in (set(s)-set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")):
        only_upper.discard(letter.upper())
    return len(only_upper)


def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()

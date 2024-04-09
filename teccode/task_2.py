from sympy import isprime


def prime_numbers(min_num: int, max_num: int) -> list[int] | str:
    """
    A function that generates a list of prime numbers within a given range.

    Parameters:
        min_num (int): The minimum number of the range.
        max_num (int): The maximum number of the range.

    Returns:
        list[int] | str: A list of prime numbers within the specified range.
    """

    if not isinstance(min_num, int) or not isinstance(max_num, int):
        raise ValueError("Only integer objects are allowed!")
    if min_num < 0 or max_num < 0:
        raise ValueError("Only positive numbers are allowed!")
    if min_num > max_num:
        raise ValueError("The minimum number cannot be greater than the maximum number!")
    result = [num for num in range(min_num, max_num + 1) if isprime(num)]
    return result

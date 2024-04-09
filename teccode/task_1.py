def unique_list(numbers: list[int]) -> list[int] | str:
    """
    Function to return a list of unique integers from the input list.

    Parameters:
    - numbers: a list of integers

    Returns:
    - a list of unique integers, or a string indicating the error message
    """

    try:
        is_numbers = all(isinstance(x, int) for x in numbers)
        if is_numbers:
            result = list(set(numbers))
            return result
        return "Only integer objects are allowed in the list!"
    except TypeError:
        return "Only iterable objects are allowed!"

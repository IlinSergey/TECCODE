def sort_list_by_length(strings: list[str]) -> None | str:  # type: ignore
    """
    Sorts a list of strings by their lengths and prints the sorted list as well as the sorted list in reverse order.

    Parameters:
    strings (list[str]): A list of strings to be sorted.

    Returns:
    None or str: Returns None if the input list contains only strings and prints the sorted list and the sorted list in reverse order. Returns a string error message if the input list contains non-string elements.  # noqa: E501
    """

    try:
        is_strings = all(isinstance(x, str) for x in strings)
        if is_strings:
            sorted_list = sorted(strings, key=len)
            print(sorted_list)

            sorted_list_reversed = sorted(strings, key=len, reverse=True)
            print(sorted_list_reversed)
        else:
            raise ValueError("Only string objects are allowed in the list!")
    except TypeError:
        return "Only iterable objects are allowed!"

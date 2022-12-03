def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    for lst_val in lst:
        if not isinstance(lst_val, list):
            return False

    return True

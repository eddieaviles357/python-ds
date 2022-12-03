def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    is_balanced = 0
    for parentheses in parens:
        if parentheses == '(':
            is_balanced += 1
        elif parentheses == ')':
            is_balanced -= 1

        if is_balanced < 0:  # invalid parentheses too many closing ones )
            return False

    return is_balanced == 0

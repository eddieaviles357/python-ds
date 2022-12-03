def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """


def three_odd_numbers(nums):
    for idx in range(len(nums) - 2):  # if any 3 sequential sum total is odd return True
        if (nums[idx] + nums[idx + 1] + nums[idx + 2] % 2 != 0):
            return True
    return False  # no sums were odd

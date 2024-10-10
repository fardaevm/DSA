def longest_consecutive_sequence(arr):
    """
    Given an array of integers, find the length of the longest consecutive sequence.
    Args:
        arr: An array of integers.
    Returns:
        int: The length of the longest consecutive sequence.
    """
    num_set = set(arr)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)
    return longest_streak




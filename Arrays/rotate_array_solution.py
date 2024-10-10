def rotate_array(arr, k):
    """
    Rotates an array to the right k steps
    Arguments:
        arr: an array of integers
        k: an integer
    Returns:
        the rotated array after k steps
    """
    if not arr:
        return arr # an empty array

    k = k % len(arr) # Ensure k is within the length of the array

    return arr[-k:] + arr[:-k]

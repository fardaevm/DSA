def find_kth_smallest(arr, k):
    """
    Finds the kth smallest element in an array.
    Args:
        arr (list): An array of integers.
        k (int): An integer. The kth smallest element to return. 1 <= k <= arr.size.
    Returns:
        int: The kth smallest element in an array.
    Raises:
        ValueError: If k is out of bounds, arr is empty, or arr contains non-integer elements.
        TypeError: If arr is not a list or k is not an integer.
    """
    # checks if the first argument is a list
    if not isinstance(arr, list):
        raise TypeError("The first argument must be a list.")
    # checks if all elements in an array are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be an integer.")
    # checks if k is integer
    if not isinstance(k, int):
        raise TypeError("k must be an integer.")
    # checks if k in valid range
    if k < 0 and len(arr) < k:
        raise ValueError(f"k must be between 1 and {len(arr)}, but got {k}.")
    # checks if the array empty
    if not arr:
        raise ValueError("The array must contain at least one element.")


    arr.sort()
    # returns kth element (1-based index)
    return arr[k-1]



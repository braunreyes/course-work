
# exercise 1.1 log₂128 == 7
# exercise 1.2 log₂256 == 8

def main(arr: list, num: int) -> int | None:
    """practice for Binary Search
        guess using non-linear O(logN)

        base case - mid == guess
        recursive case 1 - if guess > num then call again with mid - 1
        recursive case 2 - if guess < num then call again with mid + 1

    Args:
        arr (list): unique sorted list
        num (int): number to find

    Returns:
        int | None: return index or None
    """
    low = 0
    high = len(arr) -1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == num:
            return mid
        elif guess > num:
            high = mid - 1
        else:
            low = mid + 1
    return None

if __name__ == "__main__":
    result = main([1,2,3,4,5,6,7,8,9], 6)
    assert result == 5
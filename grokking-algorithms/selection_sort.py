
# exercise 1.1 log₂128 == 7
# exercise 1.2 log₂256 == 8

def find_smallest(arr: list) -> int:
    """return index of smallest number in list

    Args:
        arr (list): unsorted list of numbers

    Returns:
        int: index of smallest number
    """
    smallest_index = 0
    smallest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > smallest:
            smallest_index = i
            smallest = arr[i]
    return smallest_index

def main(arr: list) -> list:
    """practice for selection sort
        O(n * n)

    Args:
        arr (list): unsorted list

    Returns:
        list | sorted list
    """
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    
    print(arr)
    return arr
    

if __name__ == "__main__":
    result = main([3,8,4,6,2,5,9,7,1])
    assert result == [1,2,3,4,5,6,7,8,9]
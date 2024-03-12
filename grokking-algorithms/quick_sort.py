def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        left = [i for i in arr[1:] if i <= pivot]
        right = [i for i in arr[1:] if i > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    result = quick_sort([5, 6, 1, 9, 3, 11, 25, 4, 1])
    print(result)
    assert result == [1, 1, 3, 4, 5, 6, 9, 11, 25]

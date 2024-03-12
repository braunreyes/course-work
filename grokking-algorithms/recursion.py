def fact(x: int) -> int:
    """simple recursion example
    call stack will maintain "stack"
    of partially run function calls that are paused.
    they are then continued in a LIFO order

    Args:
        x (int): _description_

    Returns:
        int: _description_
    """
    if x == 1:
        return x
    else:
        return x * (x - 1)
    
def sum_num(arr):
    if not arr:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum_num(arr[1:])
    

def count_num(arr):
    if not arr:
        print("returning 0")
        return 0
    else:
        for i in arr:
            print(f"1 + count_num({arr[1:]}")
            return 1 + count_num(arr[1:])

    
def max_num(arr):
    if count_num(arr) == 1:
        return arr[0]
    else:
        for i in range(1, count_num(arr)):
            if arr[i] > arr[i-1]:
                print(arr[1:])
                return max_num(arr[1:])
            else:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                print(arr[1:])
                return max_num(arr[1:])
            


def main():
    assert fact(3) == 6
    assert sum_num([1,2,3,4]) == 10
    assert count_num([1,2,3,4,5]) == 5
    assert max_num([1,2,3,6,4,5]) == 6


if __name__ == "__main__":
    main()
    

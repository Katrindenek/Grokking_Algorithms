def binary_search(sorted_list: list, item: int):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high)
        guess = sorted_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        return None

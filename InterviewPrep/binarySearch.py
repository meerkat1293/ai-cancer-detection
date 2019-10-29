def binarysearch(some_list,target):
    midpoint_idx = len(some_list) // 2
    midpoint_value = some_list[midpoint_idx]
    print(midpoint_value)
    if target == midpoint_value:
        return 'Found'
    elif target < midpoint_value:
        binarysearch(some_list[:midpoint_idx],target)
    elif target > midpoint_value:
        binarysearch(some_list[midpoint_idx:],target)


print(binarysearch([1,2,3,4,5,6,7,8,9,10], 10))
# Returns index of number in input_list[l..h] if number is present, otherwise returns -1
def rotated_array_search(input_list, l, r, number):
    if l > r:
        return -1

    mid = (l + r) // 2
    if input_list[mid] == number:
        return mid

    # If arr[l...mid] is sorted
    if input_list[l] <= input_list[mid]:

        # As this subarray is sorted, we can quickly
        # check if key lies in half or other halfx
        if number >= input_list[l] and number <= input_list[mid]:
            return rotated_array_search(input_list, l, mid-1, number)
        return rotated_array_search(input_list, mid+1, r, number)

    # If input_list[l..mid] is not sorted, then input_list[mid... r] must be sorted
    if number >= input_list[mid] and number <= input_list[r]:
        return rotated_array_search(input_list, mid+1, r, number)
    return rotated_array_search(input_list, l, mid-1, number)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, 0, len(input_list)-1, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]) #pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 10]) #pass
test_function([[], 4])  #pass (edge case)
test_function([[1, 2, 3, 4, 6, 7, 8], 7])  #pass (sorted array)
test_function([[6, 7, 8, 1, 2, 3, 4], 3])  #pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])  #pass (edge case)

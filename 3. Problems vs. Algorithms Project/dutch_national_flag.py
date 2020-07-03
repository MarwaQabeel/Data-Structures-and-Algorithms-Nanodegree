def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2,
    sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    counter = [0, 0, 0]
    for i in input_list:
        counter[i] = counter[i] + 1

    ending_0 = [0 for i in range(counter[0])]
    ending_1 = [1 for i in range(counter[1])]
    ending_2 = [2 for i in range(counter[2])]

    return ending_0 + ending_1 + ending_2


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
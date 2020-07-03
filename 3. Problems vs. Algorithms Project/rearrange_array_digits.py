def rearrange_digits(input_list: list):

        input_list = sorting_function(input_list)
        num1: str = ""
        num2: str = ""

        for i in range(0, len(input_list), 2):

            num1 = str(input_list[i]) + num1
            try:
                num2 = str(input_list[i + 1]) + num2
            except Exception:
                return [int(num1), int(num2)]

        return [int(num1), int(num2)]

def sorting_function(array):
            if len(array) <= 1:
                return array

            midway = int(len(array) / 2)
            left, right = sorting_function(array[:midway]), sorting_function(array[midway:])
            return merge_function(left, right)

def merge_function(left, right):
            result = []
            left_p = right_p = 0

            while left_p < len(left) and right_p < len(right):
                if left[left_p] < right[right_p]:
                    result.append(left[left_p])
                    left_p += 1
                else:
                    result.append(right[right_p])
                    right_p += 1

            result.extend(left[left_p:])
            result.extend(right[right_p:])

            return result


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_case1 = [[1, 2, 3, 4, 5], [542, 31]]
test_case2 = [[7, 8, 9, 1, 2], [971, 82]]
test_function(test_case)
test_function(test_case1)
test_function(test_case2)

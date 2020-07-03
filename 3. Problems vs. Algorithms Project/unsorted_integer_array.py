def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    minimum = maximum = ints[0]

    for i in ints:
        if i <= minimum:
            minimum = i
        if i >= maximum:
            maximum = i

    return (minimum, maximum)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

k = [1]
print("Pass" if ((1, 1) == get_min_max(k)) else "Fail")

m = [0, 0]
print("Pass" if ((0, 0) == get_min_max(m)) else "Fail")
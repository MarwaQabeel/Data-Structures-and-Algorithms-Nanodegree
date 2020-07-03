## Problem 2: Search in a Rotated Sorted Array Explanation

- We are given a sorted array which is rotated at some random pivot point. We are given a
target value to search. If found in the array return the index, otherwise return -1.


- The algorithm used for this would run in time complexity `O(log n)`. This is 
possible by using a binary search approach but with a small modification. The binary search is
good because it helps to reduce time complexity by eliminating half of the competitor. 


- On every repetition we try to figure a center record and, on the off chance that we do not find the element, we attempt to see on the other 2 inclines. on the `input_list[mid] > input_list[r]` 
implies that the center component is on the left slant, while `input_list[mid] <= input_list[l]` means that the center component is on the right slant. After every cycle the search zone is splitted which takes us to complexity `O(log n)`.

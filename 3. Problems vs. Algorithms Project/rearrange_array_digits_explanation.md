## Problem 3: Rearrange Array Digits Explanation

- The arrangement found was to order the components in the array and sort them to create a number 
dependent on a sequence that enables us to sum the higher digits as the max as possible inside the value created from such array. 

 
- This keeps running in O(n log n) time and O(n) space. It actualizes a union sort calculation to sort on plummeting request the digits from the cluster. This take O(n log n) time and O(n) space. At that point it emphasizes over the arranged cluster to figure the 2 numbers. This take O(n) time and O(1) space. Also, a check is performed to check whether the subsequent number is 0, in which case the principal number is decreased to have close to 2 digits.This is O(log n) most pessimistic scenario in time and O(1) space.


- The overall space complexity is of O(n).

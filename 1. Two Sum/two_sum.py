from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict ={}

        for i, num in enumerate(nums):
            complement =  target- num
            if complement in num_dict:

                return [num_dict[complement],i]
            num_dict[num] = i
        return []
    

solution = Solution()

'''
For each test case, it calls the twoSum function and compares it with the expected result. 
If the return value of the function does not match the expected value, an error message is printed.
When all tests have passed, the message "All tests passed!" is printed.

by Said AKÇA

'''

assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1], "Test 1 failed"
assert solution.twoSum([3, 2, 4], 6) == [1, 2], "Test 2 failed"
assert solution.twoSum([3, 3], 6) == [0, 1], "Test 3 failed"
assert solution.twoSum([1, 2, 3], 7) == [], "Test 4 failed"

print("Tüm testler başarılı!")
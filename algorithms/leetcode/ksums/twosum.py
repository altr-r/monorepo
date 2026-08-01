from typing import List

'''
* can be solved using two pointer approach
* but many edge cases need to be checked in that case
* one pass hashmap version seemed easier to me
* because when I used two pointers to solve this problem
* I experienced if one test case works, the other doesn't
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, value in enumerate(nums):
          diff = target - value
          if diff in hashmap:
            return hashmap[diff], index
          else:
            hashmap[value] = index



s1 = Solution()
print(s1.twoSum([-1,-2,-3,-4,-5], -8))
from typing import List

'''
* can also be solved using the one pass hashmap method from twosum1,
* but overall two pointers is the faster approach
* doesn't need extra memory as we don't need to create any extra hashmap or dictionary
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      i = 0
      j = len(numbers) - 1

      while True: # use while (i < j) instead
        sm = numbers[i] + numbers[j]
        if sm == target:
          return i+1, j+1
        elif sm > target:
          j-=1
        else:
          i+=1

s1 = Solution()
print(s1.twoSum([2, 3, 4], 6))
from typing import List

numbers = [-1,0,1,2,-1,-4]

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:


      nums.sort()
      res = []
      for i in range(len(nums) - 1):
        l = i + 1
        r = len(nums) - 1
        s = nums[i] + nums[l] + nums [r]
        if s == 0:
          res.append([nums[i], nums[l], nums[r]])
        elif s > 0:
          r-=1
        else:
          l+=1
      return res

s1 = Solution()
print(s1.threeSum(numbers))

from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    ans = None

    seen = {}

    for index, num in enumerate(nums):
      find = target - num

      if find in seen:
        ans = [seen[find], index]

      seen[num] = index

    return ans


my = Solution()
# nums = [2,7,11,15]
# target = 9
# trueAns=[0,1]

nums = [3,2,4]
target = 6
trueAns=[1,2]

ans = my.twoSum(nums,target)

print("ans", ans, ans == trueAns)


"""

2,7,11,15
9

2,7,11,15
^ ^
+++

2,3,11,7,15
^ ^
2+3 = 5 (9)

2,3,11,7,15
^      ^
+++

3,2,11,7,15
  ^    ^
+++

O(N^2) - time
O(1) - space


3,2,11,7,15
a + b = c
a + b = target
a = target - b

map = {}

------------------------

map = {}
3,2,11,7,15
^ (9-3 = 6 NO (add 3))

map = { 3, }
3,2,11,7,15
  ^  (9-2 = 7 NO (add 2))

map = { 3, 2}
3,2,11,7,15
    ^  (9-11 = -2 NO)

map = { 3,2,11}
3,2,11,7,15
       ^  (9-7 = 2 YES!)


O(N) - time
O(N) - space
"""

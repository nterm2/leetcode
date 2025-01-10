"""
On(n) time complexity. One idea could be to subtract the current number 
in the list we are iterating over by the target. attempt to get the index of the result. if present, return arry of the index, otherwise keep iterating.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            try:
                temp_l = nums[:]
                temp_l.pop(index)
                second_index = temp_l.index(target - num)
                second_index = second_index + 1 if second_index >= index else second_index
            except:
                continue 
            else:
                return [index, second_index]

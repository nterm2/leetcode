class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # need to find the middle elemnt's index.
        #check if it is the correct value.
        # if not, check if it less than the target value, check the other side
        start_pointer = 0
        end_pointer = len(nums) - 1

        while (start_pointer <= end_pointer):
            middle_index = (end_pointer + start_pointer) // 2
            if nums[middle_index] == target:
                return middle_index
            elif nums[middle_index] > target:
                end_pointer = middle_index - 1
            else:
                start_pointer = middle_index + 1
        return -1 
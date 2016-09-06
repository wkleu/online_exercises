class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dictionary = {}
        for idx, val in enumerate(nums):
            if val in dictionary:
                dictionary[val] = dictionary[val] + [idx]
            else:
                dictionary[val] = [idx]

        for current_index, value in enumerate(nums):
            required = target - value
            if required in dictionary:
                for indexForValue in dictionary[required]:
                    if current_index != indexForValue:
                        return [current_index, indexForValue]

        return []


print(Solution().twoSum(nums=[0, 4, 3, 0], target=0))

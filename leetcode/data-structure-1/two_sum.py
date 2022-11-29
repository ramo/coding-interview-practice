# https://leetcode.com/problems/two-sum/
# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

#  

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

#  

# Constraints:

#     2 <= nums.length <= 104
#     -109 <= nums[i] <= 109
#     -109 <= target <= 109
#     Only one valid answer exists.

#  
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

from typing import List

class Solution:

# [1, 2, 3, 4, 5] target = 8 [2, 4]
# [-2, -3, 1, 5, 9, -4]  target = -7

# {
#   1:0
#   2:1
#   3:2
#   4:3
#   5:4
# }
# O(n) + O(n) = O(n)
#   [3, 3]  target = 6

      
    # Time: O(n^2)
    # Memory: O(1)
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        # iterate each number in the array
        # for each number check if the sum of this number and rest of the numbers in the array
        # is equal to the target sum
        # if true return indices of both the numbers
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        # This will not reach here
        return None 

    # Time: O(n^2)
    # Memory: O(1)
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        # iterate each number in the array
        # for each number check if target-current_num is found in remaining array
        # if found return indices of both the numbers
        
        for i in range(len(nums)):
            num_to_found = target - nums[i]
            for j in range(i+1, len(nums)):
                if num_to_found == nums[j]:
                    return [i, j]
        # This will not reach here
        return None 
      
    
    # Time: O(n)
    # Memory: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary with key as the number 
        # and value as the index of the number in the array
        # iterate each number in the array and check target-current_num is found in the dictionary
        # if found check if current_num index is not equal to this number's index
        # if yes, then return indices of both the numbers
        
        num_to_index = {}
        for i in range(len(nums)):
            num_to_index[nums[i]] = i
        
        for i in range(len(nums)):
            current_num = nums[i]
            num_to_found = target - current_num
            if num_to_found in num_to_index and num_to_index[num_to_found] != i:
                return [i, num_to_index[num_to_found]]
        
        # This will not reach here
        return None
        

if __name__ == '__main__':
  nums = [1, 2, 3, 4, 5]
  target = 9
  print(Solution().twoSum(nums, target))

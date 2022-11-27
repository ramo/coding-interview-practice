# https://leetcode.com/problems/maximum-subarray/submissions/
# 53. Maximum Subarray
# Given an integer array nums, find the subarray which has the largest sum and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:

# Input: nums = [1]
# Output: 1

# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23

# Constraints:

#     1 <= nums.length <= 105
#     -104 <= nums[i] <= 104


# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

from typing import List

class Solution:
    
    # if all numbers are negative
    # then return max(nums)

    # if all numbers are positive
    # then return sum(nums)

    # if numbers are mixed (both positive and negative)
    # then we need to apply some other logic
    
    
    # Time: O(n^2)
    # Memory: O(1)
    def maxSubArray1(self, nums: List[int]) -> int:
        # using brutforce, we will check the sum of all the subarrays
        # and return the maximum sum.
        # iterate each element in array
        # start from that index and go till end of array and find the current_sum and max_sum
        # do this for every index of the array. return the max_sum finally.
        pass
    
    
    # Time: O(n)
    # Memory: O(n)
    def maxSubArray(self, nums: List[int]) -> int:
        pass    
        # [-2,1,-3,4,-1,2,1,-5,4]

        # [-2, 1, -2, 4, 3, 5, 6, 1, 5]   ans = 6
        # [-2, 1, -3, 4, -1, 2, 1, -5, 4]        

        # [5,4,-1,7,8]

        # max_sum [5, 9, 8, 15, 23]  ans = 23
        # temp_array [5, 4, -1, 7, 8]
        
        # iterate each element in array
        # store the maximum sum till this number in max_sums array (dp)
        # in each index, check if the previous maximum sum + current_number < current number
        # we can ignore the previous max sum and put the current number as max sum for this index
        # otherwise add the current number to prev_max_sum and put that as max sum for this index
        # finally after iterating the whole array and creating the max_sums array (dp)
        # return max(max_sums) (returning the maximum value in the max_sums array)
        
        max_sums = [0] * len(nums)
        max_sums[0] = nums[0]
        for i in range(1, len(nums)):
            max_sums[i] = max(nums[i], max_sums[i-1] + nums[i])
        return max(max_sums)


if __name__ == "__main__":
    solution = Solution()
    nums = [1,3,4,5,6,7,8]
    result = solution.maxSubArray(nums)
    print(result)


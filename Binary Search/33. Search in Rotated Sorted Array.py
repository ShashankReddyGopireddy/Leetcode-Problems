"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
You may assume no duplicate exists in the array.
Example 1:
Input: [3,4,5,1,2] 
Output: 1
Example 2:
Input: [4,5,6,7,0,1,2]
Output: 0
s
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        s
        """
        # // Time Complexity = O(logN)
        # // Space Complexity = O(1)
        left = 0
        right = len(nums)-1
        while(left<right):
            mid = left + (right-left)//2
            if nums[right]>nums[mid]:
                right = mid
            elif nums[right]<= nums[mid]:
                left=mid+1
            elif nums[mid]>nums[left]:
                left=mid
            else:
                right=mid-1
            
                
        return nums[left]

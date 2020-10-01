'''
https://leetcode.com/problems/find-peak-element/
'''
import sys
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:    
        '''
        Compare mid and mid+1 if the mid is greater then move the right to mid and perform the operation else move the left to mid+1 and perform. if the lenght is 1 then return 0 because take the left limit as -infinity and right as - infinity. 
        '''
        # left = 0
        # right = 1
        # len_nums= len(nums)
        # if len(nums)==1:
        #     return 0
        # for i in range(len_nums-1):
        #     if (nums[left]<nums[right]):
        #         left +=1
        #         right=left+1
        #     else:
        #         return left
        # return len_nums-1
        left = 0
        right = len(nums) - 1
        if len(nums)==1:
            return 0
        while(left<right):
            mid = left + (right-left)//2
            if nums[mid] < nums[mid+1]:
                left=mid+1
            else:
                right = mid
        return right
            
            
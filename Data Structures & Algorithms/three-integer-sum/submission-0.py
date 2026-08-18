class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # If the current value is greater than zero, we can't sum to zero 
            # since the array is sorted and all remaining values are positive.
            if a > 0:
                break
            
            # Skip duplicate values for our first pointer (i)
            # to ensure we don't produce duplicate triplets.
            if i > 0 and a == nums[i - 1]:
                continue
            
            # Initialize our two pointers: left and right
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                threeSum = a + nums[l] + nums[r]
                
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # We found a valid triplet
                    res.append([a, nums[l], nums[r]])
                    
                    # Move both pointers inward
                    l += 1
                    r -= 1
                    
                    # Skip duplicates for our left pointer to avoid duplicate triplets
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                        
        return res
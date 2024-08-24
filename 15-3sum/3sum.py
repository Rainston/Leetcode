class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        nums.sort()  # Sort the array
        
        for i in range(len(nums) - 2):
            # Early termination: if the smallest number is greater than 0, no valid triplet exists
            if nums[i] > 0:
                break
            
            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Two-pointer technique
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    arr.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return arr

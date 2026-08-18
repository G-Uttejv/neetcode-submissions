class Solution:
    def trap(self, height: list[int]) -> int:
        # Edge case: if the array is empty, no water can be trapped
        if not height:
            return 0

        # Initialize two pointers at the beginning and end of the array
        left, right = 0, len(height) - 1
        
        # Track the maximum heights seen so far from both sides
        left_max, right_max = height[left], height[right]
        
        trapped_water = 0

        # Move the pointers inward until they meet
        while left < right:
            # We process the side with the smaller maximum height because
            # that is the bottleneck determining how much water can be trapped
            if left_max < right_max:
                left += 1
                # Update the max height seen from the left
                left_max = max(left_max, height[left])
                # Calculate water trapped at the current left position
                trapped_water += left_max - height[left]
            else:
                right -= 1
                # Update the max height seen from the right
                right_max = max(right_max, height[right])
                # Calculate water trapped at the current right position
                trapped_water += right_max - height[right]

        return trapped_water
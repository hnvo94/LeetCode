class Solution:
    def trap(height):
        if not height:
            return 0
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        res = 0
        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]
        return res
    
    test = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap(test))
'''
42. Trapping Rain Water
Time complexity: O(n) - we need to move each point (low and high) one by one through the list
Space complexity: O(1) - we don't generate any space rather than declare high and low point

Note: Very hard and tricky problem. The trick is you can use two pointers technique to maintain the max left and max right wall. The potential amount of water at that index is the 
max left wall value (for example if max left wall is 2, then it means that the potential water can be trapped at that index is 2), then if we subtract the potential amount with the height at that index, you will get the actual amount of water at that index.
Same thing for the right wall.

The key here is that left max and right max keep track of the highest barriers from each side. 
As we move the pointers, we know that water trapped at each position is limited by the smaller of left max and right max.
'''    
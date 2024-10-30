class Solution:
    def maxArea(heights):
        result = 0
        left, right = 0, len(heights) - 1
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            result = max(result, area)
            if  heights[left] > heights[right]:
                right -= 1
            elif heights[left] <= heights[right]:
                left += 1              
        return result
    
    test = [1,8,6,2,5,4,8,3,7]
    print(maxArea(test))

'''
11. Container With Most Water - Medium
Time complexity: O(n) - two pointer technique needs O(n) because we moving both left and right by one each time. 
Space complexity: O(1) we don't use any extra spaces except a result to hold the return value

Note: Tricky part is the condition to move left point and right point. Two pointers technique usually compare the result rather than the value at each point. 
By moving the pointer of the shorter line, you have a chance to increase the minimum height and potentially find a larger area.
If you moved the pointer on the taller line, the new area would either be the same or smaller because the width between the pointers decreases, and you would not get a taller minimum height.

'''  
class Solution:
    #problem: Input is an integer array, output is also an integer array which is production of all element from input array except nums[i] (itself)
    def productExceptSelf(nums):
        result = [1] * len(nums)
        left_product = 1
        #calculate left part  (prefix)
        for i in range(len(nums)):
            result[i] = left_product
            left_product *= nums[i]
        #calculate right part (postfix)
        right_product = 1
        for i in range(len(nums) - 1, -1 , -1): 
            result[i] *= right_product
            right_product  *= nums[i]
        return result

    test = [1,2,3,4]
    print(productExceptSelf(test))
    

'''
238. Product of Array Except Self - Medium
Time complexity: O(n) - 2 for loop through the nums. 
Space complexity: O(1) - we do not make any extra memory scale with size of the problem
   # solution: 
    # 1. we notice that [1,2,3,4] if we want to get the answer for number 3 in that array, it will be 1 * 2 (prefix) * 4(postfix) = 8. So, in order to calculate the output, we have to calculate all the prefix (1), (1 * 2) (1* 2 * 3) then (1 * 2 * 3 * 4)
    # 2. Then we multiple with the postfix (4) * (4 * 3) (4 * 3* 2) (4 * 3 * 2 * 1) (since 1 doesn't have prefix and 4 doesn't have a postfix, we can assume that it is 1)
    # the result can be done with 1 array with size of nums (basically we put the prefix first, then we multiply it with postfix)

'''

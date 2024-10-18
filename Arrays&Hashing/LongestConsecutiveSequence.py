class Solution:
    def longestConsecutive(nums):
        hashset = set(nums)
        result = 0
        for num in nums:
            if num - 1 not in hashset:
                length = 1
                while (num + length) in hashset:
                    length += 1
                result = max(result, length)
        return result

    test = [2,20,4,10,3,4,5]
    print(longestConsecutive(test))

'''
Problem: Leetcode 128. Longest Consecutive Sequence
Time complexity: O(n), each number in the list 
Space complexity: 
    

Note: 
    
'''

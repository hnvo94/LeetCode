class Solution:
    #def containsDuplicate(self, nums: List[int]) -> bool:
    def containsDuplicate(nums):
        hashset = set() #create a hashset
        for i in nums:  #loop through the input nums
            if i in hashset: #If the number is in hashset, return True. If not, add that number i into hashset
                return True
            hashset.add(i)
        return False # Return False if cannot find any duplicates

    nums = [1,2,3,1]
    print(containsDuplicate(nums))

'''
Problem: leetcode 217 Contains Duplicate - Easy
Time complexity: O(n) - Because the worst case is we have to loop thourgh very end of the list to find that duplicate number. And the list has n elements, so that it has O(n) runtime
Space complexity: O(n) - Same as time complexity, because we have to add n elements into the hashset. 

Note: 
    A set is an unordered collection of unique elements. It uses a hash table to store elements, and duplicates are not allowed.
    it supports operations like addition, removal, and lookup in constant time (on average). 
    Common operations include add(), remove(), in to check membership, and set operations like union, intersection, etc.

A simple problem. Other approach could be used such as shorted approach. Sort the list first, then check if the index [i] and [i + 1] have the same value then return True, otherwise return False.
'''
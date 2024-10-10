class Solution:
    #def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(nums, target):
        hashmap = {} 
        for index, num in enumerate(nums): #enumerate the list nums to figure out the index at each element and the element num in list nums
            second_number = target - num #find the second number. 
            if second_number in hashmap and hashmap[second_number] != index: # we have hashmap[second_number] != index because we don't want to select an element twice at the same index
                return [hashmap[second_number], index]
            else:
                hashmap[num] = index
        return 0

    nums = [2,7,11,15]
    target = 9
    print(twoSum(nums, target))
'''
Problem: leetcode 1 Two Sum - Easy
Time complexity: O(n) -  we have to loop thourgh very end of the list to find that duplicate number. And the list has n elements, so that it has O(n) runtime
Space complexity: O(n) - Same as time complexity, because we have to add n elements into the hashmap. 

Note: 
Making sure to check hashmap[second_number] != index, because we don't want to select an element twice at the same index
    
'''
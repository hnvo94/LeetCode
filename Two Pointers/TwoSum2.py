class Solution:
    def twoSum(numbers, target):
        low, high = 0, len(numbers) - 1
        # calculate the sum of numbers[low] and numbers[high]
        while low < high:
            indexSum = numbers[low] + numbers[high]
            # comapre with target
            if indexSum > target:
                high -= 1
            elif indexSum < target:
                low += 1
            else:
                return [low + 1, high + 1] # we want to return as indices 
        return -1


    test = [1,2,3,4]
    target = 3

    print(twoSum(test, target))
'''
167. Two Sum II - Input Array Is Sorted - Medium
Time complexity: O(n) - we need to move each point (low and high) one by one through the list
Space complexity: O(1) - we don't generate any space rather than declare high and low point

Note: Since the question asked us for the indices based 1, the answer needs to add by 1 because the index starts with 1 instead of 0 in their question. 

'''    
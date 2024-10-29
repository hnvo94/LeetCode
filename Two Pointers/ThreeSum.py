class Solution:
    def threeSum(nums):
        nums.sort() # [-4, -1, -1, 0 ,1, 2]
        result = []
        for i in range(len(nums)):
            k = nums[i]
            if k > 0: # because we sorted the list, when k > 0, there is no more pairs for adding them together to get 0
                break
            if i > 0 and k == nums[i - 1]:
                continue   
            low, high = i + 1, len(nums) - 1 #assign low = i + 1 because we want to avoid the duplicate element, if low = i, then nums[i] and nums[low] are the same which is not a good idea
            while low < high:
                if (nums[low] + nums[high]) + k == 0:
                    result.append([nums[low], nums[high], k])
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1 #moving low to avoid duplication
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1 #moving high to avoid duplication
                elif (nums[low] + nums[high]) + k < 0:
                    low += 1
                else:
                    high -= 1
        return result 
            


    test1 = [-1,0,1,2,-1,-4]
    test2 = [0,0,0]
    print(threeSum(test1))
    print(threeSum(test2))

'''
15. 3Sum - Medium
Time complexity: O(n^2) - two pointer technique needs O(n), and we have to apply it to n element (to find the first number) in the list. So it is O(n^2)
Space complexity: O(m) - m is the number of triplet that we need to store in the result. 

Note: Pretty hard problem in my opinion. Sort the list then moving the points to avoid the duplication. Then apply the two pointers technique to solve it. 

'''  
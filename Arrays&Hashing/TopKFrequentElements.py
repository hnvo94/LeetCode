
class Solution:
    def topKFrequent(nums, k): #bucket sort approach
        freq = [[] for i in range(len(nums) + 1)] #making a list freq to store the frequence of the numbers in nums. We need to plus 1 because the first index is useless.(there is no such a number appear 0 times, right?) 
        count = {} #this is a hashmap to count the frequence of a number in nums
        for number in nums: #loop through all num in nums
            count[number] = 1 + count.get(number, 0) #adding num into hashmap and increase the value by 1 each time the number appears. 
        for n, c in count.items(): #for each key (number) and value (the frequency of that number) in hashmap.
            freq[c].append(n) #adding them into the bucket list we created at the beginning. for example, if number 1 appears 3 times. it will be stored in index 3 in freq
        res = []
        for i in range(len(freq) - 1, 0 , -1): # Iterate from highest to lowest frequency
            for n in freq[i]: # check each index from high to low, if there is something in it, add it to the result.
                res.append(n)
                if len(res) == k: # when the length == k, return result.
                    return res
       
                
    test = [1]
    k = 1
    print(topKFrequent(test,  k))

'''
Problem: 347. Top K Frequent Elements - Medium
Time complexity: O(n) -  Even we have a nested loop, but the element in freq[] is exactly one. So, in worst case, we have n unique elements. 
Space complexity: O(n) - We create n + 1 freq and also a hashmap to store n unique elements in worst case. So, technically, this is O(n) space complexity.

Note: 
Bucket sort. Freq list to keep the frequency of each element. highest index is the most frequency 
    
'''
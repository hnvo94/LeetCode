class Solution:
    def maxProfit(prices: list[int]) -> int:
        pointA, pointB = 0, 1
        maxProfit = 0
        while pointB <= len(prices) - 1:
            if prices[pointA] > prices[pointB]:
                pointA = pointB        
            else:
                maxProfit = max(maxProfit, prices[pointB] - prices[pointA])
            pointB += 1
        return maxProfit

    test =[7,6,4,3,1]
    print(maxProfit(test))

'''
121. Best Time to Buy and Sell Stock - Easy 
Time complexity: O(n) - we are using sliding window technique. Moving pointB to the end of the list.
Space complexity: O(1) - we only use fixed memory in this problem

Note: since this is selling and buying stock, we cannot go back to the past to sell stock. So that pointB is always moving forward. Some edge cases may be considered. 
'''  
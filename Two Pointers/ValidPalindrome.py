class Solution:

    def isPalindrome(self, s: str) -> bool:
        low, high = 0, len(s) - 1
        while low < high:
            while low < high and not self.alphaNum(s[low]):
                low += 1
            while high > low and not self.alphaNum(s[high]):
                high -= 1
            if  (s[low]).lower() == (s[high]).lower():
                low += 1 
                high -= 1
            else:
                print("result:", s[low]," and ",s[high])
                return False
        return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
    

    test = "Was it a car or a cat I saw?"
    print(isPalindrome(test))


'''
problem: 125. Valid Palindrome - Easy
Time complexity: O(n) - because we check 1/2 characters on each end. 
Space complexity: O(1) - we don't generate any space rather than declare high and low point

Note: need a method to check if an index in the string is a number or a character (for both lowercase and uppercase)

'''    

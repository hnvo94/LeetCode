class Solution:
    #def isAnagram(self, s: str, t: str) -> bool:
    def isAnagram(s: str, t: str):
        hashmapA = {}
        hashmapB = {}
        if len(s) != len(t): # Obviously, if 2 strings do not have the same length, it won't be an anagram
            return False
        for i in range(len(s)): # Adding each character from s string (or t string) into the hashmap key and increase hashmap value by one. 
            hashmapA[s[i]] = 1 + hashmapA.get(s[i], 0)
            hashmapB[t[i]] = 1 + hashmapB.get(t[i], 0)
        for character in s:
            if hashmapA[character] != hashmapB.get(character, 0): #using hashmapB.get(character,0) to handle the error when the character is in hashmapA but not in hashmapB
                return False
        return True
    
    s = "rat" 
    t = "car"
    print(isAnagram(s, t))

    '''
    problem: Leetcode 242: Valid Anagram - Easy
    Time complexity: O(n) - we have to loop through the length of s and t. So, it is O(2n) or we can simplify it to O(n)
    Space complexity: O(n) - Also, we have to create 2 hashmaps and add those characters into the hashmap.

    Note: Simple question, but it could be solved in other approach depend on what we need
        
    '''
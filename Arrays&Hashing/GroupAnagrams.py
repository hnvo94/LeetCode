from collections import defaultdict


class Solution:
    #def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    def groupAnagrams(strs):
        hashmap = defaultdict(list)   #As the output request to be a list of each group List[List[str]. we need to create a defaultdict where the values are lists
        for word in strs: #for each word in the strs list
            signature = [0] * 26 # this problem allows input as only 26 lowercase letter. So, we can create this "count" to show which word it is. for example [1, 1, 1, 0, ... ,0] means abc
            for character in word: # for each character in each word
                signature[ord(character) - ord("a")] += 1 # ord() will get you the unicode of a character. For example:  ord("a") = 97. If we minus a unicode of a character to ord('a'), we will get the index it on the alphabet 26 letters. for example: ord('a') - ord('a') = 0. ord('b') - ord('a') = 1
            hashmap[tuple(signature)].append(word) # since a list in python is mutable, we cannot use it as the key in hashmap. So, we have to convert it into a inmutable type, in this case is tuple.
        return hashmap.values()       #get all the values from a hashmap.
    
    test = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(test))

'''
Problem: leetcode 49 Group Anagrams - Medium
Time complexity: O(n * m) -  Although we have a nested loop, but the second loop isn't a real nested loop. It just loops through a word's longest length (m)
Space complexity: O(n * m) - In worst case scenario, we have to store n keys (each word is a key) -> O(n) 
    and the hashmap value contains each word in each value of longest length m so O(m * n) 

Note: hashmap key only accept inmutable type (tuple). 
ord() will return the unicode of a character. ord(character) - ord("a") will get you the index of character on the 26 alphabet list
    
'''
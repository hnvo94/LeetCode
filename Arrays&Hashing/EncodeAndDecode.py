'''
String Encode and Decode
Solved 
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
'''

class Solution:
    def encode(strs):
        result = ""
        for i in range(len(strs)):
            result += str(len(strs[i])) + "#" + strs[i]
        return result
    
    def decode(s):
        result = []
        i = 0
        while i < len(s):
            j = i
            if s[j] != "#":
                j += 1
            length = int(s[i: j])
            result.append(s[j + 1 : j + 1 + length]) # j is 1, j + 1 = "n" and j + 1 + length = eet
            i = j + 1 + length
        return result
    
    
    test = ["neet","code","love","you"]
    decodetest = "4#neet4#code4#love4#you"
    print(encode(test))
    print(decode(decodetest))

'''
Problem: leetcode Encode and decode strings - Medium
Time complexity: O(n) - we process each element in the list. both for encode and decode
Space complexity: O(n) - we store n characters into string in encode. In decode, we append n characters into a list. 

Note:
The # is a special delimiter to separate the length from the actual string.
The lengths before the # help in decoding because they allow you to extract each string correctly, even if the string contains the # character.
'''

    
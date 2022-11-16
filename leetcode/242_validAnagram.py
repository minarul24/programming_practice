'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) == len(t):
            hashS = {}
            hashT = {}
            for i in range(len(s)):
                
                if s[i] in hashS:
                    hashS[s[i]] = 1+ hashS.get(s[i])
                else:
                    hashS[s[i]] = 1 + hashS.get(s[i],0)
                    
                if t[i] in hashT:
                    hashT[t[i]] = 1 + hashT.get(t[i])
                else:
                    hashT[t[i]] = 1 + hashT.get(t[i],0)
            
            # print("HashS = ",hashS)
            # print("HashT",hashT)
            result_true = 0
            result_false = 0
            
            for i in hashS:
                # print(i)
                if i in hashS and i in hashT:
                    if hashS[i] == hashT[i]:
                        result_true = 1
                    else:
                        result_false = 1
                else:
                    return False
                    
            
            if result_false==0 and result_true == 1:
                return True
            else:
                return False
            
                    
        
        else:
            return False

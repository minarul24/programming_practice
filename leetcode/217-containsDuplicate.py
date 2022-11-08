'''

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # creates an empty hashmap for storing the value of each key
        result = {}
        
        # iterates through the list
        for i in nums:
            
            # checks if the element is present in the hashmap already or not
            if i in result:
                # returns true if the element is already in the hashmap
                return True
            
            # adds the element to the hashmap if it is not there already
            else:
                result[i] = 1
       
        # returns false if the iteration is complete as there is not any duplicate   
        return False
        

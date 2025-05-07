class Solution:
    def firstUniqChar(self, s: str) -> int:
        key = 'abcdefghijklmnopqrstuvwxyz'  # Pre-defined order of characters
        idx = 10**5  # Set an initial large index
        
        # Iterate through each character in the pre-defined order
        for i in key:
            x = s.find(i)  # Find the first occurrence of the character
            # Check if the character is unique (not found after the first occurrence)
            if x != -1 and x == s.rfind(i):
                idx = min(idx, x)  # Update the minimum index
        
        # Return the minimum index if found, otherwise return -1
        return idx if idx != 10**5 else -1
    
#` Example usage
s = "leetcode"
solution = Solution()
result = solution.firstUniqChar(s)
print(result)  # Output: 0 (index of 'l')`
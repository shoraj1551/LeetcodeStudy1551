from collections import Counter  # Move import to top

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Step 1: Count frequency of each character
        freq = Counter(s)

        # Step 2: Find the first character with count 1
        for idx, char in enumerate(s):
            if freq[char] == 1:
                return idx

        return -1  # If no unique character exists

# Example usage
s = "leetcode"
solution = Solution()
result = solution.firstUniqChar(s)
print(result)  # Output: 0 (index of 'l')
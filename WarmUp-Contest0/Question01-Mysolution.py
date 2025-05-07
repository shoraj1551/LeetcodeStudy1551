# Time: O(n log n) due to sorting strings
# Space: O(n) for list storage and conversions

class Solution:
    def lexicalOrder_My(self, n: int) -> list[int]:
        # Step 1: Generate list of integers from 1 to n
        list_Int = [i + 1 for i in range(n)]
    
        # Step 2: Convert all integers to strings to enable lexicographical sort
        list_Str = sorted([str(i) for i in list_Int])
    
        # Step 3: Convert sorted strings back to integers
        return [int(i) for i in list_Str]

# Example usage:
solution = Solution()
n = 25
result = solution.lexicalOrder_My(n)
print(result)  
# Output: [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25]
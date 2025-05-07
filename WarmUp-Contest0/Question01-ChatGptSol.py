# Time: O(n), each number is visited once
# Space: O(n) for result list + O(log n) recursive stack depth

def lexicalOrder_dfs(n: int) -> list[int]:
    result = []

    # Helper function to perform DFS traversal
    def dfs(curr: int):
        if curr > n:
            return
        result.append(curr)  # Visit the current number
        
        for i in range(10):
            next_num = curr * 10 + i  # Try appending digits 0–9
            if next_num > n:
                break
            dfs(next_num)  # Recurse into next prefix

    # Start DFS from 1 to 9
    for i in range(1, 10):
        dfs(i)

    return result

# Example usage:
n = 25
result = lexicalOrder_dfs(n)
print(result)  
# Output: [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25]

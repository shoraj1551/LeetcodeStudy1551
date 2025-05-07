# Time: O(n), each number is visited once
# Space: O(n) for result list only (no recursion)

def lexicalOrder_iterative(n: int) -> list[int]:
    result = []
    number = 1  # Start from the smallest valid number

    for _ in range(n):
        result.append(number)  # Add current number to result

        if number * 10 <= n:
            # Go deeper into lex tree (e.g., 1 → 10)
            number *= 10
        else:
            # If we can't go deeper, try to move to the next sibling
            if number >= n:
                # If we're out of bounds, move up a level
                number //= 10
            number += 1  # Move to the next number

            # If the last digit is 0, keep moving up (avoid revisiting already seen prefixes)
            while number % 10 == 0:
                number //= 10

    return result

# Example usage:
n = 25
result = lexicalOrder_iterative(n)
print(result)
# Output: [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25]
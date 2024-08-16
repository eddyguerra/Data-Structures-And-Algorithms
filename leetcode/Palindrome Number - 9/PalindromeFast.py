class Solution:
    def isPalindromeFast(self, x: int) -> bool:
        return str(x) == str(x)[::-1]







# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [121, -121, 10]
    results = []

    for x in test_cases:
        result = solution.isPalindromeFast(x)
        results.append(result)

    # Print the results
    for i, x in enumerate(test_cases):
        print(f"Input: x = {x}")
        print(f"Output: {results[i]}")
        print()

"""
Notes:
- The function `isPalindromeFast` checks whether an integer is a palindrome by converting the integer to a string and comparing it with its reverse.
- The `[::-1]` slice notation is used to reverse the string representation of the integer.
- This approach is straightforward and leverages Python's string manipulation capabilities to check for a palindrome.

Time Complexity:
- The time complexity of this approach is O(n), where n is the number of digits in the integer. This is because string conversion and reversal both take linear time relative to the number of digits.

Space Complexity:
- The space complexity is O(n) as well, because the string representation of the number and its reverse both take up space proportional to the number of digits in the integer.

Test Cases:
1. **Input:** x = 121
   **Output:** True
   **Explanation:** 121 reads the same forwards and backwards, so it is a palindrome.

2. **Input:** x = -121
   **Output:** False
   **Explanation:** -121 reads as 121- from right to left, which is not the same as left to right.

3. **Input:** x = 10
   **Output:** False
   **Explanation:** 10 reads as 01 from right to left, which is not the same as left to right.
"""

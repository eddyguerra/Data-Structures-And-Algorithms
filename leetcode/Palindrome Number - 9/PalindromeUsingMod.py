class Solution(object):
    def isPalindromeModDivision(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        div = 1
        while x >= 10 * div:
            div *= 10

        while x:
            right = x % 10  # Get the last digit
            left = x // div  # Get the first digit

            if left != right:
                return False

            # Remove the first and last digits from x
            x = (x % div) // 10
            # Adjust div to remove two digits
            div = div // 100

        return True

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [121, -121, 10]
    results = []

    for x in test_cases:
        result = solution.isPalindromeModDivision(x)
        results.append(result)

    # Print the results
    for i, x in enumerate(test_cases):
        print(f"Input: x = {x}")
        print(f"Output: {results[i]}")
        print()

"""
Notes:
- The function `isPalindromeModDivision` checks whether an integer is a palindrome by comparing digits from both ends towards the center using modular arithmetic.
- It first identifies the highest power of 10 that is less than or equal to the number (`div`) to isolate the leftmost digit.
- The rightmost digit is isolated using the modulo operation (`x % 10`).
- The function compares the leftmost and rightmost digits. If they are different, the number is not a palindrome.
- After each comparison, the function removes the compared digits from both ends and continues the process until all digits are checked.

Time Complexity:
- The time complexity of this approach is O(log10(n)), where n is the value of the integer. This is because the number of digits in the integer determines the number of iterations, and each iteration reduces the number by two digits.

Space Complexity:
- The space complexity is O(1), as the function uses only a constant amount of extra space for variables.

Test Cases:
1. **Input:** x = 121
   **Output:** True
   **Explanation:** 121 reads the same forwards and backwards, so it is a palindrome.

2. **Input:** x = -121
   **Output:** False
   **Explanation:** Negative numbers are not palindromes because the negative sign makes the number read differently forwards and backwards.

3. **Input:** x = 10
   **Output:** False
   **Explanation:** 10 reads as 01 from right to left, which is not the same as left to right.
"""

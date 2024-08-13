
# Palindrome Number Check Using Modular Division

## Abstract
In this document, we explore an efficient algorithm to determine if a given integer is a palindrome. The method avoids converting the integer to a string, instead leveraging modular arithmetic to perform digit-wise comparisons from both ends of the number.

## 1. Introduction
A palindrome is a number that reads the same forward and backward. Traditional approaches often convert the number into a string to compare its characters. However, this paper introduces a method that checks for palindromes using modular arithmetic, which is more space-efficient and avoids string manipulation.

## 2. Algorithm Description
The `isPalindromeModDivision` function checks if a given integer is a palindrome by comparing digits from the leftmost and rightmost ends of the number. The process involves the following steps:

1. **Negative Check:** If the input integer `x` is negative, it is immediately identified as not being a palindrome since negative signs do not have a counterpart when reading backwards.
2. **Divisor Determination:** The function calculates the largest power of 10 (`div`) that is less than or equal to `x`, which helps in isolating the leftmost digit.
3. **Digit Comparison:** The function compares the leftmost digit (obtained via integer division) and the rightmost digit (obtained via modulo operation). If they are not equal, the number is not a palindrome.
4. **Digit Removal:** After each comparison, the leftmost and rightmost digits are removed, and the divisor is adjusted accordingly.
5. **Iteration:** The process repeats until all digits have been compared.

## 3. Implementation
The following Python implementation captures the above-described algorithm:

```python
class Solution(object):
    def isPalindromeModDivision(self, x):
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
```

## 4. Complexity Analysis
### 4.1 Time Complexity
The time complexity of the `isPalindromeModDivision` function is O(log10(n)), where `n` is the value of the integer. This complexity arises because the algorithm iterates through the digits of the number, and the number of digits is proportional to the logarithm of the number itself.

### 4.2 Space Complexity
The space complexity is O(1), as the function only uses a constant amount of extra space, regardless of the input size.

## 5. Example Usage and Results
The function can be tested with several inputs to validate its correctness:

```python
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
```
### Test Cases
1. **Input:** x = 121  
   **Output:** True  
   **Explanation:** 121 reads the same forwards and backwards, so it is a palindrome.

2. **Input:** x = -121  
   **Output:** False  
   **Explanation:** Negative numbers are not palindromes because the negative sign makes the number read differently forwards and backwards.

3. **Input:** x = 10  
   **Output:** False  
   **Explanation:** 10 reads as 01 from right to left, which is not the same as left to right.

## 6. Conclusion
The `isPalindromeModDivision` function provides an efficient and space-saving method to determine if a number is a palindrome. By avoiding string conversion and using modular arithmetic, this method is particularly well-suited for environments where memory usage is a concern.

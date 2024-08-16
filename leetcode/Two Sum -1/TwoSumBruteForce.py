from typing import List

class Solution:
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No solution found

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Input values
    nums = [2, 7, 11, 15]
    target = 9

    # Call the twoSumBruteForce method with the example input
    result = solution.twoSumBruteForce(nums, target)

    # Print the result
    print(f"Indices of numbers that add up to {target}: {result}")

"""
Notes:
- This implementation uses a brute-force approach to find the two indices that add up to the target.
- The method iterates through each pair of elements in the list `nums` using two nested loops.
- For each element at index `i`, it checks all subsequent elements at index `j` to see if their sum equals the target.

Time Complexity:
- The time complexity of this approach is **O(n^2)**, where `n` is the number of elements in the list.
- This is because for each element `i`, the inner loop runs for `n - i - 1` times, leading to a quadratic number of comparisons.
- This approach is not the most efficient for large input sizes due to the quadratic time complexity.

Space Complexity:
- The space complexity is **O(1)**, which means it uses constant additional space.
- The method only uses a few integer variables (`i`, `j`, and `n`) and does not require any additional data structures proportional to the input size.

Summary:
- This brute-force method is straightforward and easy to understand, but it is not optimal for large datasets due to its O(n^2) time complexity.
- In cases where efficiency is important, other methods such as using a hash map (dictionary) or the two-pointer technique may be preferred.
"""

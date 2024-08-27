class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one = 1
        two = 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one

# Example usage
if __name__ == "__main__":
    solution = Solution()
    n = 5  # Number of stairs
    result = solution.climbStairs(n)
    print(f"The number of ways to climb {n} stairs is: {result}")

"""
Notes:

1. Algorithm Explanation:
   - The solution is based on a dynamic programming approach where the number of ways to reach
     the `n`th step is the sum of the ways to reach the `(n-1)`th step and the `(n-2)`th step.
   - This approach effectively calculates the Fibonacci sequence for `n` steps.

2. Variable Explanation:
   - `one`: Tracks the number of ways to reach the current step.
   - `two`: Tracks the number of ways to reach the previous step.
   - `temp`: Temporarily stores the value of `one` during the update process.

3. Loop Execution:
   - The loop runs `n-1` times because the initial step (step 1) and the second step (step 2) are
     both initialized with a value of 1. We already know how to reach the first and second steps,
     so the loop only needs to calculate the number of ways to reach from the third step to the `n`th step.

4. Time Complexity:
   - The time complexity is **O(n)**, where `n` is the number of steps. This is due to the single loop
     that iterates `n-1` times.

5. Space Complexity:
   - The space complexity is **O(1)**, as the algorithm uses a constant amount of extra space (three variables: `one`, `two`, and `temp`).
"""

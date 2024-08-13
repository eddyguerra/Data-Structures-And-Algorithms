class Solution(object):
    def twosumhash(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store the value and its corresponding index in the list
        map = {}

        # Iterate through the list with index and value
        for i, n in enumerate(nums):
            # Calculate the difference needed to reach the target
            diff = target - n

            # If the difference exists in the map, return the indices
            if diff in map:
                return [map[diff], i]

            # Store the current number and its index in the map
            map[n] = i


# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Input values
    nums = [2, 7, 11, 15]
    target = 9

    # Call the twosum method with the example input
    result = solution.twosumhash(nums, target)

    # Print the result
    print(f"Indices of numbers that add up to {target}: {result}")

"""
Notes:
- The algorithm iterates through the list of numbers exactly once, making it an O(n) operation, where n is the number of elements in the list.
- The map dictionary provides O(1) average-time complexity for lookups and insertions.
- Overall, the time complexity of this solution is O(n), which is efficient for this problem as it only requires a single pass through the input list.
- This solution is optimal for cases where the list contains distinct elements and there is exactly one solution. The space complexity is also O(n) due to the additional storage required for the map dictionary.
"""

class Solution(object):
    def twoSum2Pointer(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums) - 1  # Initialize two pointers

        while l < r:
            curSum = nums[l] + nums[r]  # Calculate the current sum of the two pointers

            if curSum > target:
                r -= 1  # Move the right pointer to the left if the current sum is greater than the target
            elif curSum < target:
                l += 1  # Move the left pointer to the right if the current sum is less than the target
            else:
                return [l, r]  # Return the indices if the sum matches the target
        return []

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Input values
    nums = [2, 7, 11, 15]
    target = 9

    # Call the twoSum2Pointer method with the example input
    result = solution.twoSum2Pointer(nums, target)

    # Print the result
    print(f"Indices of numbers that add up to {target}: {result}")

"""
Notes:
- This `twoSum2Pointer` solution assumes that the input list `nums` is sorted. If it is not sorted, the list must be sorted first, which would add an O(n log n) complexity for the sorting step.
- The main operation of the two-pointer approach is O(n), where n is the number of elements in the list. This is because each pointer only moves from one end of the list to the other, and they each traverse the list only once.
- Thus, if the list is already sorted, the overall time complexity of the algorithm is O(n).
- If sorting is required, the total time complexity becomes O(n log n) due to the sorting step.
- The space complexity is O(1) because no additional space is required other than a few variables (pointers and temporary storage for indices).
"""

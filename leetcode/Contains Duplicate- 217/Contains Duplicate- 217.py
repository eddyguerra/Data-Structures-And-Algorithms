from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    nums1 = [1, 2, 3, 3]
    print(solution.hasDuplicate(nums1))  # Output: True

    # Example 2:
    nums2 = [1, 2, 3, 4]
    print(solution.hasDuplicate(nums2))  # Output: False

# Notes:
# Time Complexity: O(n) - where 'n' is the length of the input list 'nums'.
# The function iterates through each element of the list once, and the average
# time complexity of checking and adding elements to a hash set is O(1).

# Space Complexity: O(n) - The space complexity is O(n) because, in the worst-case scenario,
# all elements in the input list 'nums' are unique, and thus, the hash set will contain 'n' elements.

# Duplicate Integer

**Problem**  
Given an integer array `nums`, return `true` if any value appears more than once in the array, otherwise return `false`.

## Example

**Example 1:**

- **Input:** `nums = [1, 2, 3, 3]`
- **Output:** `true`

**Example 2:**

- **Input:** `nums = [1, 2, 3, 4]`
- **Output:** `false`

## Algorithm Explanation

To solve the problem of detecting duplicate integers in an array, the algorithm uses a hash set (`hashset`). The algorithm iterates over each element in the input list `nums`. For each element `n`, the following steps are performed:

1. **Check if `n` is already in `hashset`:**  
   If `n` is found in the hash set, it indicates that the value has appeared before in the array. In this case, the function returns `true`, as a duplicate is found.

2. **Add `n` to `hashset`:**  
   If `n` is not found in the hash set, it is added to the set. This operation is efficient, with an average time complexity of O(1).

3. **Continue until all elements are processed:**  
   If no duplicates are found after processing all elements in the array, the function returns `false`.

## Code

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
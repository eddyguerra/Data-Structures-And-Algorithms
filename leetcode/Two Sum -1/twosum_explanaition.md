
# Two Sum Problem: Comprehensive Explanation of Three Approaches

The Two Sum problem is a classic algorithmic challenge often encountered in coding interviews and competitive programming. The objective is to find two numbers in a list that add up to a given target value. This document explains three different approaches to solving the Two Sum problem: the Hash Map approach, the Two-Pointer approach, and the Brute-Force approach.

## Approach 1: Hash Map

### Algorithm Explanation

The Hash Map approach uses a dictionary (hash map) to store each number in the list and its corresponding index. As you iterate through the list, calculate the difference between the target and the current number. If this difference is already in the hash map, you've found your two numbers, and you can return their indices.

### Python Implementation

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
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
```

### Time Complexity

- **Time Complexity: O(n)**  
  The algorithm iterates through the list exactly once, making it a linear time operation. Dictionary lookups and insertions are O(1) on average, leading to an overall time complexity of O(n), where `n` is the number of elements in the list.

- **Space Complexity: O(n)**  
  The space complexity is O(n) due to the extra storage required for the hash map (dictionary), which stores up to `n` elements in the worst case.

### Summary

The Hash Map approach is efficient and optimal for this problem, offering O(n) time complexity. It's a preferred solution when working with large datasets where performance is a concern.

---

## Approach 2: Two-Pointer

### Algorithm Explanation

The Two-Pointer approach assumes that the input list is sorted. If the list is not sorted, it must be sorted first. The method involves two pointers, one starting at the beginning of the list (`l`) and the other at the end (`r`). The sum of the two numbers pointed to by these pointers is compared to the target. If the sum is greater than the target, the right pointer (`r`) is moved leftward; if the sum is less than the target, the left pointer (`l`) is moved rightward. The process continues until the sum equals the target.

### Python Implementation

```python
class Solution:
    def twoSum2Pointer(self, nums: List[int], target: int) -> List[int]:
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
```

### Time Complexity

- **Time Complexity: O(n)** (if the list is already sorted)  
  The method iterates through the list once using two pointers (`l` and `r`), making it a linear time operation.

- **Time Complexity: O(n log n)** (if the list needs to be sorted)  
  If the list is unsorted, sorting the list requires O(n log n) time. After sorting, the two-pointer technique runs in O(n) time.

- **Space Complexity: O(1)**  
  The space complexity is constant, O(1), because no additional space proportional to the input size is used, only a few variables (pointers and temporary storage for indices).

### Summary

The Two-Pointer approach is efficient if the input list is sorted or can be sorted efficiently. It is especially useful for scenarios where additional space usage should be minimized.

---

## Approach 3: Brute-Force

### Algorithm Explanation

The Brute-Force approach checks every possible pair of numbers in the list to see if they add up to the target. This is done using two nested loops, where the outer loop picks the first number, and the inner loop checks all the numbers after it to find a match.

### Python Implementation

```python
class Solution:
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No solution found
```

### Time Complexity

- **Time Complexity: O(n^2)**  
  The time complexity is quadratic, O(n^2), because for each element in the list, the algorithm checks all subsequent elements. This results in `n * (n - 1) / 2` comparisons, which is a significant amount of work for large lists.

- **Space Complexity: O(1)**  
  The space complexity is constant, O(1), as this approach only uses a fixed amount of extra space for variables (`i`, `j`, and `n`).

### Summary

The Brute-Force approach is straightforward and easy to implement. However, its O(n^2) time complexity makes it inefficient for large datasets. It is generally not recommended when performance is a concern, but it serves as a good starting point for understanding the problem.

---

## Conclusion

All three approaches solve the Two Sum problem, but they differ significantly in terms of efficiency and use cases:

- **Hash Map Approach**: Offers the best performance with O(n) time complexity and is ideal for large datasets.
- **Two-Pointer Approach**: Efficient for sorted lists or when minimal space usage is required, with O(n) time complexity if the list is already sorted.
- **Brute-Force Approach**: Simple and easy to understand but inefficient for large datasets due to its O(n^2) time complexity.

Choosing the right approach depends on the specific requirements of your problem, such as the size of the dataset and the importance of execution time.

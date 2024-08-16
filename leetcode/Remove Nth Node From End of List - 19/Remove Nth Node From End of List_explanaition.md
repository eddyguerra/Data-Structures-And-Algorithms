
# Remove Nth Node From End of List

This guide explains how to implement the algorithm to remove the nth node from the end of a linked list. The solution is written in Python, utilizing the `ListNode` class to represent the linked list nodes.

## Problem Statement

Given the head of a linked list, remove the nth node from the end of the list and return its head.

### Example 1

![Remove Nth Node Example](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

**Input:**
- head = [1, 2, 3, 4, 5]
- n = 2

**Output:**
- [1, 2, 3, 5]

## Code Implementation

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Create a dummy node that points to the head
        dummy = ListNode(0)
        dummy.next = head
        first = second = dummy
        
        # Move the first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next
        
        # Move both pointers until the first one reaches the end
        while first:
            first = first.next
            second = second.next
        
        # Skip the nth node from the end
        second.next = second.next.next
        
        # Return the head of the modified list
        return dummy.next
```

### Explanation:
- **ListNode Class**: The `ListNode` class is used to create nodes in the linked list, where each node contains a value (`val`) and a pointer to the next node (`next`).
- **removeNthFromEnd Method**: This method removes the nth node from the end of the list. It uses two pointers (`first` and `second`). The `first` pointer is moved `n+1` steps ahead so that the gap between `first` and `second` is `n` nodes. Both pointers are then moved simultaneously until `first` reaches the end. At this point, `second` will be just before the node that needs to be removed, and the removal is performed by adjusting the `next` pointer of `second`.

### Example Usage

```python
# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Helper functions to create and display linked lists
    def create_linked_list(lst):
        head = ListNode(lst[0])
        current = head
        for value in lst[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    def print_linked_list(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        print(result)

    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5], 2),
        ([1], 1),
        ([1, 2], 1)
    ]

    for lst, n in test_cases:
        head = create_linked_list(lst)
        new_head = solution.removeNthFromEnd(head, n)
        print(f"Input: head = {lst}, n = {n}")
        print("Output:", end=" ")
        print_linked_list(new_head)
        print()
```

### Test Cases

1. **Input:** head = [1, 2, 3, 4, 5], n = 2
   - **Output:** [1, 2, 3, 5]
   - **Explanation:** The list after removing the 2nd node from the end is [1, 2, 3, 5].

2. **Input:** head = [1], n = 1
   - **Output:** []
   - **Explanation:** The list has only one node, which is removed, resulting in an empty list.

3. **Input:** head = [1, 2], n = 1
   - **Output:** [1]
   - **Explanation:** The list after removing the last node (2) is [1].

## Complexity Analysis

- **Time Complexity:** O(L), where L is the length of the linked list. The list is traversed twice—once to move the `first` pointer, and once to remove the nth node.
- **Space Complexity:** O(1), as the function only uses a constant amount of extra space for pointers.

This solution is efficient and handles edge cases, such as removing the first node or the only node in the list, by using a dummy node.

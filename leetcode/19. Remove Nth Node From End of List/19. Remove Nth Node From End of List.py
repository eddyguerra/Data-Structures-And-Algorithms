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


"""
Notes:
- The function `removeNthFromEnd` removes the nth node from the end of a linked list.
- It uses two pointers (`first` and `second`). The `first` pointer is moved `n+1` steps ahead, so that the gap between the `first` and `second` pointers is exactly `n` nodes.
- Both pointers then move simultaneously until `first` reaches the end of the list. At this point, `second` points to the node just before the one that needs to be removed.
- The `second.next` pointer is adjusted to skip the nth node from the end.
- A dummy node is used to handle edge cases such as removing the first node of the list.

Time Complexity:
- The time complexity of this approach is O(L), where L is the length of the linked list. This is because the list is traversed twice, once to move the `first` pointer and once to remove the nth node.

Space Complexity:
- The space complexity is O(1), as the function uses only a constant amount of extra space for pointers.

Test Cases:
1. **Input:** head = [1, 2, 3, 4, 5], n = 2
   **Output:** [1, 2, 3, 5]
   **Explanation:** The list after removing the 2nd node from the end is [1, 2, 3, 5].

2. **Input:** head = [1], n = 1
   **Output:** []
   **Explanation:** The list has only one node, which is removed, resulting in an empty list.

3. **Input:** head = [1, 2], n = 1
   **Output:** [1]
   **Explanation:** The list after removing the last node (2) is [1].
"""
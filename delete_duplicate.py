# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: ListNode) -> ListNode:
    # Dummy node to handle edge cases
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    current = head

    while current:
        # Check if current node is the start of duplicates
        if current.next and current.val == current.next.val:
            # Skip all nodes with the same value
            while current.next and current.val == current.next.val:
                current = current.next
            # Link prev to the node after duplicates
            prev.next = current.next
        else:
            # Move prev forward if current is unique
            prev = prev.next
        current = current.next

    return dummy.next

# Helper function to print the linked list


def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)


# Example usage:
head = ListNode(1, ListNode(2, ListNode(
    3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
new_head = deleteDuplicates(head)
print_list(new_head)  # Output: [1, 2, 5]

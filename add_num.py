class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry
            carry = total // 10

            curr.next = ListNode(total % 10)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


def build_list(nums):
    dummy = ListNode()
    curr = dummy
    for v in nums:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def print_list(nodes):
    vals = []
    while nodes:
        vals.append(str(nodes.val))
        nodes = nodes.next
    return "->".join(vals)


def build_list_from_num(num):
    if num < 10:
        return ListNode(num)
    val = num % 10
    nextNode = build_list_from_num(num // 10)  # use integer division
    current = ListNode(val)
    current.next = nextNode
    return current


l1 = build_list([2, 4, 3])   # Represents number 342
l2 = build_list([5, 6, 4])   # Represents number 465

solution = Solution()
result = solution.addTwoNumbers(l1, l2)


print("Input l1: 2 -> 4 -> 3 (342)")
print("Input l2: 5 -> 6 -> 4 (465)")
print("Result (807):")
print_list(result)

l3 = build_list_from_num(342)   # Represents number 342
print(print_list(l3))
print(print_list(l1))

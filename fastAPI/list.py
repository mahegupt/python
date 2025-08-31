class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    '''Add at end of list'''

    def append(self, val):
        node = Node(val)
        temp = self.head
        if not temp:
            self.head = node
            return

        while (temp.next):
            temp = temp.next
        temp.next = node

    '''Add at start of list'''

    def preappend(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    '''Delete a node by value'''

    def delete(self, val):
        current = self.head
        # If 1st Node to deleted.
        if current.val == val:
            self.head = current.next
            del current
        else:
            # Loop through nodes, find the matching.
            while (current.next and current.next.val != val):
                current = current.next

            # If node found i.e. next node has matching value, deleted it.
            if current.next:
                todelete = current.next
                current.next = current.next.next
                del todelete

    def search(self, val):
        current = self.head
        while (current):
            if current.val == val:
                return True
            current = current.next

        return False

    def reverse(self):
        curr = self.head
        prev = None
        next = curr
        # Adjust the pointers.
        while (curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        # Rebase the head.
        self.head = prev

    def rreverse_helper(self, head):
        if head is None or head.next is None:
            return head

        new_head = self.rreverse_helper(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def recursive_reverse(self):
        self.head = self.rreverse_helper(self.head)

    def print_list(self):
        current = self.head
        while (current):
            print(current.val, end=" -> ")
            current = current.next
        print("None")


ll = LinkList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()
ll.preappend(13)
ll.preappend(15)
ll.preappend(19)
ll.print_list()
ll.delete(1)
ll.print_list()
ll.reverse()
ll.print_list()
ll.recursive_reverse()
ll.print_list()

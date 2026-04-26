class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ExtendedLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # 1. [span_5](start_span)Count nodes[span_5](end_span)
    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    # 2. [span_6](start_span)Find middle using slow and fast pointers[span_6](end_span)
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    # 3. [span_7](start_span)Reverse the list[span_7](end_span)
    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# [span_8](start_span)Execution matching Task 6 Expected Output[span_8](end_span)
ell = ExtendedLinkedList()
for val in [10, 20, 30, 40]:
    ell.insert_at_end(val)

print(f"Number of nodes: {ell.count_nodes()}")
print(f"Middle element: {ell.find_middle()}")

ell.reverse_list()
print("Reversed list:")
ell.display()
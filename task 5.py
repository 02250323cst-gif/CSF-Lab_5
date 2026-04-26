class Node:
    def init(self, data):
        [span_1](start_span)self.data = data # Store data[span_1](end_span)
        [span_2](start_span)self.next = None # Store reference to next node[span_2](end_span)

class LinkedList:
    def init(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return "Element found"
            current = current.next
        return "Element not found"

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# [span_3](start_span)Execution matching Task 5 Sample Output[span_3](end_span)
ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
print("Linked List:")
ll.display()

ll.insert_at_beginning(5)
print("After inserting 5 at beginning:")
ll.display()

ll.delete_node(20)
print("After deleting 20:")
ll.display()

print(f"Search 30: {ll.search(30)}")
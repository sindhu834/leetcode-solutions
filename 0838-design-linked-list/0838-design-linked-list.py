# Define a Node for the singly linked list
class Node:
    def __init__(self, val=0):
        self.val = val       # value of the node
        self.next = None     # pointer to the next node


class MyLinkedList:

    def __init__(self):
        self.head = None     # start of the linked list
        self.size = 0        # keep track of number of nodes

    # Get the value of the index-th node (0-indexed)
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1  # invalid index
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    # Add a new node at the head
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head  # new node points to current head
        self.head = new_node       # update head
        self.size += 1

    # Add a new node at the tail
    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:          # if list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node  # link last node to new node
        self.size += 1

    # Add a node before the index-th node
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return  # invalid index, do nothing
        
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            new_node = Node(val)
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.size += 1

    # Delete the index-th node
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return  # invalid index
        
        if index == 0:
            self.head = self.head.next  # remove first node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next  # skip the deleted node
        
        self.size -= 1

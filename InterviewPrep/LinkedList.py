from nodes import Node

class LinkedList:

    # Function to iniatize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        # Create new node
        new_node = Node(new_data)
        # Make next of new node as head
        new_node.next = self.head
        # Point new node the head node
        self.head = new_node

    def insertAfter(self, prev_node, new_data):

        # Check if the given prev_node exists
        if prev_node is None:
            print("Prev node must be in list")
            return
        
        # Create a new node
        new_node = Node(new_data)
        # Make next of new node as next of prev_node
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def append(self,new_data):
        
        # Create a new node
        new_node = Node(new_data)

        # If the list is empyt, set the node to be the head
        if self.head is None:
            self.head = new_node
            return

        # Else traverse until the last node
        last = self.head 
        while (last.next):
            last = last.next
        
        last.next = new_node

    def printList(self):
        elms = []
        temp = self.head
        
        while temp:
            elms.append(temp.data)
            temp = temp.next
        print(elms)

    def sort(self):
        temp = self.head
        while temp.next!=None:
            if temp.data < temp.next.data:
                temp = temp.next
                print("if")
                print(temp.data)
                
            else:
                temp
                print("else")
                print(temp.data)
                break


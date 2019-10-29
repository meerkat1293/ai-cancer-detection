# from nodes import Node
# from LinkedList import LinkedList

# # Code execution starts here 
# if __name__=='__main__': 
  
#     # Start with the empty list 
#     llist = LinkedList() 
  
#     # Insert 6.  So linked list becomes 6->None 
#     llist.append(6) 
  
#     # Insert 7 at the beginning. So linked list becomes 7->6->None 
#     llist.push(7); 
  
#     # Insert 1 at the beginning. So linked list becomes 1->7->6->None 
#     llist.push(1); 
  
#     # Insert 4 at the end. So linked list becomes 1->7->6->4->None 
#     llist.append(4) 
  
#     # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None 
#     llist.insertAfter(llist.head.next, 8) 
  
#     llist.printList()
#     # llist.sort()
#     # llist.printList()

a = 5
b = 6
print("A is",a,"B is",b)
if a < b:
    a,b = b,a
print("A is",a,"B is",b)

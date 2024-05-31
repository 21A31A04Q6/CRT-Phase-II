class Node:
    def _init_(self, data):
        self.data = data 
        self.next = None 
 
def printLinkedList(head):
    currentNode = head 
    while currentNode != None:
        print(currentNode.data, end = " --> ")
        currentNode = currentNode.next
    print()
 
def insertAthead(head, ele):
    temp = Node(ele)
    if head == None:
        return temp
 
    tail = head 
    while temp.next != None:
        temp = temp.next 
    temp.next = head
    return temp
 
 
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
head = None 
for ele in nums:
    head = insertAthead(head, ele)
    printLinkedList(head)
print("Final linked list is:")
printLinkedList(head)
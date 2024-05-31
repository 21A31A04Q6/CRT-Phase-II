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


def insertAtTail(head, ele):
    temp = Node(ele)
    if head == None:
        return temp
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
    tail.next = temp 
    return head

def deletAtSpecificPosition(head, position):
    
    index = 0 
    currentNode = head 
 
    while index != position - 1:
        index += 1
        currentNode = currentNode.next

        #current node will point to the previous node
    nodetobedelted = currentNode.next 
    nextNode = nodetobedelted.next 


    nodetobedelted.next=None
    currentNode.next= None
    currentNode.next=nextNode
    return head
    

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
head = None 
for ele in nums:
    head = insertAtTail(head, ele)
print("Final linked list is:")
printLinkedList(head)
 
head =deletAtSpecificPosition(head, 3)
printLinkedList(head)
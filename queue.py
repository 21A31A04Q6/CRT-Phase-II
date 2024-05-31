def enqueue(q,ele):
    q.append(ele)
    print(ele,"inserted into queue successfully")

def dequeue(q):
    if len(q) == 0:
        print("queue is empty")
        return
    print(q[0],"deleted successfully")
    q.pop()
q=[]
enqueue(q,10)
enqueue(q,20)
enqueue(q,30)
dequeue(q)

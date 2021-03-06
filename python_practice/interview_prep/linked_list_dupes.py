class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
# With extra storage
def dedup(n):
    if n is None:
        return
    duplicates = set()
    prev = None
    while n is not None:
        if n.data in duplicates:
            prev.next = n.next
        else:
            duplicates.add(n.value)
            prev = n
        n = n.next

# Without extra storage
def dedup2(n):
    while n is not None:
        curr = n
        while curr.next is not None:
            if curr.next.value == n.value:
                curr.next = curr.next.next
            else:
                curr = curr.next
        n = n.next

class Node:
    def __init__(self, value):
        self.value = value
        self.Next = None

def linked_duplicates(node):
    curr = head
    while curr is not None and curr.next is not None:
        while curr.next is not None and curr.data is curr.next.data:
            curr.next = curr.next.next
        curr = curr.next
    return head

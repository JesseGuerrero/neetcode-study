'''
Making a new variable will create a brand new node, pass by value.
Going out of scope of a function will reset the node, pass by value.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printListNode(node : ListNode):
    while node != None:
        print(node.val, end=", ")
        node = node.next


def reverseList(head: ListNode) -> ListNode:
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev

def createListNode(nums : list) -> ListNode:
    listnode = ListNode(nums[0], ListNode())
    temp = listnode.next
    for i, n in enumerate(nums[1:]):
        temp.val = n
        if i < len(nums)-2:
            temp.next = ListNode(n)
            temp = temp.next
    return listnode

node = createListNode([1, 2, 3])
# print(f'{node.val} {node.next.val} {node.next.next.val} {node.next.next.next}')
# printListNode(node)
printListNode(reverseList(node))

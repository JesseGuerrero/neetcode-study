# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

def createListNode(nums : list) -> ListNode:
    listnode = ListNode(nums[0], ListNode())
    temp = listnode.next
    for n in nums[1:]:
        temp.val = n
        temp.next = ListNode(n)
        temp = temp.next
    return listnode

def printListNode(listnode : ListNode):
    while listnode.next != None:
        print(listnode.val, end=", ")
        listnode = listnode.next

listnode = createListNode([1, 2, 3])
printListNode(listnode)
# print(reverseList())
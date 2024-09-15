class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode': # 2
        num1 = 0
        num2 = 0
        i = 0
        j = 0
        while True :
            num1 = num1 + l1.val * pow(10,i)
            i+=1
            l1 = l1.next
            if l1 == None:
                break
        while True:
            num2 = num2 + l2.val * pow(10,j)
            j+=1
            l2 = l2.next
            if l2 == None:
                break
        num1 += num2
        head = ListNode(0)
        tail = head
        while True:
            rem = num1 % 10
            tempnode = ListNode(rem)
            tail.next = tempnode
            tail = tail.next
            num1 = num1 // 10
            if num1 == 0:
                break
        l3 = head.next
        head.next = None
        return l3
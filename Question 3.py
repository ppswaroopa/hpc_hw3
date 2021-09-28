# Question 3

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    def addTwoNumbers(self, first, second):
        prev = None
        temp = None
        carry = 0

        while first is not None or second is not None:

            fdata = 0 if first is None else first.val
            sdata = 0 if second is None else second.val
            Sum = carry + fdata + sdata
            carry = 1 if Sum >= 10 else 0
            Sum = Sum if Sum < 10 else Sum % 10
            temp = ListNode(Sum)

            if self.head is None:
                self.head = temp
            else:
                prev.next = temp

            prev = temp

            if first is not None:
                first = first.next
            if second is not None:
                second = second.next

        if carry > 0:
            temp.next = ListNode(carry)

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_in = current.next
            current.next = prev
            prev = current
            current = next_in
        self.head = prev

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.val)
            temp = temp.next


ll_first = Solution()
ll_second = Solution()

# Create first list
ll_first.push(6)
ll_first.push(4)
ll_first.push(9)
ll_first.push(5)
ll_first.push(7)
print("First List is ")
ll_first.printList()

# Create second list
ll_second.push(4)
ll_second.push(8)
print( "\nSecond List is ")
ll_second.printList()

# Add the two lists and see result
res = Solution()
res.addTwoNumbers(ll_first.head, ll_second.head)
print("\nResultant list is ")
res.printList()

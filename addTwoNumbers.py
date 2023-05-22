# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        empty_head_node = ListNode(0)
        currentNode = empty_head_node
        #carryArray = [False] * n
        i = (carryArray.size-1)
        p = l1
        q = l2

        p, q, currentNode = l1, l2, sumListHeadNode
        carry = 0

        while p is not None or q is not None:
            
            #handle overflow
            if (p.val + q.val < 10):
                currentNode.val = p.val += q.val
            else:
                carryAray[i] = True
                #mod 10 returns remainder after 10 division, for carry case
                currentNode.val = p.val + q.val % 10

            #create next node, and set current node to next node
            #use tuple unpacking
            #p, q, currentNode = p.next, q.next, currentNode.next
            currentNode.next = ListNode(0)
            currentNode = currentNode.next
            p = p.next
            q = q.next

        currentNode = sumListHeadNode
        for i in range(carryArray.size,-1):
            #increment each value associated with a carry bit in our array
            if carryArray[i] == True:
                #increment node by one
                currentNode.val += 1
            currentNode = currentNode.next

        return (sumListHeadNode)

# by Said AKÇA

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = carry + x + y
            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        if carry > 0:
            current.next = ListNode(carry)
            
        return dummy_head.next

def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for number in lst[1:]:
        current.next = ListNode(number)
        current = current.next
    return head

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

solution = Solution()

l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
result = solution.addTwoNumbers(l1, l2)
print(f"Example 1: {linked_list_to_list(result)}")  # Should print [7, 0, 8]

l1 = create_linked_list([0])
l2 = create_linked_list([0])
result = solution.addTwoNumbers(l1, l2)
print(f"Example 2: {linked_list_to_list(result)}")  # Should print [0]

l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])
result = solution.addTwoNumbers(l1, l2)
print(f"Example 3: {linked_list_to_list(result)}")  # Should print [8, 9, 9, 9, 0, 0, 0, 1]

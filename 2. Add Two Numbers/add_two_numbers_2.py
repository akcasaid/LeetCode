# # by Said AKÇA
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        total = l1.val + l2.val + carry
        carry = total // 10
        result_list = ListNode(total % 10)
        current = result_list
        
        l1 = l1.next
        l2 = l2.next
        
        while l1 or l2 or carry:
            total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
                    
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return result_list


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
print(f"Example 1: {linked_list_to_list(result)}") 

# Example 2
l1 = create_linked_list([0])
l2 = create_linked_list([0])
result = solution.addTwoNumbers(l1, l2)
print(f"Example 2: {linked_list_to_list(result)}")  
# Example 3
l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])
result = solution.addTwoNumbers(l1, l2)
print(f"Example 3: {linked_list_to_list(result)}") 

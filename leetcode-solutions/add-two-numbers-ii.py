class Solution:
    def addTwoNumbers(self, l1, l2) -> Optional[ListNode]:

        h1 = None
        while l1:
            temp = l1
            l1 = l1.next
            temp.next = h1
            h1 = temp

        h2 = None
        while l2:
            temp = l2
            l2 = l2.next
            temp.next = h2
            h2 = temp

        total = 0
        head = None
        while h1 and h2:
            total += h1.val + h2.val
            h1 = h1.next
            h2 = h2.next
            temp = ListNode(total%10)
            temp.next = head
            head = temp
            total //= 10
        
        while h1:
            total += h1.val
            h1 = h1.next
            temp = ListNode(total%10)
            temp.next = head
            head = temp
            total //= 10
        
        while h2:
            total += h2.val
            h2 = h2.next
            temp = ListNode(total%10)
            temp.next = head
            head = temp
            total //= 10
        
        if total:
            temp = ListNode(total%10)
            temp.next = head
            head = temp
        
        return head
        
        


        
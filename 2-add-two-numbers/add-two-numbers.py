class Solution:
    def addTwoNumbers(self, l1, l2):

        def number_ac(l):
            n = 0
            p = 1

            while l:
                n += l.val * p
                p *= 10
                l = l.next

            return n

        n = number_ac(l1) + number_ac(l2)

        if n == 0:
            return ListNode(0)

        dummy = ListNode(0)
        curr = dummy

        while n:
            curr.next = ListNode(n % 10)
            curr = curr.next
            n //= 10

        return dummy.next
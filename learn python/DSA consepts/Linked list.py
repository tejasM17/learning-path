class Listnode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def revrList(self, head):
        prv = None
        cur = head

        while cur:
            print(f"current valu : {cur.val}")

            nxt = cur.next  # next node na save madu

            print(f"saving next : {nxt.val if nxt else None}")

            cur.next = prv  # ulta jodisu

            prv = cur  # prv munde haku
            cur = nxt  # cur munde haku

        return prv  # New head of reversed list


# Build linked list: 1 -> 2 -> 3 -> 4 -> 5
h = Listnode(1)
h.next = Listnode(2)
h.next.next = Listnode(3)
h.next.next.next = Listnode(4)
h.next.next.next.next = Listnode(5)

# Run reversal
Sol = Solution()
rev_head = Sol.revrList(h)

# Print reversed linked list
cur = rev_head
while cur:
    print(cur.val, end=" -> ")
    cur = cur.next

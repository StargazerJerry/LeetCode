class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkList:
    def __init__(self):
        self.head = None

    def CreateLinkList(self, lst):
        if not lst:
            return None

        self.head = ListNode(lst[0])
        cur = self.head
        for val in lst[1:]:
            cur.next = ListNode(val)
            cur = cur.next

        return self.head

    def PrintList(self, root):
        # 1 -> 2 -> 3 -> 4

        cur = root
        result_str = "LinkList = "
        while cur:
            result_str += str(cur.val) + "->"
            cur = cur.next
        result_str += "None"

        print(result_str)

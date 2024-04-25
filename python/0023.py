# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, e in enumerate(lists):
            if e:
                heap.append((e.val, i))
        heapq.heapify(heap)

        head = tail = ListNode()
        while heap:
            val, idx = heapq.heappop(heap)
            node = lists[idx]
            lists[idx] = node.next

            if node.next:
                heapq.heappush(heap, (node.next.val, idx))

            tail.next = node
            tail = node
            tail.next = None

        return head.next

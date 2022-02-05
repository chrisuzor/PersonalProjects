from queue import PriorityQueue


from collections import defaultdict


class Link:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self.next:
            return f"Link({self.val})"
        return f"Link({self.val}, {self.next})"


def merge_k_linked_lists(linked_lists):
    val_to_links = defaultdict(list)
    pq = PriorityQueue()
    for link in linked_lists:
        val_to_links[link.val].append(link)
        pq.put(link.val)
    result = Link(0)
    pointer = result
    while len(val_to_links) != 0:
        min_val = pq.get()
        link = val_to_links[min_val].pop()
        pointer.next = Link(link.val)
        pointer = pointer.next
        if len(val_to_links[min_val]) == 0:
            del val_to_links[min_val]
        if link.next:
            val_to_links[link.next.val].append(link.next)
            pq.put(link.next.val)

    return result.next

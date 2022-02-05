class Link:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self.next:
            return f"Link({self.val})"
        return f"Link({self.val}, {self.next})"


def merge_k_linked_lists(linked_lists):
    copy_linked_lists = linked_lists[:]
    result = Link(0)
    pointer = result
    while any(copy_linked_lists):
        front_vals = [link.val for link in copy_linked_lists if link]
        min_val = min(front_vals)
        for i, link in enumerate(copy_linked_lists):
            if link and link.val == min_val:
                pointer.next = Link(link.val)
                pointer = pointer.next
                copy_linked_lists[i] = link.next

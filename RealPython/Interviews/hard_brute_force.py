class Link:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self.next:
            return f"Link({self.val})"
        return f"Link({self.val}, {self.next})"


def merge_k_linked_lists(linked_lists):
    values = []
    for link in linked_lists:
        while link:
            values.append(link.val)
            link = link.next
    sorted_values = sorted(values)
    result = Link(0)
    pointer = result
    for val in sorted_values:
        pointer.next = Link(val)
        pointer = pointer.next
    return result.next


merge_k_linked_lists([Link(1, Link(2)), Link(3, Link(4))])

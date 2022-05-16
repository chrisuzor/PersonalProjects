class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    previous_node = None
    first_current_node = headOne
    second_current_node = headTwo
    while first_current_node is not None and second_current_node is not None:
        if first_current_node.value < second_current_node.value:
            previous_node = first_current_node
            first_current_node = first_current_node.next
        else:
            if previous_node is not None:
                previous_node.next = second_current_node
            previous_node = second_current_node
            second_current_node = second_current_node.next
            previous_node.next = first_current_node
    if first_current_node is None:
        previous_node.next = second_current_node
    return headOne if headOne.value < headTwo.value else headTwo

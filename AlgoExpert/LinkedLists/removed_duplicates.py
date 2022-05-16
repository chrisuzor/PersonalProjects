class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedListA(linkedList):
    # Write your code here.
    current_node = linkedList
    while current_node is not None:
        nextNode = current_node.next
        while nextNode is not None and nextNode.value == current_node.value:
            nextNode = nextNode.next
        current_node.next = nextNode
        current_node = nextNode

    return linkedList


def removeDuplicatesFromLinkedList(linkedList):
    unique_set = set()
    current_node = linkedList
    while current_node is not None:
        unique_set.add(current_node.value)
        nextNode = current_node.next
        if nextNode is not None and nextNode.value in unique_set:
            nextNode = nextNode.next
            current_node.next = nextNode
        else:
            current_node.next = nextNode
            current_node = nextNode
    return linkedList


linkedList = LinkedList(1)
linkedList.next = LinkedList(1)
linkedList.next.next = LinkedList(3)
linkedList.next.next.next = LinkedList(4)
linkedList.next.next.next.next = LinkedList(4)
linkedList.next.next.next.next.next = LinkedList(4)
linkedList.next.next.next.next.next.next = LinkedList(4)
linkedList.next.next.next.next.next.next.next = LinkedList(5)
linkedList.next.next.next.next.next.next.next.next = LinkedList(6)
linkedList.next.next.next.next.next.next.next.next.next = LinkedList(4)


linkedList = removeDuplicatesFromLinkedList(linkedList)
while linkedList is not None:
    print(linkedList.value)
    linkedList = linkedList.next

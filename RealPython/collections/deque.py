# with deque you can append and pop at both ends of a list at constant time
from collections import deque


class TicketQueueList(object):
    def __init__(self):
        self.lst = []

    def add_person(self, name):
        self.lst.append(name)
        print(f"{name} nas been added to the queue")

    def service_person(self):
        name = self.lst.pop(0)
        print(f"{name} has been serviced")

    def bypass_queue(self, name):
        self.lst.insert(0, name)
        print(f"{name} has bypassed the queue")


class TicketQueueDeque(object):
    def __init__(self):
        self.deque = deque()

    def add_person(self, name):
        self.deque.append(name)
        print(f"{name} nas been added to the queue")

    def service_person(self):
        name = self.deque.popleft()
        print(f"{name} has been serviced")

    def bypass_queue(self, name):
        self.deque.appendleft(name)
        print(f"{name} has bypassed the queue")

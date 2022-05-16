class Queue:
    __slots__ = ["first_stack", "second_stack"]

    def __init__(self):
        self.first_stack = []
        self.second_stack = []

    def enqueue(self, value):
        self.first_stack.append(value)
        self.second_stack = self.first_stack[::-1]

    def dequeue(self):
        self.second_stack.pop()
        self.first_stack = self.second_stack[::-1]

    def process_command(self, line):
        commands = line.split("")
        if commands[0] == 1:
            self.enqueue(int(commands[1]))
        elif commands[0] == 2:
            self.dequeue()
        else:
            print(self.first_stack[0])


queue = Queue()
queue.enqueue(42)
queue.dequeue()
queue.enqueue(14)
queue.enqueue(28)
queue.enqueue(60)
queue.enqueue(78)
queue.dequeue()
queue.dequeue()

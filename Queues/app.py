# FIFO
class Queue:
    def __init__(self):
        self.queue = []
    def __str__(self):
        return str(self.queue)
    def enqueue(self, value):
        return self.queue.append(value)
    def dequeue(self):
        return self.queue.pop()
    def peek(self):
        return self.queue[-1]
    def size(self):
        return len(self.queue)
    def is_empty(self):
        return self.queue == 0

first_queue = Queue()
first_queue.enqueue(10)
first_queue.enqueue(20)
first_queue.enqueue(30)
first_queue.dequeue()
print(first_queue.size())
print(first_queue.is_empty())





print(first_queue)








    
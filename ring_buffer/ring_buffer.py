# Ring Buffer time. 
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pointer = 0
        self.storage = [None] * capacity
    # Append
    def append(self, item):
        self.storage[self.pointer] = item
        self.pointer += 1

        if self.pointer > self.capacity -1:
            self.pointer = 0
    # Get 
    def get(self):
        current = [item for item in self.storage if item is not None]
        return current
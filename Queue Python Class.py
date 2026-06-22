class Queue:

    def __init__(self):
        self.__items = []

    @property
    def items(self):
        return self.__items
    
    def enqueue(self, value):
        self.__items.append(value)

    def deqeue (self):
        if self.is_empty():
            return "Queue is empty...!"
        return self.__items.pop(0)
    
    def is_empty(self):
        return len(self.__items) == 0
    
    def __str__(self):
        return f"Queue: {self.__items}"
    
    def front(self):
        if self.is_empty():
            return "Queue is empty...!"
        return self.__items[0]

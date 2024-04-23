class Queue:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)
    
    def enqueue(self,item):
        self._data.insert(0,item)
        return self._data
    
    def dequeue(self):
        if len(self) == 0:
            raise IndexError("The queue is empty.")
        return self._data.pop()
    

class EmptyStackError(Exception):
    pass

class Stack:
    
    def __init__(self):
        self._data = []

    def push(self, a):
        return self._data.append(a)
    
    def is_empty(self):
        if len(self) == 0:
            return True
        else:
            return False
    
    def pop(self):
        if self.is_empty() == True: 
            raise EmptyStackError("The stack is empty.")
        return self._data.pop()
        
    def top(self):
        if self.is_empty() == True: 
            raise EmptyStackError("The stack is empty.")
        return self._data[-1]
    
    def __len__(self):
        return len(self._data)
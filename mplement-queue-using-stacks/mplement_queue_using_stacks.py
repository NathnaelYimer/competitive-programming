class MyQueue:

    def __init__(self):
        self._stack1 = []
        self._stack2 = []
        self._length = 0

    def push(self, x: int) -> None:
        self._stack1.append(x)
        self._length += 1
        return None

    def pop(self) -> int:
        if self._stack2:
            self._length -= 1
            return self._stack2.pop()
        else:
            while self._stack1:
                self._stack2.append(self._stack1.pop())
            if self._stack2:
                self._length -= 1
                return self._stack2.pop()
            else:
                raise Exception()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self._stack2:
            return self._stack2[-1]
        else:
            while self._stack1:
                self._stack2.append(self._stack1.pop())
            if self._stack2:
                return self._stack2[-1]
            else:
                raise Exception()

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not bool(self._length)
        

    

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

from collections import deque

class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        if not self.queue1:
            self.queue1.append(x)
            while self.queue2:
                self.queue1.append(self.queue2.popleft())
        else:
            self.queue2.append(x)
            while self.queue1:
                self.queue2.append(self.queue1.popleft())

    def pop(self) -> int:
        if self.queue1:
            return self.queue1.popleft()
        elif self.queue2:
            return self.queue2.popleft()
        else:
            return None

    def top(self) -> int:
        if self.queue1:
            return self.queue1[0]
        elif self.queue2:
            return self.queue2[0]
        else:
            return None

    def empty(self) -> bool:
        return not self.queue1 and not self.queue2
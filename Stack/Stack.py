from typing import TypeVar, Generic, List, Optional

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self, size: int):
        self.size = size
        self.lst: List[Optional[T]] = [None for _ in range(size)]
        self.top = 0

    def push(self, item: T) -> None:
        if self.top == self.size:
            raise Exception("Stack is full")
        self.lst[self.top] = item
        self.top += 1

    def pop(self) -> None:
        if self.top == 0:
            raise Exception("Stack is empty")
        self.top -= 1
        self.lst[self.top] = None

    def find(self, value: T) -> Optional[int]:
        for i in range(self.size):
            if self.lst[i] == value:
                return i
        return None

    def at(self, idx: int) -> Optional[T]:
        if idx < 0 or idx > self.size:
            raise Exception("At out of scope")
        return self.lst[idx]

    def peek(self):
        if self.top == 0:
            raise Exception("Stack is empty")
        return self.lst[self.top - 1]

        
if __name__ == "__main__":
    s = Stack(4)
    s.push(1)
    s.push(1)
    s.push(1)
    s.push(1)
    s.pop()
    s.pop()
    s.pop()
    s.pop()

    print(s.top)
    s.peek()
    s.at(2)
    s.find(1)
    print(s.lst)

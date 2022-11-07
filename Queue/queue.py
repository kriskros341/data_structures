# push
# pop
# find -> int
# peek
from typing import List, TypeVar, Generic, Union

T = TypeVar("T")

class Queue(Generic[T]):
    def __init__(self, size: int):
        self.size = size
        self.lst: List[Union[T, None]] = [None for _ in range(size)]
        self.top = 0

    def push(self, item: T) -> None:
        if(self.top >= self.size):
            raise Exception("The queue is full!")
        self.lst[self.top] = item
        self.top += 1

    def pop(self) -> T:
        if self.top == 0:
            raise Exception("The queue is empty!")
        toReturn = self.lst[0]
        for idx in range(self.size-1):
            self.lst[idx] = self.lst[idx+1]
        self.top -= 1
        self.lst[self.top] = None
        if not toReturn:
            raise Exception("Queue cursor out of range")
        return toReturn

    def find(self, saught: T) -> Union[int, None]:
        for idx, val in enumerate(self.lst):
            if val == saught:
                return idx
        return None

    def peek(self) -> Union[T, None]:
        if self.top == 0:
            return None
        toReturn = self.lst[self.top-1]
        return toReturn

    def at(self, idx: int):
        if idx < 0 or idx > self.top:
            return None
        return self.lst[idx]

if __name__ == "__main__":

    q = Queue[int](4)

    q.push(1)
    q.push(1)
    q.push(1)
    q.push(1)
    q.pop()
    q.pop()
    q.pop()
    q.pop()
    q.push(1)
    print(q.lst)
    print(q.peek())
    print(q.at(1))
    print(q.find(1))
    print(q.find(4))

from typing import List, Optional, TypeVar, Generic, Union

T = TypeVar("T")

class PrioQueue(Generic[T]):
    def __init__(self, size: int):
        self.size = size
        self.lst: List[Optional[T]] = [None for _ in range(size)]
        self.prios: List[Optional[int]] = [None for _ in range(size)]
        self.top = 0

    def push(self, value: T, prio: int) -> None:
        if(self.top >= self.size):
            raise Exception("The queue is full!")
        i=0
        # find first with lower prio
        for _ in range(self.size):
            current_prio = self.prios[i]
            if not current_prio:
                break
            if current_prio < prio:
                break
            i += 1
        # shift the rest
        for idx in range(i, self.top):
            self.lst[idx+1] = self.lst[idx]
            self.prios[idx+1] = self.prios[idx]
        # insert element
        self.lst[i] = value
        self.prios[i] = prio
        self.top += 1

    def pop(self) -> T:
        if self.top == 0:
            raise Exception("The queue is empty!")
        toReturn = self.lst[0]
        for idx in range(self.size-1):
            self.lst[idx] = self.lst[idx+1]
            self.prios[idx] = self.prios[idx+1]
        self.top -= 1
        self.lst[self.top] = None
        self.prios[self.top] = None
        if not toReturn:
            raise Exception("Queue cursor out of range")
        return toReturn

    def find(self, saught: T) -> Optional[int]:
        for idx, val in enumerate(self.lst):
            if val == saught:
                return idx
        return None

    def peek(self) -> Optional[T]:
        if self.top == 0:
            return None
        return self.lst[self.top-1]

    def at(self, idx: int) -> Optional[T]:
        if idx < 0 or idx > self.top:
            return None
        return self.lst[idx]
        
if __name__ == "__main__":
    q = PrioQueue[int](4)

    q.push(1, 1)
    q.push(2, 2)
    q.push(3, 1)
    q.push(4, 0)
    print(q.lst)
    print(q.prios)
    q.pop()
    print(q.lst)
    print(q.prios)
    q.pop()
    q.peek()
    q.at(3)
    print(q.lst)
    print(q.prios)
    q.pop()
    print(q.lst)
    print(q.prios)

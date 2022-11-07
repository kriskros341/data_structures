from typing import List, Optional, TypeVar, Generic, Union

T = TypeVar("T")


class LinkedList(Generic[T]):
    class Item():
        def __init__(self, value):
            self.value = value
            self.next: Optional[LinkedList.Item] = None

    def __init__(self, size: int):
        self.size = size
        self.roar: Optional[LinkedList.Item] = None
        self.top = 0

    def print(self):
        roar = self.roar
        if not roar:
            return;
        while roar.next:
            print(roar.value, end=" ")
            roar = roar.next
        print(roar.value)

    def push(self, val: T):
        if self.top == self.size:
            raise Exception("The list is full")
        self.top += 1
        if not self.roar:
            self.roar = LinkedList.Item(val)
            return;
        roar = self.roar
        while roar.next:
            roar = roar.next

        roar.next = LinkedList.Item(val) # type: ignore

    def pop(self, idx: int):
        if idx < 0 or idx > self.size-1:
            raise Exception("list index out of range")
        if self.top == 0:
            raise Exception("The list is empty")
        self.top -= 1
        if self.top == 0:
            self.roar = None
            return
        if idx == 0:
            self.roar = self.roar.next # type: ignore
            return
        prev = None
        roar = self.roar
        i = 1
        while i != idx:
            prev = roar
            roar = roar.next
            i += 1
        prev.next = roar.next

    def find(self, value: T) -> Optional[int]:
        roar = self.roar
        idx = 0
        while roar:
            if roar.value == value:
                return idx
            roar = roar.next
            idx += 1
        return None

    def at(self, idx: int):
        if idx < 0 or idx > self.size-1:
            raise Exception("list index out of range")
        if idx >= self.top:
            return None
        i = 0
        roar = self.roar
        while i != idx:
            roar = roar.next
            i += 1
        return roar.value

    def peek(self):
        return self.at(self.top-1)
        
if __name__ == "__main__":
    l = LinkedList(4)
    l.push(1)
    l.push(2)
    l.push(3)
    l.push(4)
    l.print()
    l.pop(3)
    l.print()
    l.pop(0)
    l.print()
    l.pop(0)
    l.print()
    l.pop(0)
    l.print()
    print(l.top, "/", l.size)
    l.print()

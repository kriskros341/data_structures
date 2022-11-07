from typing import List, Optional, TypeVar, Generic, Union

T = TypeVar("T")


class DoublyLinkedList(Generic[T]):
    class Item():
        def __init__(self, value):
            self.value = value
            self.next: Optional[DoublyLinkedList.Item] = None
            self.prev: Optional[DoublyLinkedList.Item] = None

    def __init__(self, size: int):
        self.size = size
        self.roar: Optional[DoublyLinkedList.Item] = None
        self.back: Optional[DoublyLinkedList.Item] = None
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
        item = DoublyLinkedList.Item(val)
        if not self.roar:
            self.roar = item
            self.back = item
            return;
        item.prev = self.back
        if not self.roar.next:
            self.back = item
            self.roar.next = self.back
            return;
        self.back.next = item # type: ignore
        self.back = item

    def pop(self, idx: int):
        if idx < 0 or idx > self.size-1:
            raise Exception("list index out of range")
        if self.top == 0:
            raise Exception("The list is empty")
        if idx > self.top-1:
            raise Exception("No such element in list")
        self.top -= 1
        if self.top == 0 and idx == 0:
            self.roar = None
            self.back = None
            return;
        if idx == self.top:
            self.back.prev.next = None # type: ignore
            return
        if idx == 0:
            self.roar = self.roar.next # type: ignore
            return;
        i = 0
        roar = self.roar
        while (i != idx):
            roar = roar.next
            i += 1
        roar.prev.next = roar.next

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
        if not self.back:
            raise Exception("The list is empty!")
        return self.back.value
        
if __name__ == "__main__":
    l = DoublyLinkedList(4)
    l.push(1)
    l.push(2)
    l.pop(0)
    l.pop(0)
    l.print()
    print(l.at(3))
    print(l.top, "/", l.size)
    l.print()

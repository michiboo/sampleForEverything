# https://xlinux.nist.gov/dads/HTML/pile.html
#An ordered deque, that is, items may only be added to or removed from the head or the tail.
#An item is added to the head if it is smaller than the current head.
# An item is added to the tail if it is greater than the current tail.
# Items are never inserted into the middle, rather, an additional pile may be created.


class deque_pile():
    def __init__(self):
        self.data = []
        self.size = 0

    def insert(self, val):
        if self.size:
            if val < self.data[0]:
                self.data = [val] + self.data
            elif val > self.data[self.size-1]:
                self.data.append(val)
            else:
                print('create another pile')
        else:
            self.data.append(val)

    def remove_head(self):
        head = self.data[0]
        self.data = self.data[1:]
        self.size -= 1
        return head

    def remove_tail(self):
        tail = self.data[self.size-1]
        self.data = self.data[:self.size-1]
        return tail


if __name__ == "__main__":
    test = deque_pile()
    test.insert(1)
    test.insert(5)
    test.insert(2)
    assert test.remove_head() == 1
    test.insert(2)
    assert test.remove_tail() == 5

class stack():
    def __init__(self):
        self.data = []
        self.size = 0

    def push(self, val):
        self.data.append(val)
        self.size += 1

    def pop(self):
        a = self.data[self.size-1]
        self.data.remove(a)
        self.size -= 1
        return a

    def peek(self):
        return self.data[self.size-1]

    def isempty(self):
        return True if self.size == 0 else False


if __name__ == "__main__":
    test = stack()
    assert test.isempty() is True
    test.push(1)
    test.push(2)
    assert test.peek() == 2
    assert test.pop() == 2
    assert test.isempty() is False

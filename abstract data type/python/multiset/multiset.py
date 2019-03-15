#https://xlinux.nist.gov/dads/HTML/bag.html aka bag
#http://web.engr.oregonstate.edu/~sinisa/courses/OSU/CS261/CS261_Textbook/Chapter08.pdf
from collections import defaultdict


class multiset():
    def __init__(self):
        self.data = defaultdict(lambda: 0)
        self._size = 0

    def add(self, val):
        self.data[val] += 1
        self._size += 1

    def size(self, val='all'):
        if val == 'all':
            return self._size
        return self.data[val]

    def contain(self, val):
        if self.data[val]:
            return True
        return False

    def remove(self, val):
        self._size -= self.data[val]
        del self.data[val]


if __name__ == "__main__":
    test = multiset()
    test.add(1)
    test.add(2)
    test.add(1)
    assert test.size() == 3
    assert test.size(1) == 2
    assert test.contain(3) == False
    test.remove(2)
    assert test.contain(2) == False
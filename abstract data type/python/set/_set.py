import random
class _set():

    def __init__(self):
        self.data = {}
        self.size = 0

    def contain(self, val):
        if val in self.data:
            return True
        return False
        
    def isempty(self):
        if self.size:
            return False
        return True

    def _size(self):
        return self.size

    #return generator
    def iterator(self):
        return (i for i in self.data.keys())

    #return list of value
    def enumerate(self):
        return self.data.keys()

    def build(self, vals):
        for x in vals:
            self.data[x] = None
    
    def add(self, val):
        self.data[val] = None
        self.size += 1
    
    def remove(self, val):
        del self.data[val]
        self.size -= 1

    def pop(self):
        tmp = random.choice(self.data.keys())
        del self.data[tmp]
        self.size -= 1
        return tmp
    
    def map(self,func):
        return (func[i] for i in self.data.keys())

    def filter(self, _filter):
        return (i for i in self.data.keys() if _filter(i))
    
    def equal(self, set2):
        if cmp(self.data,set2):
            return True
        return False

    def clear(self):
        self.data.clear()



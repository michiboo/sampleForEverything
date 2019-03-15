class ht_asso_array():
    # TODO add different collision resolving technique, hash function
    def __init__(self, size, hashFunc=None):
        self.table = [[]] * size
        self.load = 0
        self.bucket = size
        if hashFunc:
            self.hfunc = hashFunc
        else:
            self.hfunc = self.hash_func

    def hash_func(self, val):
        tmp = 0
        for x in str(val):
            tmp += ord(x)
        return tmp % self.bucket
    
    def load_factor(self):
        return self.load / self.bucket

    def add(self, key, val):
        hash = self.hfunc(key) 
        self.table[hash].append([key,val])

    def get(self,key):
        hash = self.hfunc(key)
        for x in self.table[hash]:
            if x[0] == key:
                return x[1]
        
    

    
    



    




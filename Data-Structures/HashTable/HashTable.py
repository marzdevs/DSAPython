
class HashTable:
    def __init__(self):
        # size of list
        self.MAX = 20
        # arr is size of 100, initializing 100 list in arr
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        # for each char in key it gives ASCII char to hash
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    # adds the value to the arr in the index of the hash from get_hash
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val


    def __getitem__(self,key):
        # get the hash for the key which is march 6, and h is 9 after finding ASCII
        h = self.get_hash(key)
        # return the element
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

    def print_table(self):
        for index, item in enumerate(self.arr):
            if item is not None:
                print(f'[{index}] -> {item}')
            else:
                print(f'[{index}] -> Empty')






if __name__ == '__main__':
    t = HashTable()
    #t.get_hash("march 6")
    # adds the key and value into the arr t.add('march 6', 130)
    # calls setitem in dict
    t['march 6'] = 130
    t['march 1'] = 20
    t['march 17'] = 27

    # gets the value t.get('march 6')
    # calls getitem in dict
    t['march 6']
    #del t['march 6']
    t.print_table()


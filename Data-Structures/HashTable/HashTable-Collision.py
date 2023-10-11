
class HashTable:
    def __init__(self):
        # size of list
        self.MAX = 10
        # arr is size of 100, initializing 100 list in arr with empty arr none None
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        # for each char in key it gives ASCII char to hash
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    # adds the value to the arr in the index of the hash from get_hash
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        # index h we have a linked list need to iterate through list to update

        # find if key exists, using enum to iterate through elements
        for idx, element in enumerate(self.arr[h]):
            # length is 2 and element is equal to key
            if len(element)== 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))



    def __getitem__(self,key):
        # get the hash for the key which is march 6, and h is 9 after finding ASCII
        h = self.get_hash(key)
        # searches through the linked list
        for element in self.arr[h]:
            # elemt[0] = march 6, element[1] = 78
            if element[0] == key:
                return print(element[1])

        # return the element


    def __delitem__(self, key):
        h = self.get_hash(key)
        # looks for index, and gets the list using self.arr[h]
        for index, element in enumerate(self.arr[h]):
            # deletes key and its value
            if element[0] == key:
                del self.arr[h][index]


    def print_table(self):
        for index, item in enumerate(self.arr):
            if item is not None:
                print(f'[{index}] -> {item}')
            else:
                print(f'[{index}] -> Empty')






if __name__ == '__main__':
    t = HashTable()
    t["march 6"] = 120
    t["march 6"] = 78
    t["march 8"] = 67
    t["march 9"] = 4
    t["march 17"] = 459

    t['march 6']
    del t["march 17"] # deletes from hashmap
    t.print_table()


class HashSet:
    def __init__(self):
        # set the size and initialize table
        self.size = 10000
        self.table = [None] * self.size

    # create a hashing function using modulo
    def hashing(self, key: int):
        return key % self.size

    # adding values to the hash table using hashing function
    def add(self, key: int):
        hashF = self.hashing(key)
        # check if table is empty
        if self.table[hashF] == None:
            # add a key
            self.table[hashF] = [key]
        else:
            # if key is already present, add key to the bucket (inside list)
            self.table[hashF].append(key)

    # removing values from the table
    def remove(self, key: int):
        hashF = self.hashing(key) 
        # check if table is not empty
        if self.table[hashF] != None:
            # use while loop to check for a key if its in a bucket
            while key in self.table[hashF]:
                # remove the key
                self.table[hashF].remove(key)

    def contains(self, key: int):
        hashF = self.hashing(key)
        if self.table[hashF] != None:
            # check if key is present in the table and return true
            return key in self.table[hashF]
        # else return false
        return False

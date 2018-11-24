class example_iterator:
    def __init__(self, data):
        self.index = 0
        self.data = data

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >=len(self.data):
            raise StopIteration()
        rslt = self.data[self.index]
        self.index +=1
        return rslt

class example_iterable:
    def __init__(self):
        self.data = [1,2,3]

    def __iter__(self):
        return example_iterator(self.data)

class alternate_iterable:
    def __init__(self):
        self.data = [11,22,33]
    
    def __getitem__(self, idx):
        return self.data[idx]

for i in example_iterable():
    print(i)

for i in alternate_iterable():
    print(i)
class CircularBuffer:
    def __init__(self, n):
        self.n = n
        self.list = list()
    
    def add(self, item):
        if len(self.list) >= self.n:
            self.list.pop(0)
            self.list.append(item)
        else:
            self.list.append(item)
    
    def __getitem__(self, index):
        if index >= len(self.list):
            return self.list[self.n]
        else:
            return self.list[index]
    
    def __len__(self):
        if len(self.list) >= self.n:
            return self.n
        else:
            return len(self.list)
        

    

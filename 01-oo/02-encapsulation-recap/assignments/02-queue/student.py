class Queue:
    def __init__(self):
        self.__items = list()
    
    def add(self, item):
        self.__items.append(item)
    
    def next(self):
        guy = self.__items[0]

        self.__items.pop[0]
        return guy
    
    def is_empty(self):
        if len(self.__items) <= 0:
            return True
        else:
            return False

queue = Queue()

queue.add('Alice')   # Alice arrives first
queue.add('Bob')     # Then Bob
queue.add('Charlie') # And Charlie as third

print(queue.next)
# print(queue.__items)



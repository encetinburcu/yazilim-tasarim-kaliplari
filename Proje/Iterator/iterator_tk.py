class iterator:
    def __init__(self, limit):
        self.limit = limit
        self.numaralar = [1,2,3,4,5,6,7,8,9]
        self.numaralar = self.numaralar[:limit]
        self.index = 0 
    def __iter__(self):
        return self
    def __next__(self):
        try:
            result = self.numaralar[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result
 
siradaki = iterator(3)
print(next(siradaki))
print(next(siradaki))
print(next(siradaki))

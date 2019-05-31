class ReusablePool:
    def __init__(self, size):
        self._reusables = [Reusable() for _ in range(size)]
 
    def acquire(self):
        return self._reusables.pop()
 
    def release(self, reusable):
        self._reusables.append(reusable)
 
 
class Reusable:
    name = ""
    pass
 
 

reusable_pool = ReusablePool(10)
reusable = reusable_pool.acquire()
reusable.name = "hasta1"
reusable2 = reusable_pool.acquire()
reusable2.name = "hasta2"
print(reusable.name)
reusable_pool.release(reusable)
 
 

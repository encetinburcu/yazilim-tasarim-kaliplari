class SingletonDatabase():
    _data = {}
    def __init__(self, **x):
        self._data.update(x)
    def __str__(self):
        return str(self._data)
 
add1 = SingletonDatabase(database = "10.10.10.10")
print(add1)

add2 = SingletonDatabase(user = "burcu")
add3 = SingletonDatabase(password="burcu123")
add4 = SingletonDatabase(serviceName="yazılımtasarımkalıpları")
print(add4)         
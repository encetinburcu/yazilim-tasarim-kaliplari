class Memento(object):
    def __init__(self, state):
        self._state = state

class uretici(object):
    _state = ""

    def set(self, state):
        print("durum ayarlandı:", state)
        self._state = state

    def savetomemento(self):
        print("kaydedildi.")
        return Memento(self._state)

data = []
x = uretici()
x.set("Hasta1")
x.set("Hasta2")
data.append(x.savetomemento())
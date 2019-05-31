class Data:
        def __init__(self, name):
                self._observers = []
                self._name = name
                self._hastasayisi = 0
 
        def attach(self, observer):
                if observer not in self._observers:
                        self._observers.append(observer)
        def detach(self, observer):
                try:
                        self._observers.remove(observer)
                except ValueError:
                        print("Gözlemci, gözlemciler listesinde değil.")
        def notify(self):
                for observer in self._observers:
                        observer.update(self)
                 
        @property
        def hastasayisi(self):
                return self._hastasayisi
 
        @hastasayisi.setter
        def hastasayisi(self, hastasayisi):
                self._hastasayisi = hastasayisi
                self.notify()
                 
class HastaTakip:
        def update(self, x):
                if x._hastasayisi > 100:
                    print("hasta sayisi {}. daha fazla kayıt olunamaz!".format(x._hastasayisi))
                else:
                    print("hasta sayisi {}. daha fazla kayıt olunabilir ".format(x._hastasayisi))
 
obj = Data("Data 1")
 
y = HastaTakip()
 
obj.attach(y)
 
obj.hastasayisi = 80
obj.hastasayisi = 111

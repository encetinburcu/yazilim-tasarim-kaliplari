import copy
 
class prototypeHasta:
        def __init__(self):
                self.ad = "burcu"
                self.yas = "22"
                self.hastalik = "grip"
        def __str__(self):
                return  '{} | {} | {}'. format(self.ad, self.yas, self.hastalik)
class Prototype:
        def __init__(self):
                self.klonla = {}
        def kaydet(self, name, obj):
                self.klonla[name] = obj
        def clone(self, name, **x):
                klon = copy.deepcopy(self.klonla.get(name))
                klon.__dict__.update(x)
                return klon

class Visitor:
    def __str__(self):
        return self.__class__.__name__
class Eylem:
    def accept(self, visitor):
        visitor.visit(self)
    def tedavi(self, visitor):
        print(self, visitor,"tarafından tedavi edilir")
    def randevu(self, visitor):
        print(self, visitor,"izniyle randevu alır")
    def __str__(self):
        return self.__class__.__name__
class visitorHasta(Eylem): pass
class visitorDoktor(Visitor):
    def visit(self, eylem):
        eylem.tedavi(self)
class visitorAdmin(Visitor):
    def visit(self, eylem):
        eylem.randevu(self)

class SingletonDatabase():
    _data = {}
    def __init__(self, **x):
        self._data.update(x)
    def __str__(self):
        return str(self._data)

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

class HastaneFactory:
    def olustur(self, stringg):
        list = listyap(stringg)
        return list
class factoryHasta:
    def eylem(self):
        return "randevu alırım."
class factoryDoktor:
    def eylem(self):
        return "hastayı iyileştiririm"
class factoryAdmin:
    def eylem(self):
        return "randevu onaylarım."
def listyap(list):
    lists = {"doktor": factoryDoktor(), "admin": factoryAdmin(), "hasta": factoryHasta()}
    return lists[list]
 
def decorate(orj):
    def add():
        orjText = orj()
        return "<p>" + orjText + "</p>"
    return add
@decorate
def Decorated():return "Burcu"

class AbstractBuilder():
    def __init__(self):
        self.hasta = None
    def yeniHasta(self):
        self.hasta = Hasta()
class Hasta():
    def __init__(self):
        self.ad = None
        self.yas = None
        self.hastalik = None
    def __str__(self):
        return '{} | {} | {}'.format(self.ad, self.yas, self.hastalik)      
class ConcreteBuilder(AbstractBuilder):
    def ad_ekle(self):
        self.hasta.ad = "burcu"
    def yas_ekle(self):
        self.hasta.yas = "22"
    def hastalik_ekle(self):
        self.hasta.hastalik = "kızamık"
class Director():
    def __init__(self, builder):
        self._builder = builder
    def constructHasta(self):
        self._builder.yeniHasta()
        self._builder.ad_ekle()
        self._builder.yas_ekle()
        self._builder.hastalik_ekle()
    def getHasta(self):
        return self._builder.hasta

class afDoktor:
    def gorev(self):
        return "tedavi etmek"
    def egitim(self):
        return "tıp mezunu"
    def __str__(self):
        return "Doktor"
class afHasta:
    def gorev(self):
        return "sağlıklı yaşamak"
    def egitim(self):
        return "farketmez"
    def __str__(self):
        return "Hasta"
class afAdmin:
    def gorev(self):
        return "hasta-doktor iletişimi"
    def egitim(self):
        return "min lise mezunu"
    def __str__(self):
        return "Admin"
class DoktorFactory:
    def get_f(self):
        return afDoktor()
class HastaFactory:
    def get_f(self):
        return afHasta()
class AdminFactory:
    def get_f(self):
        return afAdmin()
class HFactory:
    def __init__(self, hFactory):
        self._hFactory = hFactory
        
    def detaylandir(self):
        x = self._hFactory.get_f()
        print("tür:", x)
        print("görevi:", x.gorev())
        print("eğitim düzeyi:", x.egitim())

ConcreteFactory = HastaFactory()
AbstractFactory = HFactory(ConcreteFactory)
AbstractFactory.detaylandir()
print("-----------------------------")

concreteBuilder = ConcreteBuilder()
director = Director(concreteBuilder)
director.constructHasta()
hasta = director.getHasta()
print("hasta:", hasta)
print("-----------------------------")

print( Decorated() ) 
print("-----------------------------")

hastane = HastaneFactory()
obj1 = hastane.olustur('doktor')
print("Doktor:", obj1.eylem())
obj2 = hastane.olustur('admin')
print("Admin:", obj2.eylem())
obj3 = hastane.olustur('hasta')
print("Hasta:", obj3.eylem())
print("-----------------------------")
 
siradaki = iterator(3)
print(next(siradaki))
print(next(siradaki))
print(next(siradaki))
print("-----------------------------")

data = []
x = uretici()
x.set("Hasta1")
x.set("Hasta2")
data.append(x.savetomemento())
print("-----------------------------")

reusable_pool = ReusablePool(10)
reusable = reusable_pool.acquire()
reusable.name = "hasta1"
reusable2 = reusable_pool.acquire()
reusable2.name = "hasta2"
print(reusable.name)
reusable_pool.release(reusable)
print("-----------------------------")

obj = Data("Data 1")
y = HastaTakip()
obj.attach(y)
obj.hastasayisi = 80
obj.hastasayisi = 111
print("-----------------------------")

p_hasta = prototypeHasta()
prototype = Prototype()
prototype.kaydet('hasta', p_hasta)
p_hasta1 = prototype.clone('hasta')
print("hasta1:", p_hasta1)
p_hasta2 = prototype.clone('hasta', hastalik = "kızamık")
print("hasta2:", p_hasta2) 
print("-----------------------------")

add1 = SingletonDatabase(database = "10.10.10.10")
print(add1)
add2 = SingletonDatabase(user = "burcu")
add3 = SingletonDatabase(password="burcu123")
add4 = SingletonDatabase(serviceName="yazılımtasarımkalıpları")
print(add4)         
print("-----------------------------")

hasta1 = visitorHasta()
doktor = visitorDoktor()
admin = visitorAdmin()
hasta1.accept(doktor)
hasta1.accept(admin)
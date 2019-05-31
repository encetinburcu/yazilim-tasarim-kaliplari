class Hasta():
    def __init__(self):
        self.ad = None
        self.yas = None
        self.hastalik = None
    def __str__(self):
        return '{} | {} | {}'.format(self.ad, self.yas, self.hastalik)      
 
class AbstractBuilder():
    def __init__(self):
        self.hasta = None
    def yeniHasta(self):
        self.hasta = Hasta()
 
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
 
concreteBuilder = ConcreteBuilder()
director = Director(concreteBuilder)
 
director.constructHasta()
hasta = director.getHasta()
print("hasta:", hasta)

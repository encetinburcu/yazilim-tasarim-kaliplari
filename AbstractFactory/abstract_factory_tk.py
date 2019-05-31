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

objectOfConcreteFactory = HastaFactory()
objectOfAbstractFactory = HFactory(objectOfConcreteFactory)
objectOfAbstractFactory.detaylandir()
import copy
 
class Hasta:
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
 
hasta = Hasta()
prototype = Prototype()
prototype.kaydet('hasta', hasta)
hasta1 = prototype.clone('hasta')
print("hasta1:", hasta1)
 
hasta2 = prototype.clone('hasta', hastalik = "kızamık")
print("hasta2:", hasta2) 
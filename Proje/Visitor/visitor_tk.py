class Eylem:
    def accept(self, visitor):
        visitor.visit(self)
    def tedavi(self, visitor):
        print(self, visitor,"tarafından tedavi edilir")
    def randevu(self, visitor):
        print(self, visitor,"izniyle randevu alır")
    def __str__(self):
        return self.__class__.__name__
 
class Hasta(Eylem): pass
 
class Visitor:
    def __str__(self):
        return self.__class__.__name__
 
class Doktor(Visitor):
    def visit(self, eylem):
        eylem.tedavi(self)
 
class Admin(Visitor):
    def visit(self, eylem):
        eylem.randevu(self)


hasta = Hasta()

doktor = Doktor()
admin = Admin()

hasta.accept(doktor)
hasta.accept(admin)

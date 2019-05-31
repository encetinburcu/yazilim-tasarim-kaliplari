class Hasta:
    def eylem(self):
        return "randevu alırım."
 
class Doktor:
    def eylem(self):
        return "hastayı iyileştiririm"
 
class Admin:
    def eylem(self):
        return "randevu onaylarım."
 
def listyap(list):
    lists = {"doktor": Doktor(), "admin": Admin(), "hasta": Hasta()}
    return lists[list]
 
class HastaneFactory:
    def olustur(self, stringg):
        list = listyap(stringg)
        return list   
 
hastane = HastaneFactory()
 
obj1 = hastane.olustur('doktor')
print("Doktor:", obj1.eylem())
 
obj2 = hastane.olustur('admin')
print("Admin:", obj2.eylem())
 
obj3 = hastane.olustur('hasta')
print("Hasta:", obj3.eylem())
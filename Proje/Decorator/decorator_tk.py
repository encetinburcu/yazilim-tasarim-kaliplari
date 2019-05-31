def decorate(orj):
    def add():
        orjText = orj()
        return "<p>" + orjText + "</p>"
    return add
 
@decorate
def Decorated():
    return "Burcu"
 
print( Decorated() ) 
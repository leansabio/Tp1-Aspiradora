#medio ambiente
class Baldosa:
    #1 es sucia
    estado=1



class Aspiradora(Baldosa):
    #estado=1
    posicion="izquierda"
    def __init__(self, baldosa):
        self.baldosaactual=baldosa
    

    def limpiar(self):
        self.baldosaactual.estado=0
    
    def izquierda(self, baldosa):
        self.posicion="izquierda"
        self.baldosaactual=baldosa

    def derecha(self,baldosa):
        self.posicion="derecha"
        self.baldosaactual=baldosa



baldosaA=Baldosa()
baldosaB=Baldosa()

aspiradora= Aspiradora(baldosaA)

i=10

while i!=0:
    i=i-1
    if (aspiradora.baldosaactual.estado==1):
        aspiradora.limpiar()
        print("limpiando",aspiradora.posicion)
    else:
        if (aspiradora.posicion=="izquierda"):
            aspiradora.derecha(baldosaB)
            print("moviendo derecha")
        else:
            aspiradora.izquierda(baldosaA)
            print("moviendo izquierda")


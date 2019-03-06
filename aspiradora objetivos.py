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

EBaldosaA=1
EBaldosaB=1

#objetivo
cantSucias=1
while True:
    
    print()
    if(EBaldosaA+EBaldosaB==cantSucias):
        print("Objetivo cumplido")
        break

    if (aspiradora.baldosaactual.estado==1):
        print("limpiando",aspiradora.posicion)
        aspiradora.limpiar()
        if (aspiradora.posicion=="izquierda"):
            EBaldosaA=0
        else:
            EBaldosaB=0
    else:
        print("Baldosa limpia")
        if (aspiradora.posicion=="izquierda"):
            EBaldosaA=0
        else:
            EBaldosaB=0
    
    if(EBaldosaA+EBaldosaB==cantSucias):
        print("Objetivo cumplido")
        break

    if (aspiradora.posicion=="izquierda"):
        aspiradora.derecha(baldosaB)
        print("Moviendo derecha")
    else:
        aspiradora.izquierda(baldosaA)
        print("Moviendo izquierda")
   
    
print()
print("alto")


    



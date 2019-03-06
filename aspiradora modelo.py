#medio ambiente
class Baldoza:
    #1 es sucia
    estado=1



class Aspiradora(Baldoza):
    #estado=1
    posicion="izquierda"
    def __init__(self, baldoza):
        self.baldozaactual=baldoza
    

    def limpiar(self):
        self.baldozaactual.estado=0
    
    def izquierda(self, baldoza):
        self.posicion="izquierda"
        self.baldozaactual=baldoza

    def derecha(self,baldoza):
        self.posicion="derecha"
        self.baldozaactual=baldoza



baldozaA=Baldoza()
baldozaB=Baldoza()

aspiradora= Aspiradora(baldozaA)

eBaldozaA=1
eBaldozaB=1

while True:
    
    print()
    if (aspiradora.baldozaactual.estado==1):
        print("limpiando",aspiradora.posicion)
        aspiradora.limpiar()
        if (aspiradora.posicion=="izquierda"):
            eBaldozaA=0
        else:
            eBaldozaB=0
    else:
        print("baldoza limpia")
        if (aspiradora.posicion=="izquierda"):
            eBaldozaA=0
        else:
            eBaldozaB=0

    if (eBaldozaA==0 and eBaldozaB==0):
        print()
        print("Todas la baldozas limpias")
        break

    if (aspiradora.posicion=="izquierda"):
        aspiradora.derecha(baldozaB)
        print("Moviendo derecha")
    else:
        aspiradora.izquierda(baldozaA)
        print("Moviendo izquierda")
   
    
print()
print("alto")


    



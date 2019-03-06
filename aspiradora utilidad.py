#medio ambiente
class Baldoza:
    #1 es sucia
    estado=1



class Aspiradora(Baldoza):
    #estado=1
    posicion=0
    def __init__(self, baldoza):
        self.baldozaactual=baldoza
    

    def limpiar(self):
        self.baldozaactual.estado=0
    
    def izquierda(self, baldoza):
        self.posicion=0
        self.baldozaactual=baldoza

    def derecha(self,baldoza):
        self.posicion=self.posicion+1
        self.baldozaactual=baldoza






baldozas=[Baldoza(),Baldoza(),Baldoza(),Baldoza()]

aspiradora= Aspiradora(baldozas[0])

cant=0

eBaldozas=[1,1,1,1]

#objetivo
cantSucias=0
for a in range(10):
    
    print()
    cant=0
    for i in range(4):
        cant=baldozas[i].estado+cant
    if(cant==cantSucias):
        print("Objetivo cumplido")
        break

    if (aspiradora.baldozaactual.estado==1):
        print("limpiando",aspiradora.posicion)
        aspiradora.limpiar()
        eBaldozas[aspiradora.posicion]=0
    else:
        print("baldoza",aspiradora.posicion,"limpia")
        eBaldozas[aspiradora.posicion]=0
    
    cant=0
    for i in range(4):
        cant=baldozas[i].estado+cant
    if(cant==cantSucias):
        print("Objetivo cumplido")
        break

    if (aspiradora.posicion<3):
        aspiradora.derecha(baldozas[aspiradora.posicion+1])
        print("Moviendo derecha")
    else:
        aspiradora.izquierda(baldozas[0])
        print("Moviendo inicio")
   
    
print()
print("alto")


    



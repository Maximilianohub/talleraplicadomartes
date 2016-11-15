#taller aplicado listas
#Ivonne Ibacache
#Rocio Jimenez
#Maximiliano Toro
import random
#modificacion
def genera():
      lista = [0]  * 6
      y=0
      for i in range(6):
          x=random.randint(1,41)
          while x==y:
              x=random.randint(1,41)
          lista[i] = x
          y=x
      lista.sort()
      print lista

genera()


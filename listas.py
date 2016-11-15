#taller aplicado listas
#Ivonne Ibacache
#Rocio Jimenez
#Maximiliano Toro

#import random
#modificacion
#def genera():
#     lista = [0]  * 6
 #    y=0
#      for i in range(6):
#          x=random.randint(1,41)
#          while x==y:
#              x=random.randint(1,41)
#          lista[i] = x
#          y=x
#      lista.sort()
#      print lista

#genera()

import random

def genera():
  l=range(1,42)
  mi_lista=[]
  while len(mi_lista)<6:
    numero=random.choice(l)
    if not (numero) in mi_lista:
      mi_lista.append(numero)
      print mi_lista
genera()

def comprueba(x,l):
    if x in l:
        return False
  

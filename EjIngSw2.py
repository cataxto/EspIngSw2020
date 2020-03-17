
from __future__ import annotations
from abc import ABC, abstractmethod

texto='catalina'
#str(input('Digite el ingreso a contar palabra '))
palabr='a'
#input('Cuál es la palabra a contar')


class contador(object):
    def contador1(texto,letra):
        cont=0
        for i in texto:
            if i==palabr:
                cont=cont+1
                print('La letra ',palabr,'aparece ',cont,' veces')

   def __str__(self):
      return self.name
            
class vocal_a(contador):
    texto=texto
    letra='a'

class vocal_e(contador):
    texto=texto
    letra='e'

class vocal_i(contador):
    texto=texto
    letra='i'

class vocal_o(contador):
    texto=texto
    letra='o'

class vocal_u(contador):
    texto=texto
    letra='u'

def __str__(self):
    return self.name


class conta(object):
    def __init__(self):
        self.vocal=input('Digite el texto para contar palabra ')
        self.texto=input('Digite la vocala  contabilizar')
    def contar(texto,vocal):
        self.texto.vocal.contador()
    


class Gato:
    tipo_animal = 'Felino'
    print('Iniciou')

    def __init__(self, nome):
        self.nome = nome

Gato.tipo_animal = 'Pet'

g1 = Gato('Kiki')
g2 = Gato('Cookie')

print(g1.tipo_animal)
print(g2.tipo_animal)

print(g1.nome)
print(g2.nome)

g2.tipo_animal = 'bichano'

print(g1.tipo_animal, '1')
print(g2.tipo_animal, '2')

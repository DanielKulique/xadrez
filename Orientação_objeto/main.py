class Cubo:
    def __init__(self, valor):
        self.x = valor 
        print('Objeto criado!')
    def calcula_cubo(self):
        cubo = self.x * self.x * self.x
        return 'Cubo calculado: ' + str(cubo)
    
print(type(Cubo))

test = Cubo(2)
c = test.calcula_cubo()

print(c)

#metodo construtor

class Gato:
    def __init__(self, nome):
        self.tipo_animal = nome
        print('Seu gato se chama ', self.tipo_animal)

    def peso_gato(self, peso):
        self.peso = peso
        if(self.peso > 5.0):
            print('Obeso')
        elif(self.peso >3.5):
            print('Peso normal')
        else:
            print('Abaixo do peso')

    def _dieta_especial_gato(self):
        self.msg = 'TUDO OK!'
        if (self.peso <3.5):
            self.msg = 'aumente a recao do felino'
        if (self.peso >= 5.0):
            self.msg = 'diminua a racao do felino'
        return self.msg
    
    def dados_gato(self):
        print('\nO gato', self.tipo_animal, 'esta com', self.peso, 'kg')
        print(self._dieta_especial_gato())

nome_gato = input('Digite o nome do seu gato: ')
g1 = Gato(nome_gato)

peso = float(input('\nQual o peso de seu gato, em kg?'))
g1.peso_gato(peso)
g1.dados_gato()
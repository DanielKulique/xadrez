class Test():
    def __init__(self, valor):
        self.x = valor
    
    def get_valor(self):
        '''metodo getter para retornar o valor do atributo x'''
        return self.x

    def set_valor(self, v):
        '''metodo setter para atribuir um novo valor ao atributo x'''
        self.x = v

teste = Test(10)
print('Valor do objeto: ', teste.get_valor())

val = int(input('Digite um valor numerico: '))
teste.set_valor(val)
print('Valor do objeto apos atribuicao: ', teste.get_valor())
class CalcCubo:
    '''permite calcular area de um cubo'''
    def __init__(self, valor): #metodo construtor
        self.x = valor
        print('objeto criado!')
        
    def calcula_cubo(self):
        self.cubo = self.x * self.x *self.x
        return 'Cubo calculado: ' + str(self.cubo)
    
num = int(input('entre com um numero: '))
objCubo = CalcCubo(num) #instanciar a classe
cubo = objCubo.calcula_cubo() # o operador "." invoca o metodo "calcula_cubo" da classe
print(cubo)
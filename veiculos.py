class Veiculos:
    def __init__(self, cor, placa, nro_rodas):
        self.cor = cor
        self.placa = placa
        self.nro_rodas = nro_rodas
    
    def ligar_motor(self):
        print('Ligando motor...')
        print('Motor ligado!')

class Motocicleta(Veiculos):
    pass

class Carro(Veiculos):
    pass

class Caminhao(Veiculos):
    pass

moto = Motocicleta('Vermelha', 'abc-1234', 2)

moto.ligar_motor()
class Veiculos:
    def __init__(self, cor, placa, nro_rodas):
        self.cor = cor
        self.placa = placa
        self.nro_rodas = nro_rodas
    
    def ligar_motor(self):
        print('Ligando motor...')
        print('Motor ligado!')
        
    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f' {chave}={valor}'for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculos):
    pass

class Carro(Veiculos):
    pass

class Caminhao(Veiculos):
    def __init__(self, cor, placa, nro_rodas, carregado):
        super().__init__(cor, placa, nro_rodas)
        self.carregado = carregado
    
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta('Vermelha', 'abc-1234', 2)

carro = Carro('Preto', 'def-5678', 4)

caminhao = Caminhao('Azul', 'ghj-9123', 8, False)

print(moto)
print(carro)
print(caminhao)

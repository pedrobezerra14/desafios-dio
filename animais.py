class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
        
    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f' {chave}={valor}'for chave, valor in self.__dict__.items()])}"
    

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leão(Mamifero):
    pass

class  Ornitorrinco(Mamifero, Ave):
    pass

gato = Gato(4, 'Preto')
print(gato)

ornitorrinco = Ornitorrinco(2, 'Vermelho', 'Laranja')
print(ornitorrinco)
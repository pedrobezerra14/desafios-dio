num = float(input('Digite um número: '))

def par_impar(num):
    if (num % 2) != 0:
        return f"{num} é ímpar!"
    else:
        return f"{num} é par!"
    
result = par_impar(num)
print(result)

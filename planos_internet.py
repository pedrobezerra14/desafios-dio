consumo = float(input('Insira o consumo médio mensal de dados (apenas números/ em GB): '))

# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(consumo):
  plano_essencial_fibra = "Plano Essencial Fibra - 50Mbps"
  plano_prata_fibra = "Plano Prata Fibra - 100Mbps"
  plano_premium_fibra = "Plano Premium Fibra - 300Mbps"

  if consumo <= 10:
    return plano_essencial_fibra
  elif consumo > 10 and consumo <=20:
    return plano_prata_fibra
  else:
    return plano_premium_fibra
    
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# TODO: Retorne o plano de internet adequado:

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))
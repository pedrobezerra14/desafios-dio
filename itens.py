# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:

itens = []
# TODO: Crie um loop para solicita os itens ao usuário:
while len(itens) < 3:
# TODO: Solicite o item e armazena na variável "item":
  adicionar_item = input('Informe três itens para adicionar a lista de equeipamentos: ')
# TODO: Adicione o item à lista "itens":
  itens.append(adicionar_item)

# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")
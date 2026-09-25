compras = ["pao", "leite", "morango"]

def mostrar():
    for compra in compras:
        print(compra)

    # print("Lista de compras do mercado Y! ")
    # print("0 Sair")
    # print("1 Mostrar Lista")
    # print("2 Cadastrar Item Na Lista")
    # print("3 Excluir Item Na Lista")
    # print("4 Modificar Item Na Lista")
    # escolha = int(input("Digite Como Deseja Proseguir! : "))



def criar():
    nova_compra = input("Digite oque voce deseja adicionar na lista de compras! :")
    compras.append (nova_compra)

#     print("0 Sair")
#     print("1 Mostrar Lista")
#     print("2 Cadastrar Item Na Lista")
#     print("3 Excluir Item Na Lista")
#     print("4 Modificar Item Na Lista")
#     escolha = int(input("Digite Como Deseja Proseguir! : "))
 
def excluir():
    remover_compra = input("escreva qual compra voce quer remover! : ")
    compras.remove(remover_compra)

def modificar():
    modificar_compra = input("escreva qual compra voce quer alterar? : ")
    posicao = compras.index(modificar_compra)
    novo_valor_compra = input("digite o item pelo qual voce quer substituir : ")
    compras[posicao] = novo_valor_compra
    

escolha = 1
while escolha != 0 :
    print("0 Sair")
    print("1 Mostrar Lista")
    print("2 Cadastrar Item Na Lista")
    print("3 Excluir Item Na Lista")
    print("4 Modificar Item Na Lista")
    escolha = int(input("Digite Como Deseja Proseguir! : "))

    if escolha == 1:
        mostrar()

    elif escolha == 2:
        criar()

    elif escolha == 3:
        excluir()

    elif escolha == 4:
        modificar()

    elif escolha == 0:
        break
    else:
        print("Digite um numero valido!")
        



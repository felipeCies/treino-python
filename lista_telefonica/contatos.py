#Aluno: Felipe Luiz Cieslick
#Curso Análise e desenvolvimento de sistemas
lista_telefonica = {}


def adicionar():
    nome= input("Qual o nome do contato? ").strip().title()
    telefone = input("Qual o número do contato? ").strip()
    lista_telefonica [nome] = telefone
    print("Contato adicionado")

def exibir():
    if lista_telefonica:
        print("Lista de Contatos")
        nomes_ordem = sorted(lista_telefonica.keys())
        for nome in nomes_ordem:
            telefone = lista_telefonica[nome]
            print(f"Nome: {nome}")
            print(f"Telefone: {telefone}")
            print("_" * 30)
    else:
        print("Nenhum contato adicionado")


def buscar():
    nome = input("Qual contato deseja buscar? ").strip().title()
    if nome in lista_telefonica:
        print(f"Nome: {nome}")
        print(f"Telefone: {lista_telefonica[nome]}")
        print ("_" *30)
    else:
        print("Contato não encontrado")

def editar():
    nome = input("Qual contato deseja editar? ").strip().title()
    if nome in lista_telefonica:
        novo_nome = input("Digite o novo nome: ").strip().title()
        novo_telefone = input("Digite o novo telefone: ").strip()
        
        if novo_nome:
            lista_telefonica[novo_nome] = lista_telefonica.pop(nome)
            nome = novo_nome  
        if novo_telefone:
            lista_telefonica[nome] = novo_telefone
        
        print("Contato atualizado")
    else:
        print("Contato não encontrado")

    

def excluir():
    nome = input("Qual contato deseja deletar? ").strip().title()
    if nome in lista_telefonica:
        del lista_telefonica[nome]
        print ("_" *30)
        print("Contato deletado")
        print ("_" *30)

    else:
        print ("_" *30)
        print("Contato não encontrado")
        print ("_" *30)

def menu():
    print("Tecle 1 para adicionar um contato")
    print("Tecle 2 para exibir contatos")
    print("Tecle 3 para buscar um contato")
    print("Tecle 4 para deletar um contato")
    print("Tecle 5 para editar um contato")
    print("Tecle 6 para sair da lista")



def loop():
    while True:
        menu()
        x = input("Escolha uma opção: ").strip()

        if x == "1":
            adicionar()
        elif x == "2":
            exibir()
        elif x == "3":
            buscar()
        elif x == "4":
            excluir()
        elif x == "5":
            editar()
        elif x == "6":
            print("Até mais")
            break
        y = input("Deseja fazer outra operação? (1 - Sim / 2 - Não): ").strip()
        if y == "2":
            print("Finalizando programa.")
            break   



loop()   

class No:

  def __init__(self, valor):
    self.valor = valor
    self.proximo = None

  def mostra_no(self):
    print(self.valor)


class ListaEncadeada:

  def __init__(self):
    self.primeiro = None

  def insere_inicio(self, valor):
    novo = No(valor)
    novo.proximo = self.primeiro
    self.primeiro = novo

  def mostrar(self):
    if self.primeiro == None:
      print('Não existem voos cadastrados')
      return None

    atual = self.primeiro
    while atual != None:
      atual.mostra_no()
      atual = atual.proximo

  def pesquisa(self, valor):
    if self.primeiro == None:
      print('Não existem voos cadastrados')
      return None

    atual = self.primeiro
    while atual.valor != valor:
      if atual.proximo == None:
        print('Voo não encontrado!')
        break
      else:
        atual = atual.proximo
    return atual


lista = ListaEncadeada()

des = int(input('Digite o número de destino da viagem : '))
lista.insere_inicio(des)

pto = 1
while pto != 0:
  pto = int(
    input('Digite um ponto de parada ou zero(0) para informar a origem : '))
  if pto != 0:
    lista.insere_inicio(pto)

    ori = int(input('Digite a origem do embarque : '))
    lista.insere_inicio(ori)

    print('')
    print('Itinerário da Origem ao Destino da viagem : ')
    lista.mostrar()

    pesquisa = str(input('Deseja pesquisar por número de voo ?(s/n) : '))
    while pesquisa.upper() == 'S':
      aux = int(input('Digite o número do voo : '))
      consultar = lista.pesquisa(aux)
      print('Voo nº ', consultar.valor, ' encontrado!')
      pesquisa = str(input('Deseja pesquisar por número de voo ?(s/n) : '))
  else:
    print('FIM DA EXECUÇÃO DO PROGRAMA !')

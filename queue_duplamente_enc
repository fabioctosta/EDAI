
class No:
    def __init__(self,valor):
        self.valor = valor
        self.prox = None
        self.ant = None

    def show(self):
        print(f"{self.valor}")

class lista_duplamente_encadeada():

    def __init__(self):
        self.head = None
        self.size = 0
    def append(self,valor):
        elemento = No(valor)
        self.size += 1
        if self.head is None:
            self.head = elemento
        else:
            ponteiro = self.head
            while ponteiro.prox is not None:
                ponteiro = ponteiro.prox
            ponteiro.prox = elemento
            elemento.ant = ponteiro

    def insert(self, valor, pos):
        print(f"Voce quer inserir o valor {valor} na posicao {pos} da lista.")
        elemento = No(valor)
        if self.head is not None:
            if (pos == 0):
                elemento.prox = self.head
                self.head = elemento
            elif (pos > 0):
                ponteiro = self.head
                for i in range(pos-1):
                    ponteiro = ponteiro.prox
                elemento.prox = ponteiro.prox
                elemento.ant = ponteiro
                ponteiro.prox.ant = elemento
                ponteiro.prox = elemento
        else:
            self.head = elemento
        # self.display()

    def tamanho(self):
        print(f" A lista tem tamanho : {self.size}")

    def begin(self,valor):
        self.size +=1
        elemento = No(valor)
        if self.head is None:
            self.head = elemento
        else:
            ponteiro = self.head
            self.head = elemento
            self.head.prox = ponteiro
        # self.display()
    def display(self):
        if self.head is None:
            print("A lista está vazia")
        else:
            print("A lista possui elementos: ")
            ponteiro = self.head
            while ponteiro is not None:
                ponteiro.show()
                ponteiro = ponteiro.prox
            print("___________________")

    def freelist(self):
        self.head = None
        tam = 0

lista = lista_duplamente_encadeada()
lista.display()
lista.append(20)
lista.append(15)
lista.append(30)
lista.begin(10)
lista.display()
# lista.tamanho()
lista.insert(100,1)
lista.display()

lista.insert(60,4)
lista.display()

# Tarefa página 2
# a = []
# b = []
# c = []
#
# n = int(input())
#
# vetor = input()
# vetor2 = input()
#
# vetor_str = vetor.split()
# vetor2_str = vetor2.split()
# for valor in vetor_str:
#     valor = int(valor)
#     a.append(valor)
# for valor in vetor2_str:
#     valor = int(valor)
#     b.append(valor)
#
# print(a)
# print(b)
#
# lista1 = lista_duplamente_encadeada()
# lista2 = lista_duplamente_encadeada()
#
# for elemento in a:
#     lista1.append(elemento)
# lista1.display()
#
# for elemento in b:
#     lista2.append(elemento)
# lista2.display()
#

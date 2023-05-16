
# Implementando o nó

class No:
    def __init__(self,valor):
        self.valor = valor
        self.prox = None

    def show(self):
        print(f'{self.valor}')

class lista_encadeada:

    def __init__(self):
        self.head = None

    def append(self,valor):
        # Insere diretamente um valor na variavel valor e transforma-o em nó
        elemento = No(valor)
        if self.head is not None:
            ponteiro = self.head
            while ponteiro.prox is not None:
                ponteiro = ponteiro.prox
            ponteiro.prox = elemento
        else:
            self.head = elemento
    def display(self):
        if self.head is not None:
            print("A lista é: ")
            ponteiro = self.head
            while ponteiro is not None:
                ponteiro.show()
                ponteiro = ponteiro.prox
        else:
            print("Essa lista está vazia.")

    def freelist(self):
        self.head = None

    def insert(self,valor,pos):
        elemento = No(valor)
        if pos == 0:
            elemento.prox = self.head
            self.head = elemento
        else:
            ponteiro = self.head
            if ponteiro is None:
                raise IndexError("index out of range")
            for i in range(pos-1):
                ponteiro = ponteiro.prox
            elemento.prox = ponteiro.prox
            ponteiro.prox = elemento

    def conc(self,l1,l2):
        ponteiro1 = l1.head
        ponteiro2 = l2.head
        while ponteiro1 is not None:
            self.append(ponteiro1.valor)
            if ponteiro2 is not None:
                self.append(ponteiro2.valor)
                ponteiro2 = ponteiro2.prox
            ponteiro1 = ponteiro1.prox


# Implementacao do Display e insercao do primeiro elemento

# # a = No(35)
# lista = lista_encadeada()
# lista.display()
# lista.append(35)
# lista.display()
#
# # adicionando outros elementos à lista
# lista.append(70)
# lista.append(15)
# lista.append(33)
# lista.display()
# lista.insert(20,0)
# lista.display()
# lista.insert(100,1)
# lista.display()
# lista.insert(200,4)
# lista.display()

a = [1.2,3.5,9.78]
b = [5, 2.9]

l1 = lista_encadeada()
l2 = lista_encadeada()

# a_str = a.split()
# b_str = b.split()

# for valor_str in a_str:
#     valor_str = int(valor_str)
#     l1.append(valor_str)
#
# for valor_str in b_str:
#     valor_str = int(valor_str)
#     l2.append(valor_str)

for i in a:
    l1.append(i)

for i in b:
    l2.append(i)

l1.display()
l2.display()

l3 = lista_encadeada()
l3.conc(l1,l2)
l3.display()

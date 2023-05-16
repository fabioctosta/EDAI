class No:
    def __init__(self,valor):
        self.valor = valor
        self.prox = None

    def show(self):
        print(f"{self.valor}")

class Stack:

    def __init__(self):
        self.top = None

    def push(self,valor):
        elemento = No(valor)
        if self.top is None:
            self.top = elemento
        else:
            elemento.prox = self.top
            self.top = elemento
            self.display()

    def display(self):
        if self.top is None:
            print("A Pilha está vazia")
        else:
            ponteiro = self.top
            print("A pilha tem elementos:")
            while ponteiro is not None:
                ponteiro.show()
                ponteiro = ponteiro.prox
            print("_________________")

    def pop(self):
        if self.top is None:
            print("Não há elementos na lista para serem excluidos.")
        else:
            self.top = self.top.prox
            self.display()

    def freestack(self):
        while self.top is not None:
            self.pop()

pilha = Stack()
pilha.display()
pilha.push(20)
pilha.push(30)
pilha.push(50)
pilha.pop()
pilha.push(100)
pilha.push(90)
pilha.pop()

pilha.freestack()
pilha.display()

# for i in range(6):
#     pilha.push(i**2)
#
# pilha.display()

class No:
    def __init__(self,valor):
        self.valor = valor
        self.prox = None

    def show(self):
        print(f'{self.valor}')

class Queue:
    def __init__(self):
        self.front = None
        self.last = None

    def append(self,valor):
        elemento = No(valor)
        if self.front is None:
            self.front = elemento
            self.last = elemento
        else:
            self.last.prox = elemento
            self.last = elemento

    def display(self):
        if self.front is None:
            print("A lista está vazia.")
        else:
            ponteiro = self.front
            while ponteiro is not None:
                print(ponteiro.valor, end=" ")
                ponteiro = ponteiro.prox
            print('\n')

    def pop(self):
        if self.front is None:
            print("É impossível remover algum elemento")
        else:
            valor = self.front.valor
            if (self.front == self.last):
                self.front = None
                self.last = None
            else:
                self.front = self.front.prox
            return valor

fila1 = Queue()
fila1.append(20)
fila1.append(14)
fila1.append(33)
fila1.display()
fila1.pop()
fila1.display()

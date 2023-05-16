
# Implementando o nó

class No:
    def __init__(self,valor):
        self.valor = valor
        self.prox = None

    def show(self):
        print(f"{self.valor}")

class lista_enc_circular:
    def __init__(self):
        self.head = None

    def append(self,valor):
        elemento = No(valor)
        if self.head is None:
            self.head = elemento
            self.head.prox = self.head
        else:
            ponteiro = self.head
            while ponteiro != self.head:
                ponteiro = ponteiro.prox
            ponteiro.prox = elemento
            elemento.prox = self.head

    def insert(self,valor,pos):
        elemento = No(valor)
        if self.head is Not None:
            if (pos == 0):
                elemento.prox = self.head
                self.head = elemento
            elif (pos > 0):
                ponteiro = self.head
                for i in range(pos):
                    ponteiro = ponteiro.prox
                elemento.prox = ponteiro

        else:
            self.head = elemento


    def display(self):
        if self.head is None:
            print("A lista está vazia")
        else:
            elementos = []
            ponteiro = self.head
            while True:
                elementos.append(ponteiro.valor)
                ponteiro = ponteiro.prox
                if ponteiro == self.head:
                    break
            print("->".join(map(str, elementos)))

lista = lista_enc_circular()
lista.append(3)
lista.append(12)
lista.append(20)
lista.append(24)
lista.display()

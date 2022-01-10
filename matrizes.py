
class Creat_matriz:
    def __init__(self):
        self.dados1 = []
        self.dados2 = []
        self.recebe_dados()
        self.tipo_operacao()

    def recebe_dados(self):
        self.cont_loop = 1
        while True:
            if self.cont_loop ==3:
                break
            self.size_matrizes = str(input(f'Qual o tamanho da matriz {self.cont_loop}? Utilize X, ColXLin: '))
            self.coluna, self.linha = self.fatia_string(self.size_matrizes)
            self.cont_linha = 1
            self.cont_coluna = self.coluna
            self.cont = 1
            for i in range(self.coluna*self.linha):
                if self.cont_loop ==1:
                    self.dados1 = int(input(f'Digite os dado da linha {self.cont_linha}: '))
                else:
                    self.dados2 = int(input(f'Digite os dado da linha {self.cont_linha}: '))
                if self.cont >= self.cont_coluna:
                    self.cont_linha += 1
                    self.cont_coluna += self.coluna
                self.cont += 1
            self.cont_loop += 1


    def fatia_string(self, size):
        self.fatiado = size.split('X')
        self.size_matrize = list(map(int, self.fatiado))
        return self.size_matrize[0], self.size_matrize[1]

    def tipo_operacao(self):
        self.tipo = str(input('Qual será o tipo de operação? (+, -, *, /'))
        if self.tipo == '+':
            self.operacao_soma()

    def operacao_soma(self):
        pass








Creat_matriz()
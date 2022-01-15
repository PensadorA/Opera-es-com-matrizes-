from erros import  *
class Creat_matriz(Erros):
    def __init__(self):
        self.dados1 = []
        self.dados2 = []
        self.tamanho = []
        self.resultado =[]
        self.recebe_dados()
        self.tipo_operacao()

    def recebe_dados(self):
        self.cont_loop = 1
        while True:
            if self.cont_loop == 3:
                break
            self.size_matrizes = str(input(f'Qual o tamanho da matriz {self.cont_loop}? Utilize X, ColXLin: '))
            self.tamanho.append(self.size_matrizes)
            self.coluna, self.linha = self.fatia_string(self.size_matrizes)
            self.cont_linha = 1
            self.cont_coluna = self.coluna
            self.cont = 1
            for i in range(self.coluna*self.linha):
                if self.cont_loop == 1:
                    self.dados1.append(int(input(f'Digite os dado da linha {self.cont_linha}: ')))
                else:
                    self.dados2.append(int(input(f'Digite os dado da linha {self.cont_linha}: ')))
                if self.cont >= self.cont_coluna:
                    self.cont_linha += 1
                    self.cont_coluna += self.coluna
                self.cont += 1
            self.cont_loop += 1


    def fatia_string(self, size):
        try:
            self.fatiado = size.split('X')
            self.size_matrize = list(map(int, self.fatiado))
            return self.size_matrize[0], self.size_matrize[1]
        except:
            self.error_1()

    def tipo_operacao(self):
        self.tipo = str(input('Qual será o tipo de operação? (+, -, *, /'))
        if self.tipo == '+':
            self.operacao_soma()

    def operacao_soma(self):
        if self.tamanho[0] == self.tamanho[1]:
            print(self.dados1)
            for i in range(len(self.dados1)):
                self.resultado.append(self.dados1[i] + self.dados2[i])
            print(f'Sua matriz resultante  da soma é: {self.resultado}')
        else:
            self.error_2()











Creat_matriz()
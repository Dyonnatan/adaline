class Treinamento_Adaline(object):
    
    def inicializar_sinapses_mostrar(self):
        self.vetor_sinapses = [0.0, 1.0, 0.0, 1.0]
        print("Valor das sinapses: ")
        x = 0
        for x in xrange(4):
            print("w%i : %.1f " %(x, self.vetor_sinapses[x]))
        print("==========================")
        
    def inicializar_vetores_treinamento_mostrar(self):
        self.x1 = [1.0, -1.0, 1.0]
        self.x2 = [-1.0, 1.0, -1.0]
        x = 0
        print("Valor do primeiro vetor de treinamento(x1): ")
        for x in xrange(3):
            print("%.1f" %self.x1[x])
        print("==========================")
        print("Valor de segundo vetor de treinamento(x2): ")
        for x in xrange(3):
            print("%.1f" %self.x2[x])
        print("==========================")
    
    def inicializar_saidas_desejadas_mostrar(self):
        self.ydesejado1 = 1
        self.ydesejado2 = -1
        print("Valor da saida desejada do primeiro vetor de treinamento: %i" %self.ydesejado1)
        print("==========================")
        print("Valor da saida desejada do segundo vetor de treinamento: %i" %self.ydesejado2)
        print("==========================")

    def calcular_v_do_vetor_treinamento(self, vetor_treinamento):
        self.v = 0.0
        x = 0
        for x in xrange(4):
            self.v += vetor_treinamento[x] * self.vetor_sinapses[x]
        return self.v

    def calcular_erro(self, ydesejado):
        self.erro = 0.0
        self.erro = ydesejado - self.v
        return self.erro

    def atualizar_sinapses_mostrar(self, vetor_treinamento):
        teta = 0.1
        x = 0
        variacao_sinapses = [0.0, 0.0, 0.0, 0.0]
        for x in xrange(4):
            variacao_sinapses[x] = teta * self.erro * vetor_treinamento[x]
        for x in xrange(4):
            self.vetor_sinapses[x] += variacao_sinapses[x]
        print("Vetor de variacao de sinapses:")
        for x in xrange(4):
            print("%.1f" %variacao_sinapses[x])
        print("==========================")
        print("O vetor das sinapses atualizadas: ")
        for x in xrange(4):
            print("%.1f" %self.vetor_sinapses[x])
        print("==========================")

if __name__ == "__main__":
    adaline = Treinamento_Adaline()
    adaline.inicializar_sinapses_mostrar()
    adaline.inicializar_vetores_treinamento_mostrar()
    adaline.inicializar_saidas_desejadas_mostrar()
    adaline.x1.insert(0, 1.0)
    adaline.x2.insert(0, 1.0)
    epoca = 0
    while 1:
        epoca += 1
        print("Epoca: %i" %epoca)
        print("Para o vetor x1:")
        v = 0.0
        v = adaline.calcular_v_do_vetor_treinamento(adaline.x1)
        print("O valor de 'V': %.1f" %v)
        erro1 = 0.0
        erro1 = adaline.calcular_erro(adaline.ydesejado1)
        print("O valor do erro: %.1f" %erro1)
        adaline.atualizar_sinapses_mostrar(adaline.x1)
        print("Para o vetor x2:")
        v = 0.0
        v = adaline.calcular_v_do_vetor_treinamento(adaline.x2)
        print("O valor de 'V': %.1f" %v)
        erro2 = 0.0
        erro2= adaline.calcular_erro(adaline.ydesejado2)
        print("O valor do erro: %.1f" %erro2)
        adaline.atualizar_sinapses_mostrar(adaline.x2)
        erro_medio_quadratico = 0.0
        erro_medio_quadratico = ( (erro1 ** 2) + (erro2 ** 2) ) / 2 
        print("O valor do erro medio quadratico e: %.1f" %erro_medio_quadratico)
        if erro_medio_quadratico < 0.01:
            print("Acabou...")
            break
        else:
            print("Continuando...")
            print("======================================")

from random import randint

class Digito:
    def __init__(self, valor):
        self.peso = valor
        self.alfa = "abcdefghijlmknopqrstuvxywzABCDEFGHIJKLMNOPQRSTUVXYWZ0123456789_#!/\\=+-*"
        self.tm = len(self.alfa)
        self.string = ""

    def gerente(self):
        # Mapear pesos a funções caso seja necessário
        func_map = {
            8: self.case_01,
            9: self.case_02,
            10: self.case_03,
            11: self.case_04,
            12: self.case_05,
            13: self.case_06,
            14: self.case_07,
            15: self.case_08,
            16: self.case_09
        }
        return func_map.get(self.peso, lambda: "")()  # Retorna "" caso peso não exista no mapa

    def gerar_string(self, length):
        return ''.join(self.alfa[randint(0, self.tm - 1)] for _ in range(length))

    # Cada caso agora usa o método `gerar_string` para criar uma string de comprimento específico
    def case_01(self): return self.gerar_string(8)
    def case_02(self): return self.gerar_string(9)
    def case_03(self): return self.gerar_string(10)
    def case_04(self): return self.gerar_string(11)
    def case_05(self): return self.gerar_string(12)
    def case_06(self): return self.gerar_string(13)
    def case_07(self): return self.gerar_string(14)
    def case_08(self): return self.gerar_string(15)
    def case_09(self): return self.gerar_string(16)

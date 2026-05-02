# Abstração e Encapsulamento: abstrai a ideia de quarto de hotel e encapsula detalhes dos atributos.
class Quarto:
    next_numero = 100

    def __init__(self, numero, tipo, capacidade, valor_diaria): # Consatrutor da classe Quarto.
        self.numero = Quarto.next_numero # Número do quarto.
        Quarto.next_numero += 1 # Incrementa.
        self.tipo = tipo        # Característica do quarto.
        self.capacidade = capacidade
        self.valor_diaria = valor_diaria

    def __str__(self):
        return f"Quarto número: {self.numero}\nTipo: {self.tipo}\nCapacidade: {self.capacidade}\nDiária: R$ {self.valor_diaria:.2f}\n"


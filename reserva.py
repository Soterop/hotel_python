import textwrap
from datetime import date           # Importa biblioteca 
from hospede import Hospede         # Importa classe Hospede do módulo hospede.py.
from quarto import Quarto

# Abstração e Encapsulamento: Reserva abstrai o conceito de reserva e encapsula todos os dados e lógica.

class Reserva:
    next_id = 1 # Contador, cada id de reserva se torna único.
    from datetime import datetime
    agora = datetime.now()
    formatar_agora_data = agora.strftime('%d/%m/%y') # Obter a data formatada.
    formatar_agora_hora = agora.strftime('%H:%M:%S')
    dia1 = agora.day
    mes1 = agora.month
    ano1 = agora.year
    data_agora = date(ano1, mes1, dia1)

    def __init__(self, hospede, quarto, entrada, saida): # Construtor da classe Reserva.


        if not isinstance(hospede, Hospede):
            raise ValueError("Hóspede deve ser um objeto da classe Hóspede")
        if not isinstance(quarto, Quarto):
            raise ValueError("Quarto deve ser um objeto da classe Quarto.")
        if not isinstance(entrada, date) or not isinstance(saida, date):
            raise ValueError("As datas de entrada e saída devem ser objeto datetime.date")
        if entrada >= saida:
            raise ValueError("A data de saída deve ser posterior à data de entrada.")
        if (saida <= Reserva.data_agora and entrada < Reserva.data_agora):
            raise ValueError("A data não pode ser anterior ao dia de hoje.")
        

        self.id_reserva = Reserva.next_id # Id único para reserva.
        Reserva.next_id += 1              # Incremento do contador
        self.hospede = hospede
        self.quarto = quarto
        self.entrada = entrada
        self.saida = saida
        self.status = "Confirmada"        # Atributo 'status' da reserva.

    def calcular_total(self):
        total = self.saida - self.entrada # Diferença entre data de entrada e saída.
        return total.days * self.quarto.valor_diaria # Retorna valor total da reserva.
    
    def __str__(self): # String do objeto Reserva.
        mensagem = f"""
Número da reserva: {self.id_reserva}
Hóspede: {self.hospede.get_nome()}\nTelefone: {self.hospede.get_telefone()}\nEmail: {self.hospede.get_email()}\nCPF: {self.hospede.get_cpf()}
Quarto: {self.quarto.numero} - {self.quarto.tipo}
Entrada: {self.entrada.strftime('%d/%m/%y')}
Saída: {self.saida.strftime('%d/%m/%y')}
Status: {self.status}
Valor total: R$ {self.calcular_total():.2f}
"""
        return textwrap.dedent (mensagem)






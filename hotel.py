from hospede import Hospede # Importa classe Hospede.
from funcionario import Funcionario # Importa classe Funcionário.
from quarto import Quarto  # Importa classe Quarto.
from reserva import Reserva # Importa classe Reserva.
from datetime import date # Módulo para trabalhar datas.

#  Abstração e encapculamento: A classe hotel gerencia outras classes e encapsula métodos e listas.

class Hotel:

    def __init__(self, nome): # Construtor da classe Hotel.
        self.nome = nome
        self.quartos = []   # Lista para armazenas objetos Quarto. Encapsulamento de lista.
        self.hospedes = []  # Lista objeto Hospede
        self.funcionarios = [] # Lista objeto Funcionario
        self.reservas = [] # Lista objeto reserva
      

    def adicionar_quarto(self, quarto):
# isinstance, garante entradas válidas, facilita a depuração do código.
        if not isinstance(quarto, Quarto): # Verifica se objeto é instância de Quarto.
            raise ValueError("O objeto deve ser uma instância de Quarto.")
        self.quartos.append(quarto) # Adiciona o quarto à lista.
        print(f"Quarto {quarto.numero} adicionado ao hotel {self.nome}.") # Saída.

    def adicionar_hospede(self, hospede):
# isinstance, garante entradas válidas, facilita a depuração do código.
        if not isinstance(hospede, Hospede): # Verifica se é instância de hospede.
            raise ValueError("O objeto deve se uma instância de Hospede")
        self.hospedes.append(hospede) # Adiciona o hóspede à lista.
        print(f"Hóspede {hospede.get_nome()} adicionado ao hotel {self.nome}.")

    def adicionar_funcionario(self, funcionario):
# isinstance, garante entradas válidas, facilita a depuração do código.
        if not isinstance(funcionario, Funcionario): # Verifica se é instância de Funcionário.
            raise ValueError("O objeto deve ser uma instância de Funcionario.")
        self.funcionarios.append(funcionario) # Adiciona o funcionário à lista.
        print(f"Funcionário {funcionario.get_nome()} adicionado ao hotel {self.nome}.")


    def remover_quarto(self, numero_quarto): # Remove quarto da lista.

        quarto_encontrado = False
        tamanho_antes = len(self.quartos)
        # Cria uma nova lista contendo apenas os hóspedes que NÃO possuem a ID especificada.
        # Forma segura de "remover" itens sem modificar a lista durante a iteração.
        self.quartos = [f for f in self.quartos if f.numero != numero_quarto]

        # Verifica se o tamanho da lista mudou para saber se a reserva foi removida
        if len(self.quartos) < tamanho_antes: # Lógica simplificada para verificação
            quarto_encontrado = True

        if quarto_encontrado:
            # Se a nova lista for menor que a original, significa que uma reserva foi removida.
            print(f"O quarto {numero_quarto} foi removido do hotel {self.nome}.")
            return True # Adiciona um retorno para indicar sucesso
        else:
            print(f"O quarto número {numero_quarto} não foi encontrada no hotel {self.nome}.")
            return False # Adiciona um retorno para indicar falha

            
    def remover_hospede(self, numero_hospede): # Remove Hóspede da lista.

        hospede_encontrado = False
        tamanho_antes = len(self.hospedes)
        # Cria uma nova lista contendo apenas os hóspedes que NÃO possuem a ID especificada.
        # Forma segura de "remover" itens sem modificar a lista durante a iteração.
        self.hospedes = [f for f in self.hospedes if f.id_hospede != numero_hospede]

        # Verifica se o tamanho da lista mudou para saber se a reserva foi removida
        if len(self.hospedes) < tamanho_antes: # Lógica simplificada para verificação
            hospede_encontrado = True

        if hospede_encontrado:
            # Se a nova lista for menor que a original, significa que uma reserva foi removida.
            print(f"O hóspede matrícula {numero_hospede} removido do hotel {self.nome}.")
            return True # Adiciona um retorno para indicar sucesso
        else:
            print(f"A matrícula número {numero_hospede} não foi encontrada no hotel {self.nome}.")
            return False # Adiciona um retorno para indicar falha

                
    def remover_funcionario(self, matricula): # Remove funcionário da lista

        funcionario_encontrado = False
        tamanho_antes = len(self.funcionarios)
        # Cria uma nova lista contendo apenas os funcionários que NÃO possuem a matrícula especificada.
        # Forma segura de "remover" itens sem modificar a lista durante a iteração.
        self.funcionarios = [f for f in self.funcionarios if f.get_matricula() != matricula]

        # Verifica se o tamanho da lista mudou para saber se a reserva foi removida
        if len(self.funcionarios) < tamanho_antes: # Lógica simplificada para verificação
            funcionario_encontrado = True

        if funcionario_encontrado:
            # Se a nova lista for menor que a original, significa que uma reserva foi removida.
            print(f"O funcionário matrícula {matricula} removido do hotel {self.nome}.")
            return True # Adiciona um retorno para indicar sucesso
        else:
            print(f"A matrícula número {matricula} não foi encontrada no hotel {self.nome}.")
            return False # Adiciona um retorno para indicar falha


    def remover_reserva(self, id_reserva): # Remove reserva da lista.

        reserva_encontrada = False
        tamanho_antes = len(self.funcionarios)
        # Cria uma nova lista contendo apenas as reservas que NÃO possuem o ID especificado
        # Forma segura de "remover" itens sem modificar a lista durante a iteração.
        self.reservas = [f for f in self.reservas if f.id_reserva != id_reserva]

        # Verifica se o tamanho da lista mudou para saber se a reserva foi removida
        if len(self.reservas) < tamanho_antes: # Lógica simplificada para verificação
            reserva_encontrada = True

        if reserva_encontrada:
            # Se a nova lista for menor que a original, significa que uma reserva foi removida.
            print(f"A reserva número {id_reserva} foi removida do hotel {self.nome}.")
            return True # Adiciona um retorno para indicar sucesso
        else:
            print(f"A reserva número {id_reserva} não foi encontrada no hotel {self.nome}.")
            return False # Adiciona um retorno para indicar falha


    def fazer_reserva(self, hospede, quarto, entrada, saida): # Faz a reserva

# Iteração (for loop): Verifica disponibilidade.
        for reserva in self.reservas:
        	
            # Condicional (if): verifica se a reserva é mesmo quarto.
            # Evita sobreposição.

            if reserva.quarto == quarto and reserva.status == "Confirmada":
                # Se houver sobreposição imprime erro.

                if not (saida <= reserva.entrada or entrada >= reserva.saida):
                    print(f"Erro: O quarto {quarto.numero} já está reservado no período solicitado de {reserva.entrada.strftime('%d/%m/%y')} a {reserva.saida.strftime('%d/%m/%y')}.")
                    return None # return None: saída se a reserva não puder ser feita.
                
        try: # Detectar possíveis erros.
            nova_reserva = Reserva(hospede, quarto, entrada, saida) # Tenta criar reserva.
            self.reservas.append(nova_reserva) # Adicionar à lista.
            print(f"\nReserva {nova_reserva.id_reserva} feita com sucesso para o hóspede {hospede.get_nome()} no quarto {quarto.numero}.")
            return nova_reserva # Retorna objeto de nova reserva.
        
        except ValueError as e: # except: Captura a exceção ValueError.
            print(f"Erro ao fazer reserva: {e}") # Saída com erro.
            return None # Retorna None no erro.

    def cancelar_reserva(self, id_reserva): # Cancela reserva existente pela id.
        # Iteração percorre lista até encontrar id correspondente.
        for reserva in self.reservas:
            if reserva.id_reserva == id_reserva and reserva.status == "Confirmada":
                reserva.status = "Cancelada" # Altera o status da reserva para Cancelada.
                print(f"\nReserva {id_reserva} cancelada com sucesso.")
                return True # Se o cancelamento foi bem-sucedido.
            print(f"\nReserva {id_reserva} não encontrada ou já cancelada/finalizada.")
            return False # Não encontrada

    def listar_quartos(self):
        print(f"\nQuartos no {self.nome}\n")
        if not self.quartos: # Verifica lista vazia.
            print("\nNenhum quarto registrado.")
            return [] # Retorna lista vazia.
        for quarto in self.quartos: # Iteração, percorre lista e imprime quartos.
            print(f"{quarto}")
        return self.quartos  # Lista completa de quartos.
    
    def listar_hospedes(self):
        print(f"\nHóspedes no {self.nome}\n")
        if not self.hospedes: # Verifica se lista está vazia.
            print("\nNenhum hóspede registrado.")
            return []
        for hospede in self.hospedes: # Iteração na lista para cada hóspede.
            print(f"{hospede}")
        return self.hospedes
    
    def listar_funcionarios(self):
        print(f"\nFuncionários no {self.nome}\n")
        if not self.funcionarios: # Verifica se a lista está vazia.
            print("Nenhum funcionário registrado.")
            return []
        for funcionario in self.funcionarios: # Iteração na lista para cada funcionário.
            print(f"-{funcionario}-")
        return self.funcionarios
    
    def listar_reservas(self):
        print(f"\nReservas no {self.nome}\n")
        if not self.reservas: # Verifica se lista está vazia.
            print("\nNenhuma reserva registrada.")
            return []
        for reserva in self.reservas: # Iteração, percorre e imprime cada reserva.
            print(f"\n{reserva}")
        return self.reservas
        
    def buscar_hospede_por_id(self, id_hospede):
        for hospede in self.hospedes: # Iteração lista de hóspedes
            if hospede.id_hospede == id_hospede: # Condicional que compara id.
                return hospede # Retorna o objeto se encontrado.
        return None # Se nenhum quarto for encontrado.
            
    # Busca um quarto pelo número.
    def buscar_quarto_por_numero(self, numero):
        for quarto in self.quartos: # iteração: percorre a lista de quartos.
            if quarto.numero == numero: # condicional: compara o número do quarto.
                return quarto # return: retorna o objeto quarto se encontrado.
        return None # none: retorna none se nenhum quarto com o número for encontrado.

    # representação em string de um objeto hotel.
    def __str__(self):
        return f"hotel {self.nome} com {len(self.quartos)} quartos, {len(self.hospedes)} hóspedes e {len(self.reservas)} reservas."



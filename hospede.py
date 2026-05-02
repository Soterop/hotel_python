from pessoa import Pessoa # Importa a classe Pessoa do módulo pessoa.py

# Herança: A classe Hóspede herda atributos de Pessoa e adiciona outros.
# Reutilização do código.
class Hospede(Pessoa):  # Hóspede recebe atributos de Pessoa.
    next_id = 1     # Contador.

    def __init__(self, nome, telefone, email, cpf): # Construtor.
        super().__init__(nome, telefone, email, cpf) # Chama construtor da classe pai (Pessoa).
        self.id_hospede = Hospede.next_id      
		# ID único para hóspede
        Hospede.next_id += 1 # Incrementa próximo hóspede
    
          
    
    def __str__(self): # Polimorfismo: Sobrescreve o método __str__ adicionando ID do hóspede.
    		return f"Hóspede número de identificação: {self.id_hospede}\n{super().__str__()}\n"
	
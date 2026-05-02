from pessoa import Pessoa # Importa a classe Pessoa do módulo pessoa.py

# Herança, Funcionário herda de Pessoa.
# Reutilização da lógica e atributos de Pessoa.

class Funcionario(Pessoa):
    next_matricula = 101 # Contadorpara gerar matrículas únicas iniciado em 101.

# Construtor da classe Funcionario herda atributos e adiciona cargo e salário.
    def __init__(self, nome, telefone, email, cpf, cargo, salario):
    	
        super().__init__(nome, telefone, email, cpf) #super, chama construtor classe pai (Pessoa)
        self.__matricula = Funcionario.next_matricula  # Atribui matrícula única.
        Funcionario.next_matricula += 1 # Incrementa o contador.
        self.__cargo = cargo
        self.__salario = salario

    def get_matricula(self):
        return self.__matricula
    
    def set_matricula(self, matricula):
        self.__matricula = matricula
        return self.__matricula

    def get_cargo(self):
        return self.__cargo
    
    def set_cargo(self, cargo):
        self.__cargo = cargo
        return self.__cargo
    
    def get_salario(self):
        return self.__salario
    
    def set_salario(self, salario):
        self.__salario = salario
        return self.__salario


# Polimorfismo: O método __str__ é sobrescrito para adaptar ao funcionário.
# Adiciona-se matrícula, cargo e salário.

    def __str__(self):
        return f"Funcionário Matrícula: {self.get_matricula()}\nCargo: {self.get_cargo()}\nSalário: {self.get_salario()}\n{super().__str__()}\n"


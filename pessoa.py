from datetime import date   # Importa datetime para trabalhar com datas.

# Abstração dos atributos comuns de pessoa.
# Encapsulamento dos atributos de pessoa.

class Pessoa:
# Método __init__ é o construtor da classe. Chamado para criar novo objeto Pessoa.
# self: refere-se a instância atual da classe.
# nome, telefone, email, cpf são atributos de Pessoa.

    def __init__(self, nome, telefone, email, cpf):
        self.__nome = nome    # Padrão atribuir valor do parâmetro ao atributo da instância.
        self.__telefone = telefone
        self.__email = email
        self.__cpf = cpf


    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
        return self.__nome

    def get_telefone(self):
        return self.__telefone
    
    def set_telefone(self, telefone):
        self.__telefone = telefone
        return self.__telefone
    
    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email
        return self.__email
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, cpf):
        self.__cpf = cpf
        return self.__cpf
    
    def exibir_dados(self):
        pass
    

# Método __str__ define a representação em string de um objeto. Chamado por print().
    def __str__(self):
        return f"Nome: {self.get_nome()}\nTelefone: {self.get_telefone()}\nEmail: {self.get_email()}\nCPF: {self.get_cpf()}\n "
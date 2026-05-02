# https://youtu.be/EM0Uo-_chPI
# Link vídeo Sistematização - Programação Orientada a Objetos - Plínio Sotero de Sousa
from datetime import date # Módulo para trabalhar datas.
from textwrap import dedent # Usado para formatação do texto.
import webbrowser
import os # usado para adicionar comando para limpar o prompt.

# Importando classes dos Módulos.
from pessoa import Pessoa
from hospede import Hospede
from funcionario import Funcionario
from quarto import Quarto
from reserva import Reserva
from hotel import Hotel

def limpa():           # Comando para limpar terminal.
    if os.name == 'nt':
        os.system('cls')    # limpar terminal do windows.
    else:
        os.system('clear')  # Limpar terminal no linux e mac.

def exibir_menu():

    print("Data:", Reserva.formatar_agora_data, "\nHora:", Reserva.formatar_agora_hora, "\n")
    srtMult = dedent ("""\
            Hotel - Programação Orientada a Objetos
Opções:____________________________________________________________
|  Adicinoar:                   |                                  |
|  1. Quarto                    |  4. Reserva (Fazer/ Cancelar)    |
|  2. Hóspede                   |  5. Listar                       |
|  3. Funcionário               |  6. Excluir (Atenção!)           | 
|  x. Abrir vídeo no youtube    |  0. Sair                         |
|_______________________________|__________________________________|

""") # Menu com formatação livre.    
    print(srtMult)  # Printa texto do menu.
    return input("Escolha uma opção: ") # Reconhece entrada do usuário.

def obter_data(prompt): # Função para obter data válida do usuário.
    while True:
        data_str = input(prompt + " (formato DD/MM/AAAA, exemplo 4/8/2016): ") 
        
        try:
            dia, mes, ano = map(int, data_str.split('/')) # Tenta dividir e converter a string.
            return date(ano, mes, dia) # Retorna objeto date se houver a conversão.
        except ValueError: # Captura a excessão ValueError, facilita na depuração.
            print("Formato de data inválido. Use DD/MM/AAAA, exemplo 2/4/1981")

# Bloco principal de execução. Só roda quando o arquivo é executado diretamente.
if __name__ == "__main__":
    meu_hotel = Hotel("POO - CEUB") # Cria instância do objeto Hotel.
    print(f"\nSistema iniciado: {meu_hotel.nome}")

    while True: # Iteração do menu.
        opcao = exibir_menu() # Chama a função criada para o menu.

        # Condicional para acessar as diferentes opções do menu.
        if opcao == '1': # 1. Adicionar Quarto.
            limpa()
            try: # Lidando com entradas inválidas.

                prompt_mul1 = dedent("""\
                                     
_Tipo do quarto:_
| 1. Solteiro    |
| 2. Casal       |
| 3. Master      |
| 4. Deluxe)     |
|________________|
Escolha uma opção: """)
                print("")
                ent = input(prompt_mul1) # Comando para entrada do usuário.
                if ent == '1':
                    tipo = "solteiro" # Opções de tipo de quarto.
                elif ent == '2':
                    tipo = "Casal"
                elif ent == '3':
                    tipo = "Master"
                elif ent == '4':
                    tipo = 'Deluxe'
                    
                else:
                    print("Digite um valor válido.")
                limpa()
                print("\nTipo de quarto: ",tipo)
                capacidade = int(input("Capacidade do quarto: "))
                valor_diaria = float(input("Valor da diária: R$ ")) # Entrada com conversão para float.
                quarto = Quarto("numero", tipo, capacidade, valor_diaria) # Cria instância de quarto.
                meu_hotel.adicionar_quarto(quarto)  # Método Hotel para adicionar quarto.
                print("\nPressione ENTER para continuar.")
                input()
                limpa()

            except ValueError:
                print("Entrada inválida. Verifique os tipos de dados.") # Comando indicando erro.
                
        elif opcao == '2': # Adicionar hóspede.
                limpa()
                nome = input("\nNome do hóspede: ")
                telefone = input("Telefone do hóspede: ")
                email = input("Email do hóspede: ")
                cpf = input("CPF do hóspede: ")
                hospede = Hospede(nome, telefone, email, cpf) 
                meu_hotel.adicionar_hospede(hospede)
                print("\nPressine ENTER para continuar.")
                input()
                limpa()
                
        elif opcao =='3': # Adicionar Funcionário.
                limpa()
                print("")
                nome = input("Nome do funcionário: ")
                telefone = input("Telefone do funcionário: ")
                email = input("Email do funcionário: ")
                cpf = input ("CPF do funcionário: ")
                prompt_mul2 = dedent("""\
                                     
_Cargo do Funcionário:______
| 1. Concierge              |
| 2. Supervisor de Limpeza  | 
| 3. Chef de Cozinha        |
| 4. Manutenção             |
| 5. Gerente Geral          |
| 6. Gerente de Receitas    |                                                                  
|___________________________|
Escolha uma opção: """)

                cargo = input (prompt_mul2)
                
                if cargo == '1':
                    cargo = "Concierge"
                elif cargo == '2':
                    cargo = "Supervisor de Limpeza"
                elif cargo =='3': 
                    cargo = "Chef de Cozinha"
                elif cargo == '4':
                    cargo = "Manutenção"
                elif cargo == '5':
                    cargo = "Gerente Geral"
                elif cargo == '6':
                    cargo = "Gerente de Receitas"
                else:
                    print("Faltou algum campo para preenchimento.")
                limpa()
                print("\nNome do funcionário: ",nome)
                print("Telefone do funcionário: ", telefone)
                print("Email do funcionário: ", email)
                print("CPF do funcionário:", cpf)
                print("Cargo do Funcionário: ", cargo)
                salario = input("Salário do funcionário: R$ ")
                funcionario = Funcionario(nome, telefone, email, cpf, cargo, salario)
                meu_hotel.adicionar_funcionario(funcionario)
                print("\nPressione ENTER para continuar.")
                input()
                limpa()
                
        elif opcao =='4':
            limpa()
            prompt_mul3 = dedent("""\
                                     
__Opções:________________
| 1. Fazer Reserva       |
| 2. Cancelar Reserva    |
| 3. Voltar              |                                                       
|________________________|
Escolha uma opção: """)

            reserv = input(prompt_mul3)

            if reserv == '1':  # Fazer Reserva.
                try:
                    meu_hotel.listar_hospedes() # Listar hóspedes para o usuário escolher.
                    id_hospede = int(input("Número de identificação do hóspede para reserva: "))
                    hospede = meu_hotel.buscar_hospede_por_id(id_hospede)
                    
                    meu_hotel.listar_quartos() # Lista de quartos para escolha do usuário.
                    
                    numero_quarto = int(input("Número do quarto para reserva: "))
                    print("")
                    quarto = meu_hotel.buscar_quarto_por_numero(numero_quarto)
                    print("Data:", Reserva.formatar_agora_data, "Hora:", Reserva.formatar_agora_hora)
                    if hospede and quarto: # Verifica se foram encontrados hóspede e quarto.
                    	
             
                        entrada = obter_data("Data de entrada")
                        saida = obter_data("Data de saída")
                        
                        if entrada and saida: # Verifica se datas são válidas.
                            meu_hotel.fazer_reserva(hospede, quarto, entrada, saida) # Realiza a reserva.
                            print("\nPressione ENTER para continuar.")
                            input()
                            limpa()
                            
                    else:
                            print("Hóspede ou Quarto não encontrado.")
                            print("\nPressione ENTER para continuar.")
                            input()
                            limpa()
                            
                except ValueError:
                    print("Entrada inválida.")
                    print("\nPressione ENTER para continuar.")
                    input()
                    limpa()

            elif reserv == '2': # Cancelar Reserva.
                try:
                    meu_hotel.listar_reservas()
                    id_reserva = int(input("Número da reserva para cancelar: "))
                    meu_hotel.cancelar_reserva(id_reserva) # Altera para cancelada.
                    print("\nPressione ENTER para continuar.")
                    input()
                    limpa()
                    
                except ValueError:
                    print("\nEntrada inválida.")

            elif reserv == '3': # Voltar.
                pass
                limpa()

            else:
                print("\nDigite valor válido.")
                
        
        elif opcao == '5': # Listar.
          limpa()
          prompt_mul4 = dedent("""\

__Listar:____________
| 1. Quartos         |
| 2. Hóspedes        |
| 3. Funcionários    |
| 4. Reservas        |                                                       
| 5. Voltar          |
|____________________|
Escolha uma opoção: """)
          
          
          liste = input(prompt_mul4)
          limpa()
          if liste == '1': # Quartos.
               meu_hotel.listar_quartos()
               print("\nPressione ENTER para continuar.")
               input()
               limpa()
          elif liste == '2': # Hóspedes.
               meu_hotel.listar_hospedes()
               print("\nPressione ENTER para continuar.")
               input()
               limpa()
          elif liste == '3': # Funcionários.
               meu_hotel.listar_funcionarios()
               print("\nPressione ENTER para continuar.")
               input()
               limpa()
          elif liste == '4': # Reservas.
               meu_hotel.listar_reservas()
               print("\nPressione ENTER para continuar.")
               input()
               limpa()
          elif liste == '5': # Volar.
               pass
               limpa()
          else:
               print("\nEntrada inválida.")
        elif opcao == '6': # Remover
            limpa()
            prompt_mul5 = dedent("""\
            	
__Remover:____________
| 1. Quartos         |
| 2. Hóspedes        |
| 3. Funcionários    |
| 4. Reservas        |                                                       
| 5. Voltar          |
|____________________|                                 
Escolha uma opção: """)
            exc = input(prompt_mul5)
            if exc == '1':
                    if exc == '1': # Remover Quarto
                        limpa()
                        sim = input("\nCUIDADO - Você tem certeza? Digite 'Sim' ou x para continuar: ")
                        if sim == "Sim":  

                            numero_quarto_str = input("Digite o número do quarto que deseja excluir: ")
                            try:  # Evite erro de inserção, strings, int
                                numero_quarto_remov = int(numero_quarto_str)
                            except ValueError:
                                print(f"Entrada inválida. '{numero_quarto_str}' não é um número de quarto válido.")
                   
                            meu_hotel.remover_quarto(numero_quarto_remov) # Método em hotel para remover quarto.
                            print("\nPressione ENTER para continuar.")
                            input()
                            limpa()
                        else:
                            pass
                            limpa()

            elif exc =='2':
                    if exc == '2':  # Remover hóspede
                        limpa()
                        sim = input("\nCUIDADO - Você tem certeza? Digite 'Sim' ou x para continuar: ")
                        if sim == "Sim":

                            numero_hospede_str = input("Digite o número de identificação que deseja excluir: ")
                            try: # Evitar erro de inserção pelo tipo da variável.
                                numero_hospede_remov = int(numero_hospede_str)
                            except ValueError:
                                print(f"Entrada inválida. '{numero_hospede_str}' não é uma ID de hóspede válido.")
                        
                            meu_hotel.remover_hospede(numero_hospede_remov)
                            print("\nPressione ENTER para continuar.")
                            input()
                            limpa()
                        else:
                            pass
                            limpa()   

            elif exc =='3':
                    if exc == '3': # Remover Funcionário
                        limpa()
                        sim = input("\nCUIDADO -Você tem certeza? Digite 'Sim' ou x para continuar: ")
                        if sim == "Sim":
                            
                      #     matricula_remover = int(input("Digite a matrícula do funcionário: "))
                            matricula_str = input("Digite a matrícula do funcionário: ")
                            try:
                                matricula_remov = int(matricula_str)
                            except ValueError:
                                print(f"Entrada inválida. '{matricula_str}' não é uma matrícula de funcionário válido.")
                              
                            meu_hotel.remover_funcionario(matricula_remov)
                            print("\nPressione ENTER para continuar.")
                            input()
                            limpa()
                        else:
                            pass
                            limpa()                
            elif exc =='4':
                    if exc == '4': # Remover reserva.
                        limpa()
                        sim = input("\nCUIDADO -Você tem certeza? Digite 'Sim' ou x para continuar: ")
                        if sim == "Sim": 

                            reserva_str = input("Digite o número da reserva: ")
                            try:
                                reserva_remover = int(reserva_str)
                            except ValueError:
                                print(f"Entrada inválida. '{reserva_str}' não é um número de reserva válida.")

                            meu_hotel.remover_reserva(reserva_remover)
                            print("\nPressione ENTER para continuar.")
                            input()
                            limpa()
                        else:
                            pass
                            limpa()  


            elif exc =='5':
                pass
                limpa()
           
            else:
               print("\nEntrada inválida.")                
            
        elif opcao == 'x': # Abrir vídeo no youtube
            
            import webbrowser
            webbrowser.open('https://youtu.be/EM0Uo-_chPI')
            print("\nVídeo abrindo no seu navegador.\nPressione ENTER para continuar.")
            input()
            limpa()
                
        elif opcao == '0': # Sair
            print("\nEncerrada a sessão.")
            break # Interrompe o loop''while True' imediatamente.
            
        else:
            print("\nTente novamente. Data expirada.")



        
                    

        





    


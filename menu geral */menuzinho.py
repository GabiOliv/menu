import os
import time
#Teste
print("========= Aperte enter para entrar ========== \n")
#então pessoal, toda vez que eu acresentar um: def (alguma coisa), estou me relacionando ao método que irei usar.
def movimentação(): 
  #aqui estou usando o método movimentação
  

  def saldo():
    print("[Clique no número 1 para ver saldo] \n")
    print("[Clique no número 2 para voltar ao menu] \n")
    z=input()
    if z=="1": #Se z for igual a 1, ele lhe trará o saldo
      print("Seu saldo é: \n ") 
      menu()
    else: # se não, voltará ao menu
      menu()

  def extrato():
    print("[ Digite o número 1 para ver extrato] \n")
    print( 35*("-+")) # você encontrará muito essa parte de: 35*("-+")
    #isso só é uma forma de separar as linhas e deixar um pouco mais estiloso o código
    print("[Digite o número 2 para voltar ao menu] \n") 

    print(25*("-+"))

    y=input() # aqui fora criado um input com a váriavel y
    if y==1: 
      print("extrato") #Se y for igual a 1, ele nos mostrará o extrato
      menu()
    else:
      menu() #Se não, voltará para o menu

  def trans():
    print("[Digite o número 1 para verificar transações recentes] \n")
    print(15*("-+"))
    print("[Digite o número 2 para fazer uma transaçao] \n")
    print(15*("-+"))
    print("[Digite o número 3 para voltar ao menu] \n")
    print(15*("-+"))
    o=input()
    if o==1: #Se a opção for 1, ele lhe mostrará quanto você gastou
      print("vc gastou ...\n")
      menu()
    elif o==2:
      print("[qual valor da transação] \n") #se a opção for 3, ele lhe mostrará o valor da transação
      menu()
      print(15*("-+"))

    else:
      menu()  # Se não, voltará para o menu

  def menu(): # aqui, criamos um método menu, para que o usuário escolha qual opção ele deseja
    print("[Digite o número 1 para saldo] \n")
    print(15*("-+"))
    print("[Digite o número 2 para extrato] \n")
    print(15*("-+"))
    print("[Digite o número 3 para transação] \n")
    print(15*("-+"))
    x =input() #novamente criamos um input, agora com a variavel x
    if x=="1": # se o que o usuário escolher for a opção 1, ele irá direto para o método saldo
      saldo()
    if x=="2": # se o que o usuário escolher for a opção 1, ele irá direto para o método extrato
      extrato()
    if x=="3": # se o que o usuário escolher for a opção 1, ele irá direto para o método trans
      trans()

  menu()
def principal():
    lista = [] # inicializa a lista vazia
    while True: 
        time.sleep(2)
        os.system("cls");
        print(" === MÓDULO CLIENTE === ")
        print( 35*("-+"))
        print("[1 - Cadastrar Banco ou Fintech]")
        print( 35*("-+"))
        print("[2 - Editar Cadastro]")
        print( 35*("-+"))
        print("[3 - Listar Banco ou Fintech]")
        print( 35*("-+"))
        print("[4 - Sair do Sistema do Banco]")
        print( 35*("-+"))
        opcao = int(input("[Digite o Opção Desejada:]"))
        print( 35*("-+"))

        if opcao == 1:
            print("\n Digite o Nome da Empresa: ")
            print( 35*("-+"))
            print("\n Digite o CNPJ da Empresa: ")
            print( 35*("-+"))
            print("\n Digite Localização da Empresa: ")
            print( 35*("-+"))
            print("\n Digite a Inscrição Estadual da Empresa: ")
            print( 35*("-+"))
            print("\n Escolher Funcionalidades: S ou N ")
        # print("\n  - Saque:")
        # print("\n  - Depósito:")
        # print("\n  ...")

        if opcao == 2:
            print("\n Digite o CNPJ da Empresa: ")
            print( 35*("-+"))
            print("\n Digite um Novo Nome:")
            print( 35*("-+"))
            print("\n Digite uma Nova Localização:")
            print( 35*("-+"))
            print("\n Digite uma Nova Inscrição Estadual:")
            print( 35*("-+"))
            print("\n Escolha Novas Funcionalidades:")
        # print("\n  - Saque:")
        # print("\n  - Depósito:")
        # print("\n  ...")
            print("\n Escolha o Estado do Banco:")
        # print("\n  Ativo: S ou N")

        if opcao == 3:
            #print("\n DECIDIR POR PEGAR INDIVIDUAL PELO NOME DO ARQUIVO OU COLETIVO DE TODAS EMPRESAS PELA PASTA COM TODOS ARQUIVOS ARMAZENADOS")

            #INDIVIDUAL
            print("\n Digite o CNPJ da Empresa: \n")

            #GERAL
            #LISTAR DIRETO
            #opção de parar de listar

        if opcao == 4:
            print("\n Saindo do Programa...")
            break







def adm():
    lista = [] 
    while True:
        time.sleep(2)
        os.system("cls");
        print(" ============= Módulo administrativo =============")
        print("1 - Acessar área de alimentação de cédulas")
        print("2 - Acessar Sangria")
        print("3 - Acessar área de relatórios")
        print("4 - Sair")
        opcao = int(input("Digite qual área gostaria de acessar:"))

        if opcao == 1:
            print("\n  Aqui estamos falando da reposição das notas do caixa.  Portanto, essa área vai  definirá  o valor no qual o caixa entra em sinal vermelho e irá precisar da realimentação de cédulas, para quue haja a reposição de cédulas. ")
        # irá alimentar as cédulas
            time.sleep(9)

        if opcao == 2:
            print("\n Aqui, quando o dinheiro for movimentado ser o planejamento do próprio banco, por segurança, será alocado para um lugar especifíco.")
            time.sleep(9)
        # sangria

        if opcao == 3:
        
            print("\n Aqui, o caixa irá emitir/mostrar um relatório para que nós do administrativo tenhamos controle de suas movimentações em determinado período de tempo, como por exemplo a quantidade de extratos emitidos, saques, depósitos, transferências e toda a quantia de dinheiro envolvida nestes processos.")
            time.sleep(9)
    
            #irá gerar o arquivo txt

        if opcao == 4:
            print("\n Saindo do Programa...")
            break




print("----------MENU-----------")
print("Para entrar na aba cliente digite 1")
print("Para entrar na aba movimentação digite 2")
print("Para entrar na aba administração digite 3")
print("-------------------------")
decisao = input("O que você quer fazer?")
if decisao == "1":
   principal()

elif decisao == "2":
    movimentação()

elif decisao =="3":
    adm()

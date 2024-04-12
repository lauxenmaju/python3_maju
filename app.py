#1 10/04 imoport lib os (operational system)
import os

restaurante=[]

#2 declarando a função finalizar_app
def finalizar_app():
    os.system('clear')
    print ('Finalizando o app\n')

def chamar_nome_do_app():
    print ("Restaurante Expresso\n")

# 12 criando opção_invalida
def opcao_invalida():
    print ('opção invalida\n')
    input('Digite uma tecla para voltar ao menu principal:')
    main()
    
def exibir_opcoes():
    print ("1 Cadastrar Restaurante")
    print ("2 Listar Restaurante")
    print ("3 Ativar Restaurente")
    print ("4 Sair\n")


def cadatrar_novo_restaurante():
    os.system('clear')
    nome_do_restaurante= input('digite o nome do novo restaurante:')
    restaurante.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante}, foi cadastrado com sucesso\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()

#8 declarando a função opcao_digitada1
def escolher_opcao():
    #11 adcionando o try
    try:
        opcao_digitada = (int(input("Escolha uma opção")))
        print ("Você selecionou:",opcao_digitada, "\n")
        if(opcao_digitada==1):
            print("Você escolheu Cadastrar Restaurante\n")
            cadatrar_novo_restaurante()
        elif(opcao_digitada==2):
            print("Você escolheu Listar Restaurante\n") 
        elif(opcao_digitada==3):
            print ("Voce escolheu Ativar Restaurante\n")
        elif(opcao_digitada==4):
             print('Voce escolheu sair do programa') 
             finalizar_app()
        #3 chamando a função finalizar_app 
        else:
            opcao_invalida()
    except:
        opcao_invalida()         
  
  #5 escrever a funçaõ main
def main():
    #10 clear
    os.system('clear')
    #6 chamar o nome do app
    chamar_nome_do_app()
    #7 chamar a escolha de opções
    exibir_opcoes()
    #9 chamar a opção digitada
    escolher_opcao()

#4 criando a entrada através da variável main
if(__name__=='__main__'):
    main()

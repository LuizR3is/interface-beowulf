import os
import paramiko


# Função responsável por fazer o ssh entre o código e o node1
def entra_node1():
    address = '192.168.1.12'
    username = 'so'
    password = '01'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=address, username=username, password=password)

    return ssh


def entra_node2():
    address = '192.168.1.14'
    username = 'so'
    password = '01'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=address, username=username, password=password)

    return ssh


# Função responsável por fechar o ssh após concluir alguma funcionalidade
def fecha_ssh(ssh):
    ssh.close()


# Função responsável por executar a funcionalidade 1, a listagem de arquivos de um determinado diretório
def listagem_arquivos():
    os.system('clear')
    endereco = input('Informe o endereço do diretório que deve ter seus arquivos listados: ')

    ssh = entra_node1()  # Faz o SSH com o node1

    stdin, stdout, stderr = ssh.exec_command('ls ' + endereco)  # Roda o comando em node1 e retorna a lista de arquivos
    lista = stdout.readlines()

    for arq in lista:
        print(arq)

    fecha_ssh(ssh)


# Função responsável por executar a funcionalidade 2, a listagem extendida de arquivos de um determinado diretório,
def listagem_filtrada():
    os.system('clear')
    print('A listagem desses arquivos do diretório segue a ordenação "Modificados Recentemente"\n')
    endereco = input('Informe o endereço do diretório que deve ter seus arquivos listados: ')

    ssh = entra_node1()  # Faz o SSH com o node1

    stdin, stdout, stderr = ssh.exec_command('ls -t ' + endereco)  # Roda o comando em node1 e retorna a lista de arquivos ordenados por modificados recentemente
    lista = stdout.readlines()

    for arq in lista:
        print(arq)

    fecha_ssh(ssh)


def criar_copia():
    os.system('clear')
    copiado = input('Informe qual arquivo ou pasta deseja copiar: ')
    copia = input('Informe o nome da futura cópia: ')

    ssh1 = entra_node1()  # Faz o SSH com o node1

    stdin, stdout, stderr = ssh1.exec_command('cp ' + copiado + ' ' + copia)

    fecha_ssh(ssh1)
    
    ssh2 = entra_node2()
    
    stdin, stdout, stderr = ssh2.exec_command('cp ' + copiado + ' ' + copia)

    fecha_ssh(ssh2)


def criar_arquivo():
    os.system('clear')
    nome_arquivo = input('Informe o nome do arquivo que deseja criar: ')

    ssh1 = entra_node1()  # Faz o SSH com o node1

    stdin, stdout, stderr = ssh1.exec_command('touch ' + nome_arquivo)

    fecha_ssh(ssh1)

    ssh2 = entra_node2()

    stdin, stdout, stderr = ssh2.exec_command('touch ' + nome_arquivo)

    fecha_ssh(ssh2)


def menu():
    opcao = 99

    while(opcao != 0):
        print('*********************************************************')
        print('                        Interface                        ')
        print('*********************************************************')

        print('Menu de Funcionalidades: ')
        print('1- Listagem de arquivos')
        print('2- Listagem de arquivos extendida (tempo)')
        print('3- Criar cópia de arquivo ou diretório')
        print('13- Criar arquivos')
        print('0- Sair')
        print('*********************************************************')

        opcao = int(input('Digite o número da opção que deseja selecionar: '))

        if(opcao == 1):
            listagem_arquivos()
            input('\n\nTecle ENTER para voltar ao menu...')
            os.system('clear')

        if(opcao == 2):
            listagem_filtrada()
            input('\n\nTecle ENTER para voltar ao menu...')
            os.system('clear')

        if(opcao == 3):
            criar_copia()
            input('\n\nTecle ENTER para voltar ao menu...')
            os.system('clear')

        if(opcao == 13):
            criar_arquivo()
            input('\n\nTecle ENTER para voltar ao menu...')
            os.system('clear')


menu()

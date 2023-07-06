import os
import paramiko


# Função responsável por fazer o ssh entre o código e o node1
def entra_node1():
    # Informações referentes ao endereço de IP, username e senha para ter acesso ao node1
    address = '192.168.1.12'
    username = 'so'
    password = '01'

    ssh1 = paramiko.SSHClient()
    ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh1.connect(hostname=address, username=username, password=password)

    return ssh1


# Função responsável por fazer o ssh entre o código e o node2
def entra_node2():
    # Informações referentes ao endereço de IP, username e senha para ter acesso ao node2
    address = '192.168.1.14'
    username = 'so'
    password = '01'

    ssh2 = paramiko.SSHClient()
    ssh2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh2.connect(hostname=address, username=username, password=password)

    return ssh2


# Função responsável por fechar o ssh após concluir alguma funcionalidade
def fecha_ssh(ssh):
    ssh.close()


# Função responsável por executar a funcionalidade de listagem de arquivos de um determinado diretório
def listagem_arquivos():

    print('')

    if(len(argumentos) >= 2):
        stdin, stdout, stderr = node1.exec_command('ls ' + argumentos[1])  # Roda o comando em node1 e retorna a lista de arquivos
    else:
        stdin, stdout, stderr = node1.exec_command('ls')

    lista = stdout.readlines()

    for arq in lista:
        print(arq, end='')

    print('')


# Função responsável por executar a funcionalidade de listagem extendida de arquivos de um determinado diretório, ordenados por modificado recentemente
def listagem_filtrada():

    print('')

    if (len(argumentos) >= 2):
        stdin, stdout, stderr = node1.exec_command('ls -t ' + argumentos[1])  # Roda o comando em node1 e retorna a lista de arquivos
    else:
        stdin, stdout, stderr = node1.exec_command('ls -t')

    lista = stdout.readlines()

    for arq in lista:
        print(arq, end='')

    print('')


# Função que faz uma cópia de um arquivo ou diretório
def criar_copia():

    node1.exec_command('cp ' + argumentos[1] + ' ' + argumentos[2])
    node2.exec_command('cp ' + argumentos[1] + ' ' + argumentos[2])


# Função que executa a funcionalidade de criar um arquivo
def criar_arquivo():

    node1.exec_command('touch ' + argumentos[1])
    node2.exec_command('touch ' + argumentos[1])


# Função que faz a renomeação de um arquivo ou pasta
def renomear():

    node1.exec_command('mv ' + argumentos[1] + ' ' + argumentos[2])
    node2.exec_command('mv ' + argumentos[1] + ' ' + argumentos[2])


# Função que move um arquivo ou pasta de um diretório para outro
def mover():

    node1.exec_command('mv ' + argumentos[1] + ' ' + argumentos[2])
    node2.exec_command('mv ' + argumentos[1] + ' ' + argumentos[2])


# Função que remove um arquivo de um diretório
def remover_arquivo():

    node1.exec_command('rm ' + argumentos[1])
    node2.exec_command('rm ' + argumentos[1])


# Função que cria um diretório
def criar_diretorio():

    node1.exec_command('mkdir ' + argumentos[1])
    node2.exec_command('mkdir ' + argumentos[1])


# Função que remove um diretório
def remover_diretorio():

    node1.exec_command('rm -r ' + argumentos[1])
    node2.exec_command('rm -r ' + argumentos[1])


# Função responsável pela inserção de um texto dentro de um arquivo
def inserir_arq():

    node1.exec_command('echo ' + argumentos[1] + ' >> ' + argumentos[2])
    node2.exec_command('echo ' + argumentos[1] + ' >> ' + argumentos[2])


# Função responsável por exibir o conteúdo de algum arquivo
def exibir_arq():

    stdin, stdout, stderr = node1.exec_command('cat ' + argumentos[1])
    lista = stdout.readlines()

    for i in lista:
        print(i)


# Função que exibe o manual de instruções dos comandos disponíveis na interface
def manual():
    print('MANUAL DOS COMANDOS')
    print('1- listar: Lista os arquivos e diretórios presentes naquele diretório.\nFormato esperado: listar [endereço do diretório]\nCaso o argumento seja vazio, listará a pasta ~compartilhada~, que está na home.\nExemplo: listar compartilhada/pasta\n')
    print('2- listar_t: Lista os arquivos e diretórios ordenando pelos modificados recentemente primeiro.\nFormato esperado: listar_t [endereço do diretório]\nCaso o argumento seja vazio, listará a pasta ~compartilhada~, que está na home.\nExemplo: listar_t compartilhada/pasta\n')
    print('3- copiar: Faz uma cópia do arquivo ou pasta selecionado.\nFormato esperado: copiar [endereço de origem com o nome do arquivo] [endereço de destino com o nome do arquivo]\nExemplo: copiar compartilhada/teste.txt compartilhada/copia.txt\n')
    print('4- criar_arq: Cria um arquivo no diretório selecionado.\nFormato esperado: criar_arq [endereço com o nome do arquivo]\nExemplo: criar_arq compartilhada/pasta/teste.txt\n')
    print('5- mover: Move um arquivo ou diretório de um lugar para o outro.\nFormato esperado: mover [endereço de origem com o nome do arquivo] [endereço de destino com o nome do arquivo]\nExemplo: mover compartilhada/teste.txt compartilhada/pasta/movido.txt\n')
    print('6- renomear: Renomeia arquivo ou diretório.\nFormato esperado: renomear [endereço com o nome atual do arquivo] [endereço com o futuro nome do arquivo]\nExemplo: renomear compartilhada/teste.txt compartilhada/novonome.txt\n')
    print('7- remover_arq: Remove um arquivo do diretório.\nFormato esperado: remover_arq [endereço com o nome do arquivo]\nExemplo: remover_arq compartilhada/teste.txt\n')
    print('8- criar_dir: Cria uma pasta/diretório.\nFormato esperado: criar_dir [endereço com o nome da nova pasta]\nExemplo: criar_dir compartilhada/pasta/novapasta\n')
    print('9- remover_dir: Remove um diretório e apaga os arquivos dentro dele.\nFormato esperado: remover_dir [endereço com o nome da pasta]\nExemplo: remover_dir compartilhada/pasta/exemplo\n')
    print('10- inserir_arq: Insere algum texto dentro de um arquivo.\nFormato esperado: inserir_arq [texto que deseja inserir] [endereço com o nome do arquivo]\nExemplo: inserir_arq exemplo teste.txt\n')
    print('11- exibir_arq: Exibe o conteúdo do arquivo.\nFormato esperado: exibir_arq [endereço com o nome do arquivo]\nExemplo: exibir_arq teste.txt\n')
    print('12- sair: fecha o programa.\n')
    print('13- manual: exibe o manual.\n')


node1 = entra_node1()
node2 = entra_node2()

comando = 'continua'

while(comando != 'sair'):

    comando = 'continua'

    comando = input()
    argumentos = comando.split()

    if(argumentos[0] == 'listar'):
        listagem_arquivos()
    elif(argumentos[0] == 'listar_t'):
        listagem_filtrada()
    elif(argumentos[0] == 'copiar'):
        criar_copia()
    elif(argumentos[0] == 'criar_arq'):
        criar_arquivo()
    elif(argumentos[0] == 'mover'):
        mover()
    elif(argumentos[0] == 'renomear'):
        renomear()
    elif(argumentos[0] == 'remover_arq'):
        remover_arquivo()
    elif(argumentos[0] == 'criar_dir'):
        criar_diretorio()
    elif(argumentos[0] == 'remover_dir'):
        remover_diretorio()
    elif(argumentos[0] == 'inserir_arq'):
        inserir_arq()
    elif(argumentos[0] == 'exibir_arq'):
        exibir_arq()
    elif(argumentos[0] == 'manual'):
        manual()
    elif(argumentos[0] == 'limpar'):
        os.system('clear')
    elif(argumentos[0] == 'sair'):
        comando = 'sair'
    else:
        print('Esse comando não existe.')


fecha_ssh(node1)
fecha_ssh(node2)

# interface-beowulf

A interface se deu através da criação de um programa em python que se conecta através de um ssh em outras máquinas virtuais, sendo capaz de receber comandos amigáveis para um usuário sem muito conhecimento e, a partir deles, rodar comandos nas máquinas virtuais conectadas (node1 e node2).
Dessa forma, a interface permite uma abstração em relação à ideia de máquinas virtuais e permite a utilização de uma pasta compartilhada, local onde os arquivos e diretórios serão lidos e utilizados por todas as VMs de forma igual. Nesse caso específico foram apenas duas VMs, mas, da forma como o código foi feito, é plenamente possível expandir para mais, necessitando apenas de modificações simples.

<b>Funcionalidades implementadas:</b> <br/>
-listagem, <br/>-listagem extendida, <br/>-criação de arquivos e diretórios, <br/>-movimentação de arquivos e diretórios, <br/>-cópia de arquivos e diretórios, <br/>-renomeação de arquivos e diretórios, <br/>-inserção de texto em arquivo <br/>-exibição de conteúdo de arquivo.

<b>Bibliotecas utilizadas no Python:</b> <br/>
os<br/>
paramiko

<b>Instruções para rodar o programa</b></br>
Para rodar o programa basta ter o python3 instalado no Linux (Ubuntu), além das bibliotecas mencionadas acima, entrar no diretório e digitar <b>'python3 interface.py'</b>. A partir daí o programa começará a funcionar e para ter acesso ao manual dos comandos só precisa digitar 'manual' e apertar 'ENTER'. A partir daí, é só executar os comandos pré-definidos de forma correta (como está no manual) e as instruções vão gerar comportamentos nas VMs (node1 e node2), de forma compartilhada. Lembrando que o nome da pasta em que haverá esse compartilhamento é 'compartilhada/'.</br>

<b>Manual dos comandos</b></br>
1- listar: Lista os arquivos e diretórios presentes naquele diretório.</br>
Formato esperado: listar [endereço do diretório]</br>
Caso o argumento seja vazio, listará a pasta ~compartilhada~, que está na home.</br>
Exemplo: listar compartilhada/pasta</br>
</br>
2- listar_t: Lista os arquivos e diretórios ordenando pelos modificados recentemente primeiro.</br>
Formato esperado: listar_t [endereço do diretório]</br>
Caso o argumento seja vazio, listará a pasta ~compartilhada~, que está na home.</br>
Exemplo: listar_t compartilhada/pasta</br>
</br>
3- copiar: Faz uma cópia do arquivo ou pasta selecionado.</br>
Formato esperado: copiar [endereço de origem com o nome do arquivo] [endereço de destino com o nome do arquivo]</br>
Exemplo: copiar compartilhada/teste.txt compartilhada/copia.txt</br>
</br>
4- criar_arq: Cria um arquivo no diretório selecionado.</br>
Formato esperado: criar_arq [endereço com o nome do arquivo]</br>
Exemplo: criar_arq compartilhada/pasta/teste.txt</br>
</br>
5- mover: Move um arquivo ou diretório de um lugar para o outro.</br>
Formato esperado: mover [endereço de origem com o nome do arquivo] [endereço de destino com o nome do arquivo]</br>
Exemplo: mover compartilhada/teste.txt compartilhada/pasta/movido.txt</br>
</br>
6- renomear: Renomeia arquivo ou diretório.</br>
Formato esperado: renomear [endereço com o nome atual do arquivo] [endereço com o futuro nome do arquivo]</br>
Exemplo: renomear compartilhada/teste.txt compartilhada/novonome.txt</br>
</br>
7- remover_arq: Remove um arquivo do diretório.</br>
Formato esperado: remover_arq [endereço com o nome do arquivo]</br>
Exemplo: remover_arq compartilhada/teste.txt</br>
</br>
8- criar_dir: Cria uma pasta/diretório.</br>
Formato esperado: criar_dir [endereço com o nome da nova pasta]</br>
Exemplo: criar_dir compartilhada/pasta/novapasta</br>
</br>
9- remover_dir: Remove um diretório e apaga os arquivos dentro dele.</br>
Formato esperado: remover_dir [endereço com o nome da pasta]</br>
Exemplo: remover_dir compartilhada/pasta/exemplo</br>
</br>
10- inserir_arq: Insere algum texto dentro de um arquivo.</br>
Formato esperado: inserir_arq [texto que deseja inserir] [endereço com o nome do arquivo]</br>
Exemplo: inserir_arq exemplo teste.txt</br>
</br>
11- exibir_arq: Exibe o conteúdo do arquivo.</br>
Formato esperado: exibir_arq [endereço com o nome do arquivo]</br>
Exemplo: exibir_arq teste.txt</br>
</br>
12- sair: fecha o programa.</br>
</br>
13- manual: exibe o manual.</br>
</br>


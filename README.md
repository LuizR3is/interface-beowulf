# interface-beowulf

A interface se deu através da criação de um programa em python que se conecta através de um ssh em outras máquinas virtuais, sendo capaz de receber comandos amigáveis para um usuário sem muito conhecimento e, a partir deles, rodar comandos nas máquinas virtuais conectadas (node1 e node2).
Dessa forma, a interface permite uma abstração em relação à ideia de máquinas virtuais e permite a utilização de uma pasta compartilhada, local onde os arquivos e diretórios serão lidos e utilizados por todas as VMs de forma igual. Nesse caso específico foram apenas duas VMs, mas, da forma como o código foi feito, é plenamente possível expandir para mais, necessitando apenas de modificações simples.

Funcionalidades implementadas: <br/>
-listagem, <br/>-listagem extendida, <br/>-criação de arquivos e diretórios, <br/>-movimentação de arquivos e diretórios, <br/>-cópia de arquivos e diretórios, <br/>-renomeação de arquivos e diretórios, <br/>-inserção de texto em arquivo <br/>-exibição de conteúdo de arquivo.

Bibliotecas utilizadas no Python: <br/>
os<br/>
paramiko

mensagem = """                                                                                       História dos Sistemas Operacionais


                                              					              INTRODUÇÃO

Sistemas operacionais são ligados intimamente ligados à arquitetura dos computadores que são executados. 
O primeiro computador digital foi projetado pelo matemático inglês Charles Babbage. Dedicou sua vida à construir uma máquina analítica, nunca a fez perfeitamente, pois na tecnologia de sua época não havia os aparatos necessários para tal feito.
Ao decorrer de suas tentativas percebeu que precisaria de um “software” para sua máquina, e assim contratou Ada Lovelace, a primeira    programadora do mundo.

                                                                                          Primeira Geração (1945-1955)
				                           Válvulas e Painéis

Em méados da década de 40 um grupo de estudiosos obtiveram sucesso na construção de máquinas de calcular. Eram mecânicas e         válvulas faziam todo o trabalho, eram enormes e lentas.
A programação era feita baseada em ligações de fios e pelo manuseio de válvulas. Posteriormente na década de 50, cartões perfurados    eram utilizados para escrever programas.

				                Segunda Geração (1955-1965)
				              Transistores e sistemas de lote

Essa geração foi revolucionária pela introdução dos usos de transistores, o que reduziu consideravelmente o tamanho de um computado, além de torná-los mais eficientes e confiáveis. Nessa geração também foi desenvolvido o sistema de lotes, o que permitia um computador executar múltiplas tarefas em sequência.

				                Terceira Geração (1965-1980)
					    CIs e multiprogramação

Os circuitos integrados foram uma nova criação que diminuiu ainda mais o tamanho dos computadores, além de aumentarem a sua           eficiência.
Nessa geração foram desenvolvidos vários novos sistemas e funcionalidades que facilitavam  o uso de um computador:
* Multiprogramação
* Tempo compartilhado
* Spooling

					           Quarta Geração 
					   Computadores pessoais

Os sistemas operacionais da quarta geração foram marcados por serem fáceis de usar e serem acessíveis, foram desenvolvidos para     funcionar em diversos tipos de hardwares.
Essa geração também é marcada pela popularização de computadores pessoais, que podem ser usados em casa, foram projetados para 
suportar interfaces gráficas, e oferecer recursos avançado.
As interfaces gráficas de usuário são sistemas implementados na quarta geração que permite usuários comuns interajam com o 
computador usando ícones, janelas e menus em vez de digitar comandos em um prompt.
As inteterfaces gráficas (GUI) tornou os computadores mais acessíveis à usuários e permitiu a criação de aplicativos gráficos mais avançados.

Fontes:
* Sistemas Operacionais: projeto e implementação - Tanenbaum e Albert S. Woodhull

"""

mensagem_funcionamento = """			                               Funcionamento do Sistema Operacional
						
						Introdução

O funcionamento de um sistema operacional e dividido entre módulos, que desempenham suas funções para o funcionamento de um        computador.

					                       Kernel
					
O kernel, também chamado de núcleo, é responsável pelo gerenciamento de memória, de processos, subsistemas de arquivos, gerenciamento de rede, suporte aos dispositivos de Entrada e Saida.
É o elo que faz a ligação entre o hardware e os softwares de um computador, componente central de todo o sistema operacional.

				                  Gerenciamento de Processos

Para o Sistema Operacional executar um processo, é necessário o sistema de descritor de processos, também conhecido como bloco de controle de processo (PCB). o PCB permite o monitoramento e controle da execução de um processo.

					Gerenciamento de Memória

Os sistemas de gerenciamento de memória são divididos entre 2 grupos: os que fazem troca de processos entre a memória principal e de disco, e os que não fazem.
Monoprogramação sem Troca ou Paginação: nesse sistema de gerenciamento, um único processo e executado por vez utilizando toda a  memória disponível o sistema operacional carrega um programa do disco para a memória principal e o executa. depois aguarda o usuário 
para um novo programa ser executado.
Multiprogramação: técnica de processamento onde um computador executa simultaneamente múltiplos processos, fazendo com que a    CPU seja utilizada em 100% do tempo diminuindo o tempo ocioso.
 
                                                                                          					Gerenciamento de Arquivos
 
O móduclo de gerenciamento de arquivos tem várias funções, segurança para um usuário não acessar o arquivo de outro usuário,                compartilhamento de arquivos entre usuários e pela rede, é a parte mais visível do SO pois o usuário está sempre utilizando arquivos.

São utilizados três métodos diferentes para acessar dados de arquivos:

- Acesso sequencial
- Acesso direto
- Acesso indexado

Fontes:
* Sistemas Operacionais - Ramiro Córdova
"""

mensagem_hardware = """					    Hardware e Software

					            O Hardware

O hardware é tudo aquilo que podemos tocar, é composta pela parte tangível do computador.
São exemplos:

* Processador
* Disco
* Placa mãe

					            O Software

É tudo aquilo que é intangível no computador, ele é armazenado no hardware e executado pelo processador. e seus dados normalmente     são mantidos na memória.

				           Relações entre Hardware e Software

John von Neumann propõe que os computadores devem ter uma unidade central de processamento (CPU), composta por uma unidade 
aritmética e uma unidade de controle de registradores, além disso prevê a existência de uma memória principal (RAM) e dispositivos de 
entrada e saída, isso é conhecido como arquitetura de Von Neumann.
Um computador é formado por esses componentes físicos além dos programas e sistema operacional. 

Temos como princípio da equivalência que todas as operações realizadas por um software pode ser diretamente realizada por um 
hardware e vice-versa. Máquinas virtuais e emuladores são exemplos de softwares que simulam o funcionamento de um hardware.
Porém o contrário e menos intuitivo. Um hardware pode ter o funcionamento de um software para buscar mais perfomance por exemplo, 
fazendo com que a execução do hardware seja em tempo real.

					Componentes do Hardware

Um computador criado a partir da arquitetura de Von Neumann terá: pelo menos um processador, memória RAM e algum dispositivo de 
entrada e saida.

				                                Processador

A função do processador e interpretar as instruções de um programa e executá-las. Para isso, o processador possui três principais 
componentes:
A unidade lógico-aritmética, que efetua cálculos e operações de lógica; a unidade de controle, que garante o fluxo dos dados e operações dentro do processador e os registradores, que são pequenas memórias, exrtremamente rápidas, dentro do processador

					         Memória Principal

A memória RAM e comumente associada à memória principal.
Ela deve ser muito rápida para não perder ciclos de processamento, cumpre a função de armazenar dados e instruções dos programas
que estão sendo executados.
Memória cache é uma memória ainda mais rápida que são localizadas próximas ou dentro do processador.
A memória principal é volátil, não guarda informação caso o computador seja desligado.

					       Memória Secundária

Tem a função de armazenar informação de maneira durável, para ser lida em um momento posterior, essas memórias são mais lentas 
que a memória principal.

				                Dispositivos de entrada e saida

São a maneira com que o usuário interage com o computador:

* Monitor
* Teclado
* Mouse
* Placas de rede

					        Tipos de Software

1. Sistema Operacional (SO): software que controla o hardware e fornece serviços para os programas de aplicação.

2. Programas de Aplicação: programas escritos para realizar tarefas específicas, como processamento de texto, edição de imagens, 
planilhas eletrônicas, jogos, entre outros.

3. Utilitários: programas que realizam tarefas de manutenção, gerenciamento e diagnóstico do sistema, como backup, desfragmentação, verificação de vírus, etc.

4. Compiladores: programas que traduzem código fonte de uma linguagem de programação para código de máquina executável.

5. Interpretadores: programas que leem e executam o código fonte de uma linguagem de programação diretamente, sem a necessidade 
de compilação prévia.

6. Editores de Texto: programas que permitem a criação e edição de arquivos de texto simples.




"""
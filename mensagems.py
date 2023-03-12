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
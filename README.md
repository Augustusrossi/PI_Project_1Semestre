PROJETO INTEGRADOR 1 SEMESTRE-SISTEMA DE INFORMAÇÃO (SI)

// Descrição //

O presente projeto consiste no desenvolvimento de um sistema de gerenciamento de consultas e atendimentos médicos, elaborado como parte das atividades acadêmicas da disciplina de Projeto Integrador do curso de Sistemas de Informação.
A aplicação foi desenvolvida utilizando a linguagem Python integrada ao banco de dados MySQL, permitindo o cadastro, gerenciamento e consulta de informações relacionadas a pacientes, médicos e requerimentos de atendimento.
O sistema possibilita tanto a utilização de registros já existentes quanto a realização de novos cadastros, oferecendo uma estrutura funcional para o controle básico de um ambiente de pronto atendimento.
Além disso, o projeto busca organizar o fluxo de atendimentos médicos, auxiliando no gerenciamento de solicitações, acompanhamento de pacientes e controle das demandas registradas no sistema.


// Objetivo do projeto // 
O principal objetivo deste projeto é aplicar, na teoria e na prática, os conceitos fundamentais de desenvolvimento de software e banco de dados, promovendo a experiência em trabalho em equipe e na construção de sistemas integrados.

Durante o desenvolvimento do projeto, foram aplicados conceitos como:

Manipulação de banco de dados utilizando SQL;
Integração entre Python e MySQL;
Desenvolvimento de operações CRUD (Create, Read, Update e Delete);
Estruturação modular do sistema;
Organização e separação de responsabilidades no código entre os integrantes da equipe;
Controle básico de atendimentos médicos;
Gerenciamento de pacientes, médicos e seus respectivos requerimentos;
Simulação de um fluxo de atendimento em ambiente de pronto atendimento.

// Tecnologias Utilizadas // 

MySQL
FortClient VPN (utilizado para conexão com a rede da PUC-Campinas)
VS Code com desenvolvimento em Python
Git e GitHub para versionamento e gerenciamento do projeto

// Funcionalidades do Sistema // 

Funcionalidades principais:

Interface/Front gráfica; (em processo de decisão) 
Cadastro de pacientes; ok
Cadastro de médicos; ok
Busca de pacientes; ok 
Busca de médicos; ok
Gerenciamento de requerimentos; ok
Controle de atendimentos; ok
Alteração de status das solicitações; (em processo)
Integração com banco de dados MySQL; ok 
Operações básicas de CRUD. ok
Estatísticas visuais para analise; (em processo)

// Estrutura do Projeto python // 

PI_Project_1Semestre/
│
├── __pycache__/              # Arquivos compilados automaticamente pelo Python
│
├── Index.py            # Estrutura base das operações
│
├── README.md                 # Documentação principal do projeto
│
├── chamadaBanco.py           # Responsável pela conexão e comunicação com o banco de dados
│
├── imports.py                # Centralização das bibliotecas e importações utilizadas
│
├── medicos.py                # Funcionalidades relacionadas ao gerenciamento de médicos
│
├── paciente.py               # Funcionalidades relacionadas ao gerenciamento de pacientes
│
├── requerimentos.py          # Controle e gerenciamento dos requerimentos de atendimento
│
└── teste.py                  # Arquivo utilizado para testes e validações do sistema


// Execução do Projeto //

Observação:
Durante o desenvolvimento do projeto, algumas funcionalidades foram desenvolvidas separadamente pelos integrantes da equipe. Após a finalização de cada estrutura e módulo, os arquivos foram encaminhados ao integrante Augustus, responsável pela integração dos códigos, organização da estrutura final do sistema e execução completa da aplicação.

Pré-requisitos
Antes de iniciar a execução do projeto, é necessário possuir os seguintes softwares instalados na máquina:

Python
MySQL
VS Code
Git
FortClient VPN

Etapa 1.0 — Conexão com a VPN da PUC-Campinas
Abrir o FortClient VPN;
Realizar a conexão com a rede da PUC-Campinas utilizando as credenciais fornecidas pela matéria BD;
Após a conexão, verificar o acesso ao banco de dados MySQL disponibilizado pela universidade.

Essa etapa é necessária para permitir a comunicação entre a aplicação Python e o banco de dados hospedado na rede da instituição.

Etapa 2.0 — Clonagem e Acesso ao Projeto
Clonar o repositório utilizando o Git e a URL disponibilizada:
git clone 
Acessar a pasta do projeto:
cd PI_Project_1Semestre

Caso o projeto esteja sendo iniciado manualmente, é possível criar a pasta e adicionar os arquivos diretamente no diretório desejado.

Abrir o projeto no VS Code:
code .

Etapa 3.0 — Configuração da Conexão com o Banco de Dados
Configurar a conexão entre o Python e o banco de dados MySQL utilizando as credenciais fornecidas pela universidade.
Exemplo de configuração:

host = "localhost"
user = "usuario"
password = "senha"
database = "nome_do_banco"

As informações devem ser inseridas no arquivo responsável pela comunicação com o banco de dados do sistema.

Etapa 4.0 — Execução do Sistema

Após todas as configurações concluídas, executar os arquivos principais do sistema pelo terminal Python ou pelo terminal integrado do VS Code.

Exemplo:

py medicos.py

ou

python medicos.py

A execução poderá variar de acordo com o módulo ou funcionalidade que se deseja testar dentro do sistema




// Resultados Esperados // 

Cadastro de pacientes; ok
Cadastro de médicos; ok 
Gerenciamento de requerimentos de atendimento; ok
Consulta de informações registradas; ok 
Atualização e remoção de dados; 
Controle básico do fluxo de atendimentos médicos; ok
Organização das solicitações e status de atendimento; (em processo)
Integração entre Python e banco de dados MySQL. ok


// Observações Preliminares //

O desenvolvimento do projeto foi realizado utilizando práticas colaborativas inspiradas na metodologia ágil Scrum, com divisão de responsabilidades entre os integrantes da equipe e desenvolvimento modular das funcionalidades.

Cada integrante ficou responsável por partes específicas do sistema, realizando o desenvolvimento individual dos módulos. Após a finalização das estruturas, os arquivos foram integrados em uma única aplicação, permitindo a organização e execução completa do sistema.

A metodologia adotada contribuiu para:

Melhor organização do projeto;
Separação de responsabilidades;
Desenvolvimento simultâneo de funcionalidades;
Facilidade na manutenção do código;
Integração colaborativa entre os membros da equipe

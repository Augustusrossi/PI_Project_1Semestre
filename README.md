# PI_Project_1Semestre
---

## Descrição do projeto:
O presente projeto consiste no desenvolvimento de um sistema de gerenciamento de consultas e atendimentos médicos, elaborado como parte das atividades acadêmicas da disciplina de Projeto Integrador do curso de Sistemas de Informação.
A aplicação foi desenvolvida utilizando Python integrado ao banco de dados MySQL, permitindo o cadastro, gerenciamento e consulta de informações relacionadas a pacientes, médicos e requerimentos de atendimento.
O sistema possibilita tanto a utilização de registros já existentes quanto a realização de novos cadastros, oferecendo uma estrutura funcional para o controle básico de um ambiente de pronto atendimento.


## Objetivo do Projeto
O principal objetivo deste projeto é aplicar, na teoria e na prática, os conceitos fundamentais de desenvolvimento de software e banco de dados, promovendo a experiência em trabalho em equipe e na construção de sistemas integrados.

### Conceitos aplicados no projeto
- Manipulação de banco de dados utilizando SQL
- Integração entre Python e MySQL
-	Desenvolvimento de operações CRUD (Create, Read, Update e Delete)
-	Estruturação modular do sistema
-	Organização e separação de responsabilidades no código entre os integrantes da equipe


## Integrantes da Equipe
| Nome Completo | RA |
| :--- | ---: |
| Augustus Klingbeil Rossi | 26001089 |
| Diego dos Santos Duque | 26005557 |
| Gabriel Almeida Fransiozi | 26006944 |
| Kauan Silva Cabrera | 26007624 |
| Matheus Neves | 22019901 |




## Tecnologias e Versões Utilizadas

| Tecnologia | Versão | Finalidade |
| :--- | :---: | ---: |
| Python | 3.14.5 | Linguagem principal do backend |
| MySQL | 8.0.20 | Banco de dados relacional |
| mysql-connector-python | 9.7.0 | Driver de conexão Python <-> MySQL |
| Git | 2.54.0 | Controle de versão |
| GitHub | Uso online | Hospedagem do repositório e gestão do projeto |
| Trello | Uso online | Gestão de tarefas e sprints da equipe |
| FortiClient VPN | 7.4 | Acesso à rede interna da PUC-Campinas |
| VS Code | 1.122.1 | IDE principal de desenvolvimento |

### Instalação das dependências Python
```
# Instalar todas as dependências de uma vez
pip install mysql-connector-python matplotlib
```


## Como Execuar o Projeto

### Pré-requisitos
- Python Instalado - [dowload](https://www.python.org/downloads/)
- MySQL Server instalado
- FortiClient VPN configurado e conectado à rede PUC-Campinas
- Git instalado para clonar o repositório
- IDE (da preferência) para inicialização do código

### Passo a Passo

#### 1. Conectar à VPN
É necessário entrar na VPN da PUCCAMPINAS-SP com as seguintes credenciais:
**user:** 26001089
**password:** Doti_100

#### 2. Clonar o projeto da branch main
```
git clone https://github.com/Augustusrossi/PI_Project_1Semestre.git
```

#### 3. Inicializar o projeto na IDE desejada
```
python index.py
```

## Fluxos de Funcionamento do Sistema

### Fluxos de Execução
```text
Index.py  (entrada principal)
   │
   ├──► imports.py         (carregado primeiro — disponibiliza acesso aos outros módulos)
   │
   ├──► chamadaBanco.py    (abre conexão MySQL; reutilizada por todos os módulos)
   │         │
   ├──► paciente.py  ──────┤  lê/escreve tabela `pacientes`
   ├──► medicos.py   ──────┤  lê/escreve tabela `medicos`
   └──► requerimentos.py ──┘  lê/escreve tabela `requerimentos`
                               vincula paciente ↔ médico ↔ status
```


### Fluxo Hipotético do uso do Sistema
1. Paciente chega ao pronto atendimento
2. Operador/caixa de atendimento e usa a função de cadastrar paciente ou buscar um paciente caso já exista
3. Uma solicitação é cadastrada com base na queixa do paciente levando em conta os campos, dor, desconforto e tempo dos sintomas
4. Um médico é associado à uma solicitação o que significa que o paciente está em atendimento, portanto o status está como "Andamento"
5. Após a consulta o status passa para "finalizado"
6. Além disso a central de atendimento tem acesso a funções genéricas como listagem geral de pacientes, médicos e requerimentos, visualizações específicas ou gerais como no caso das estatísticas.


## Regras de Prioridade das Solicitações
Foi elaborado uma média ponderada onde cada campo no cadastro de solicitações tem um peso específico:
- Dor
- Desconforto
- Tempo

### Cálculo:
RESULTADO = ( (dor X 5) + (desconforto X 2) + (tempo X 3) ) / 10

### Prioridade: 
- **Sem Urgência:** resultado < 5;
- **Urgente:** resultado >=5 && resultado < 8
- **Crítico:** resultado >= 8

## Gerenciamento do projeto
O Trello foi utilizado como ferramenta de gestão das tarefas do projeto. As colunas do quadro seguiram a estrutura:
-	Backlog — funcionalidades planejadas ainda não iniciadas
-	Em andamento — tarefas sendo desenvolvidas no sprint atual
-	Em revisão — pull requests abertos aguardando code review
-	Concluído — tarefas finalizadas e mescladas na branch principal

##Estrutura do Projeto
```
PI_Project_1Semestre/
│
├── __pycache__/          # Arquivos compilados automaticamente pelo Python
│
├── Index.py              # Ponto de entrada; inicializa GUI e menu principal
│
├── README.md             # Documentação principal do projeto
│
├── chamadaBanco.py       # Conexão e comunicação com o banco de dados MySQL
│
├── imports.py            # Centralização de bibliotecas e importações
│
├── medicos.py            # CRUD e gerenciamento de médicos
│
├── paciente.py           # CRUD e gerenciamento de pacientes
│
├── requerimentos.py      # Controle de requerimentos e status de atendimento
│
└── teste.py              # Testes e validações do sistema

```

## Funcionalidade do Sistema
-	Interface gráfica com Tkinter
-	Cadastro de pacientes e médicos
-	Busca e edição de registros existentes
-	Gerenciamento de requerimentos de atendimento
-	Controle e atualização de status das solicitações
-	Classificação de atendimentos por prioridade (Protocolo de Manchester)
-	Integração completa com banco de dados MySQL
-	Operações CRUD (Create, Read, Update, Delete)
-	Estatísticas visuais geradas com Matplotlib

# PROJETO INTEGRADOR 1º SEMESTRE - SISTEMA DE INFORMAÇÃO (SI)

## Descrição

O presente projeto consiste no desenvolvimento de um sistema de gerenciamento de consultas e atendimentos médicos, elaborado como parte das atividades acadêmicas da disciplina de Projeto Integrador do curso de Sistemas de Informação.

A aplicação foi desenvolvida utilizando a linguagem Python integrada ao banco de dados MySQL, permitindo o cadastro, gerenciamento e consulta de informações relacionadas a pacientes, médicos e requerimentos de atendimento.

O sistema possibilita tanto a utilização de registros já existentes quanto a realização de novos cadastros, oferecendo uma estrutura funcional para o controle básico de um ambiente de pronto atendimento.

Além disso, o projeto busca organizar o fluxo de atendimentos médicos, auxiliando no gerenciamento de solicitações, acompanhamento de pacientes e controle das demandas registradas no sistema.

---

# Objetivo do Projeto

O principal objetivo deste projeto é aplicar, na teoria e na prática, os conceitos fundamentais de desenvolvimento de software e banco de dados, promovendo a experiência em trabalho em equipe e na construção de sistemas integrados.

Durante o desenvolvimento do projeto, foram aplicados conceitos como:

- Manipulação de banco de dados utilizando SQL;
- Integração entre Python e MySQL;
- Desenvolvimento de operações CRUD (Create, Read, Update e Delete);
- Estruturação modular do sistema;
- Organização e separação de responsabilidades no código entre os integrantes da equipe;
- Controle básico de atendimentos médicos;
- Gerenciamento de pacientes, médicos e seus respectivos requerimentos;
- Simulação de um fluxo de atendimento em ambiente de pronto atendimento.

---

# Tecnologias Utilizadas

- MySQL
- FortClient VPN (utilizado para conexão com a rede da PUC-Campinas)
- VS Code com desenvolvimento em Python
- Git e GitHub para versionamento e gerenciamento do projeto

---

# Funcionalidades do Sistema

## Funcionalidades principais

- Interface/Front gráfica; *(em processo de decisão)*
- Cadastro de pacientes; **ok**
- Cadastro de médicos; **ok**
- Busca de pacientes; **ok**
- Busca de médicos; **ok**
- Gerenciamento de requerimentos; **ok**
- Controle de atendimentos; **ok**
- Alteração de status das solicitações; *(em processo)*
- Integração com banco de dados MySQL; **ok**
- Operações básicas de CRUD; **ok**
- Estatísticas visuais para análise; *(em processo)*

---

# Estrutura do Projeto Python

```bash
PI_Project_1Semestre/
│
├── __pycache__/              # Arquivos compilados automaticamente pelo Python
│
├── Index.py                  # Estrutura base das operações
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

CREATE TABLE paciente (
    id_paciente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(120) NOT NULL,
    rg VARCHAR(20),
    telefone VARCHAR(20),
    data_cadastro DATETIME
);

CREATE TABLE medico (
    id_medico INT AUTO_INCREMENT PRIMARY KEY,
    crm VARCHAR(20) NOT NULL,
    nome VARCHAR(75) NOT NULL,
    email VARCHAR(100),
    funcao VARCHAR(50)
);

CREATE TABLE requerimentos (
    id_requerimento INT AUTO_INCREMENT PRIMARY KEY,
    id_medico INT NOT NULL,
    id_paciente INT NOT NULL,
    descricao VARCHAR(200),
    data_hora_abertura DATETIME,
    data_hora_fechamento DATETIME,
    status VARCHAR(50),
    prioridade VARCHAR(10),

    CONSTRAINT fk_requerimento_medico
        FOREIGN KEY (id_medico)
        REFERENCES medico(id_medico),

    CONSTRAINT fk_requerimento_paciente
        FOREIGN KEY (id_paciente)
        REFERENCES paciente(id_paciente)
);
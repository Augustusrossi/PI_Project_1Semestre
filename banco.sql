CREATE TABLE medico (
    crm INT PRIMARY KEY,
    nome VARCHAR(75),
    email VARCHAR(100),
    funcao VARCHAR(50)
);

CREATE TABLE Paciente (
    id_paciente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(120) NOT NULL,
    rg VARCHAR(20),
    descricao VARCHAR(200),
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE requerimentos (
    id_requerimento INT AUTO_INCREMENT PRIMARY KEY,
    id_medico INT,
    id_paciente INT,
    descricao VARCHAR(200),
    data_hora_abertura DATETIME NOT NULL,
    data_hora_fechamento DATETIME,
    estagio VARCHAR(50),
    prioridade VARCHAR(50),

    FOREIGN KEY (id_medico) REFERENCES medico(crm),
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente)
);


INSERT INTO medico VALUES
(101, 'Dr João', 'joao@email.com', 'Cardiologista'),
(102, 'Dra Ana', 'ana@email.com', 'Clínica Geral');

INSERT INTO Paciente (nome, rg, descricao) VALUES
('Matheus', '123456', 'Dor de cabeça'),
('Carlos', '789101', 'Febre');

INSERT INTO requerimentos 
(id_medico, id_paciente, descricao, data_hora_abertura, estagio, prioridade)
VALUES
(101, 1, 'Consulta urgente', NOW(), 'Aberto', 'Alta'),
(102, 2, 'Retorno', NOW(), 'Em andamento', 'Média');

SELECT * FROM Pacientes;
SELECT * FROM medico;
SELECT * FROM requerimentos;

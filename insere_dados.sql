INSERT INTO `db_partiu`.`estado` (`nome`) VALUES
('Acre'),
('Alagoas'),
('Amapá'),
('Amazonas'),
('Bahia'),
('Ceará'),
('Distrito Federal'),
('Espírito Santo'),
('Goiás'),
('Maranhão'),
('Mato Grosso'),
('Mato Grosso do Sul'),
('Minas Gerais'),
('Pará'),
('Paraíba'),
('Paraná'),
('Pernambuco'),
('Piauí'),
('Rio de Janeiro'),
('Rio Grande do Norte'),
('Rio Grande do Sul'),
('Rondônia'),
('Roraima'),
('Santa Catarina'),
('São Paulo'),
('Sergipe'),
('Tocantins');

INSERT INTO cidade (nome, populacao, descricao, estado_codEstado) VALUES
('Rio de Janeiro', 6748000, 'A capital do estado do Rio de Janeiro, famosa por suas praias e o Cristo Redentor.', 1),
('Maceió', 12330000, 'Maceió, é a capital do estado de Alagoas, na costa leste do Brasil.', 2),
('Florianópolis ', 2886698, 'Florianópolis, a capital do estado de Santa Catarina no sul do Brasil, é maioritariamente constituída pela Ilha de Santa Catarina, com 54 km de comprimento.', 24);

INSERT INTO hotel (nome, numQuartos, categoria, rua, bairro, cep, cidade_codCidade) VALUES
('Hotel Majestic Palace', 259, 5, 'Av. Jornalista Rubens de Arruda Ramos, 2746', 'Centro', '88015702', 3),
('Hotel Copacabana Palace', 239, 5, 'Av. Atlântica, 1702', 'Copacabana', '22021001', 1),
('Hotel Unique', 94, 5, 'Av. Brigadeiro Luís Antônio, 4700', 'Jardim Paulista', '01402002', 2),
('Hotel Fasano', 60, 5, 'Rua Vieira Souto, 80', 'Ipanema', '22420000', 1);

INSERT INTO pacote 
(nome, preco, dataInicio, dataFim, descricao, cidade_codCidade, hotel_codHotel)  
VALUES 
('Pacote Florianópolis Verão', 1500.00, '2024-12-20', '2025-01-05', 'Pacote de férias em Florianópolis com estadia no Hotel Majestic Palace.', 3, 4),

('Pacote Rio De Janeiro Carnaval', 1200.00, '2024-02-20', '2024-02-25', 'Pacote de Carnaval em Rio de Janeino.', 1 , 1),

('Pacote Maceio Réveillon', 2000.00, '2024-12-28', '2025-01-02', 'Pacote de Réveillon em Maceio.', 2 , 2);


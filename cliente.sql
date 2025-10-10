-- Criação do banco
CREATE DATABASE IF NOT EXISTS `cliente`
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_0900_ai_ci; -- se seu MySQL não tiver essa collation, use utf8mb4_general_ci
USE `cliente`;

-- Criação da tabela (derivada do INSERT fornecido)
CREATE TABLE IF NOT EXISTS `dadoscliente` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(150) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `telefone` VARCHAR(20) NOT NULL,
  `dt` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_email` (`email`)            -- índice simples (se quiser tornar único, troque por UNIQUE)
) ENGINE=InnoDB;

-- População (mantendo os IDs informados)
INSERT INTO `dadoscliente` (`id`, `nome`, `email`, `telefone`, `dt`) VALUES
(1, 'Brunno Henrique Vilas Boas', 'brunnohenrique50@gmail.com', '(62) 99999-9999', '2022-07-04 22:33:43'),
(3, 'Jose Santos Silva', 'teste@gmail.com', '(62) 99888-8888', '2022-07-04 22:38:12'),
(4, 'Matheusaa', 'testematheus@gmail.com', '(62) 99777-7777', '2022-07-04 22:39:41'),
(5, 'Jorge', 'jorgeteste@gmail.com', '(62) 99333-3333', '2022-07-04 22:55:31');

CREATE USER 'crud'@'%' IDENTIFIED BY '9kjThhnVcXJP';
GRANT ALL PRIVILEGES ON cliente.* TO 'crud'@'%';
FLUSH PRIVILEGES;
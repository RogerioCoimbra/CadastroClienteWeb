# CadastroClienteWeb
Aplicação web PHP para cadastro de clientes em um banco de dados MySql.

git clone git@github.com:RogerioCoimbra/CadastroClienteWeb.git
docker pull php:8.4.10-alpine
docker pull mysql:oraclelinux9
docker build -t cadastro-cliente-web .

docker run --rm --name CadastroClienteWeb -p 8080:8080 -v "E:\Projetos\CadastroClienteWeb:/app" -w /app cadastro-cliente-web php -S 0.0.0.0:8080 -t /app
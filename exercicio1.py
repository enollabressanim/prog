import sqlite3

# criar uma "conexão" com o banco de dados
conexao = sqlite3.connect("cadastro.db")

# criar um curso para manipulação dos dados e tabelas
cursor = conexao.cursor()

# criar a tabela de cliente
cursor.execute("create table if not exists cliente \
        (id integer primary key,\
        nome text not null,\
        CPF varchar(11) not null unique,\
        RG varchar(7) not null unique,\
        telefone varchar(10),\
        celular varchar(11) not null unique,\
        email not null unique,\
        rua text,\
        numero text,\
        bairro text,\
        cidade text,\
        estado text,\
        CEP varchar(8) not null) ")

print('Tabela criada com sucesso.')

# fechar a conexão
conexao.close()
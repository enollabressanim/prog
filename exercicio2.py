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

# inserir vários dados
cursor.execute('INSERT into cliente values (1, "cliente 1", "111.111.111-11", '\
    ' "1.111.111", "1111-1111", "11111-1111", "cliente1@tabela.com", "rua 1", '\
    ' "1", "dos clientes", "cidade 1", "CC", "11111-000")')
cursor.execute('INSERT into cliente values (2, "cliente 2", "222.222.222-22", '\
    ' "2.222.222", "2222-2222", "22222-2222", "cliente2@tabela.com", "rua 2", '\
    ' "2", "dos clientes", "cidade 2", "CC", "22222-000")')
cursor.execute('INSERT into cliente values (3, "cliente 3", "333.333.333-33", '\
    ' "3.333.333", "3333-3333", "33333-3333", "cliente3@tabela.com", "rua 3", '\
    ' "3", "dos clientes", "cidade 3", "CC", "33333-000")')
cursor.execute('INSERT into cliente values (4, "cliente 4", "444.444.444-44", '\
    ' "4.444.444", "4444-4444", "44444-4444", "cliente4@tabela.com", "rua 4", '\
    ' "4", "dos clientes", "cidade 4", "CC", "44444-000")')
cursor.execute('INSERT into cliente values (5, "cliente 5", "555.555.555-55", '\
    ' "5.555.555", "5555-5555", "55555-5555", "cliente5@tabela.com", "rua 5", '\
    ' "5", "dos clientes", "cidade 5", "CC", "55555-000")')
cursor.execute('INSERT into cliente values (6, "cliente 6", "666.666.666-66", '\
    ' "6.666.666", "6666-6666", "66666-6666", "cliente6@tabela.com", "rua 6", '\
    ' "6", "dos clientes", "cidade 6", "CC", "66666-000")')
cursor.execute('INSERT into cliente values (7, "cliente 7", "777.777.777-77", '\
    ' "7.777.777", "7777-7777", "77777-7777", "cliente7@tabela.com", "rua 7", '\
    ' "7", "dos clientes", "cidade 7", "CC", "77777-000")')
cursor.execute('INSERT into cliente values (8, "cliente 8", "888.888.888-88", '\
    ' "8.888.888", "8888-8888", "88888-8888", "cliente8@tabela.com", "rua 8", '\
    ' "8", "dos clientes", "cidade 8", "CC", "88888-000")')
cursor.execute('INSERT into cliente values (9, "cliente 9", "999.999.999-99", '\
    ' "9.999.999", "9999-9999", "99999-9999", "cliente9@tabela.com", "rua 9", '\
    ' "9", "dos clientes", "cidade 9", "CC", "99999-000")')
cursor.execute('INSERT into cliente values (10, "cliente 10", "101.010.101-01", '\
    ' "1.010.101", "1010-1010", "01010-1010", "cliente10@tabela.com", "rua 10", '\
    ' "10", "dos clientes", "cidade 10", "CC", "10101-000")')

# executa comando select para recuperar as informações
for linha in cursor.execute("select * from cliente"):
    print(linha)

# confirmar a operação
conexao.commit()

# fechar a conexão
conexao.close()

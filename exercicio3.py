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
cursor.execute('INSERT or IGNORE into cliente values (1, "cliente 1", "111.111.111-11", '\
    ' "1.111.111", "1111-1111", "11111-1111", "cliente1@tabela.com", "rua 1", '\
    ' "1", "dos clientes", "cidade 1", "CC", "11111-000")')
cursor.execute('INSERT or IGNORE into cliente values (2, "cliente 2", "222.222.222-22", '\
    ' "2.222.222", "2222-2222", "22222-2222", "cliente2@tabela.com", "rua 2", '\
    ' "2", "dos clientes", "cidade 2", "CC", "22222-000")')
cursor.execute('INSERT or IGNORE into cliente values (3, "cliente 3", "111.111.111-11", '\
    ' "3.333.333", "3333-3333", "33333-3333", "cliente3@tabela.com", "rua 3", '\
    ' "3", "dos clientes", "cidade 3", "CC", "33333-000")')

# executa comando select para recuperar as informações
for linha in cursor.execute("select * from cliente"):
    print(linha)

# confirmar a operação
conexao.commit()

# fechar a conexão
conexao.close()

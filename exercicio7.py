import sqlite3

# criar uma "conexão" com o banco de dados
conexao = sqlite3.connect('cadastro.db')

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

# solicitando os dados ao usuário
cliente = []
for i in range(1,11):
    cliente.append( ("cliente" + str(i), "CPF" + str(i),"RG" + str(i), 
    "telefone" + str(i), "celular" + str(i), "email" + str(i), "rua" + str(i),
    "numero" + str(i), "bairro" + str(i), "cidade" + str(i), "estado" + str(i), 
    "CEP" + str(i)) )

print("valores a serem inseridos: " + str(cliente))

# inserindo dados na tabela
cursor.executemany('insert into cliente (id, nome, CPF, RG, telefone, celular, '\
    'email, rua, numero, bairro, cidade, estado, CEP) '\
    'values (null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', cliente)

print('Dados inseridos com sucesso.')
for linha in cursor.execute("select * from cliente"):
    print(linha)

# confirmar a operação
conexao.commit()

# fechar a conexão
conexao.close()
 
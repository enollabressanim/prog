import sqlite3

# criar uma "conexão" com o banco de dados
conexao = sqlite3.connect('cadastro.db')

# criar um curso para manipulação dos dados e tabelas
cursor = conexao.cursor()

for lista in conexao.execute("select * from cliente order by email asc"):
    print(f"ORDEM DOS E-MAILS: {lista[6]}")

# confirmar a operação
conexao.commit()

# fechar a conexão
conexao.close()
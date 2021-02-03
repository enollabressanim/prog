import sqlite3

# criar uma "conexão" com o banco de dados
conexao = sqlite3.connect("cadastro.db")

# criar um curso para manipulação dos dados e tabelas
cursor = conexao.cursor()

for linha in cursor.execute("select * from cliente"):
    print(linha)

# fechar a conexão
conexao.close()
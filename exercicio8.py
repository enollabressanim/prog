import sqlite3

# criar uma "conexão" com o banco de dados
conexao = sqlite3.connect('cadastro.db')

# criar um curso para manipulação dos dados e tabelas
cursor = conexao.cursor()

for linha in cursor.execute("DELETE FROM cliente"):
    print(linha)
    
# confirmar a operação
conexao.commit()

# fechar a conexão
conexao.close()
 
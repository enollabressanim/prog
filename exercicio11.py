import sqlite3

# criar uma "conexão" com o banco de dados
conexao = sqlite3.connect('cadastro.db')

# criar um curso para manipulação dos dados e tabelas
cursor = conexao.cursor()

# deleta as linhas da tabela "cliente"
cursor.execute("DELETE from cliente")

# confirmar a operação
conexao.commit()

# fechar a conexão
conexao.close()

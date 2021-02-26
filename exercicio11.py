import sqlite3
# O exercício 11 pede para que que faça a exclusão de todas as linhas da tabela.
# A instrução DELETE é utilizada para fazer a exclusão de algo na linguagem SQL.
# Neste caso ela está sendo usada para deletar todas as linhas da tabela cliente.

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

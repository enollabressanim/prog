import sqlite3

# O exercício 6 pede para listar todas as linhas e colunas armazenadas 
# no banco de dados ordenadas por alguma coluna de escolha particular,
# sendo ordenadas na ordem reversa da ordem utilizada no exercício anterior.
# Para que isso aconteça, é selecionado todos os dados da tabela cliente
# e assim sendo ordenada pelo e-mail na ordem descrescente.

# criar uma "conexão" com o banco de dados
conexao = sqlite3.connect('cadastro.db')

# criar um curso para manipulação dos dados e tabelas
cursor = conexao.cursor()

#listar linhas de coluna em ordem decrescente
for lista in conexao.execute("select * from cliente order by email desc"):
    print(f"ORDEM DOS E-MAILS: {lista[6]}")

# confirmar a operação
conexao.commit()

# fechar a conexão
conexao.close()

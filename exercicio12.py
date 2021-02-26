import sqlite3

# O exercício 12 pede para que faça a exclusão de uma linha específica da tabela.
# A instrução DELETE é utilizada para fazer a exclusão de algo na linguagem SQL.
# Neste caso ela está sendo usada para deletar apenas uma linha específica da tabela cliente.
# Para que aja a exclusão de apenas uma determinada linha, é necessário o uso do where, 
# que tem como finalidade especificar que uma instrução da linguagem de manipulação de dados SQL 
# deve afetar apenas as linhas que atendem aos critérios especificados, no caso, nesta situação, 
# mudando apenas a coluna nome, que tem como valor Cliente 7.

# criar uma "conexão" com o banco de dados
conexao = sqlite3.connect('cadastro.db')

# criar um curso para manipulação dos dados e tabelas
cursor = conexao.cursor()

# deleta a linha que possui o nome "cliente 7"
cursor.execute("DELETE from cliente WHERE nome = 'cliente 7'")

# executa comando select para recuperar as informações da tabela
for linha in cursor.execute("select * from cliente"):
    print(linha)

# confirmar a operação
conexao.commit()

# fechar a conexão
conexao.close()

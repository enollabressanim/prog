import sqlite3

# O exercício 12 pede para que  faça a exclusão de uma linha específica da tabela.
# Para que isso ocorra, é utilizado o UPDATE, atualizando os dados da tabela cliente, 
# selecionando a coluna celular, para que a mesma seja atualizada.
# Para que aja a atualização de apenas determinadas linhas, é necessario o uso do where, 
# que tem como finalidade modificar apenas a linha que possui um valor já determinado, 
# no caso, nesta situação, mudando apenas a coluna nome, que tem como valor Cliente 7.

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

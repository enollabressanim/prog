import sqlite3

# O exercício 9 pede para que seja atualizado todas as linhas de uma coluna da tabela.
# Para que isso ocorra, é utilizado o UPDATE, atualizando os dados da tabela cliente, 
# onde irá selecionar a coluna estado, mudando todas as suas linhas para SC


# criar uma "conexão" com o banco de dados
conexao = sqlite3.connect('cadastro.db')

# criar um curso para manipulação dos dados e tabelas
cursor = conexao.cursor()

# altera todos os valores da coluna estado para "SC"
cursor.execute("UPDATE cliente SET estado = 'SC'")

# executar comando select para recuperar as informações da tabela
for linha in cursor.execute("select * from cliente"):
    print(linha)
    
# confirmar a operação
conexao.commit()

# fechar a conexão
conexao.close()
 

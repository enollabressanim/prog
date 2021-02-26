import sqlite3

# O exercício 13 pede para que altere a tabela adicionando uma nova coluna.
# A instrução ALTER TABLE é utilizada para fazer alguma modificação na tabela.
# Neste caso, esta sendo usado o ADD COLUMN para adicionar uma nova coluna, 
# sendo deminominada como idade.

# criar uma "conexão" com o banco de dados
conexao = sqlite3.connect('cadastro.db')

# criar um curso para manipulação dos dados e tabelas
cursor = conexao.cursor()

# adiciona uma nova coluna na tabela "cliente"
cursor.execute('ALTER TABLE cliente ADD COLUMN idade TEXT;')

# executa comando select para recuperar as informações da tabela
for linha in cursor.execute("select * from cliente"):
    print(linha)

# confirmar a operação
conexao.commit()

# fechar a conexão
conexao.close()
 


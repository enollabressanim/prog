import sqlite3

# criar uma "conexão" com o banco de dados
conexao = sqlite3.connect('cadastro.db')

# criar um curso para manipulação dos dados e tabelas
cursor = conexao.cursor()

# altera os dados da coluna celular que são iguais a variavel "filtro"
filtro = '22222-2222'
cursor.execute("UPDATE cliente SET celular = '92323-9987' WHERE celular like ?", (filtro + "%",))

# executar comando select para recuperar as informações da tabela
for linha in cursor.execute("select * from cliente"):
    print(linha)

# confirmar a operação
conexao.commit()

# fechar a conexão
conexao.close()

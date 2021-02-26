import sqlite3

# O exercício 10 pede para que seja atualizado determinadas linhas de uma coluna da tabela.
# Para que isso ocorra, é utilizado o UPDATE, atualizando os dados da tabela cliente, 
# selecionando a coluna celular, para que a mesma seja atualizada.
# Para que aja a atualização de apenas determinadas linhas, é necessario o uso do where, 
# que tem como finalidade especificar que uma instrução da linguagem de manipulação de 
# dados SQL deve afetar apenas as linhas que atendem aos critérios especificados, 
# nesta situação, mudando apenas a coluna celular que possui o valor 22222-2222.
# Usando o operador LIKE combinado com o caracter especial porcentagem (%),
# há a indicação da posição que o conteúdo está sendo procurado no valor string do campo especificado.

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

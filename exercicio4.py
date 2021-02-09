import sqlite3

# criar uma "conexão" com o banco de dados
conexao = sqlite3.connect('cadastro.db')

# criar um curso para manipulação dos dados e tabelas
cursor = conexao.cursor()


for lista in conexao.execute("select * from cliente"):
    print(f"id: {lista[0]}, nome: {lista[1]}, CPF: {lista[2]}, RG: {lista[3]}, \
telefone: {lista[4]}, celular: {lista[5]}, email: {lista[6]}, rua: {lista[7]}, \
numero: {lista[8]}, bairro: {lista[8]}, cidade: {lista[8]}, estado: {lista[8]}, \
CEP: {lista[8]}")


# confirmar a operação
conexao.commit()

# fechar a conexão
conexao.close()
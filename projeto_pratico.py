import sqlite3

class BancoDados():
    def criar_tabelas(self):
        # criar uma "conexão" com o banco de dados
        conexao = sqlite3.connect('sistema.db')
        # criar um curso para manipulação dos dados e tabelas
        cursor = conexao.cursor()

        # criar a tabela de clientes
        cursor.execute("""create table if not exists clientes (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                CPF VARCHAR(11) NOT NULL UNIQUE,
                RG VARCHAR(7) NOT NULL UNIQUE,
                telefone VARCHAR(10),
                celular VARCHAR(11) NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                rua TEXT,
                numero TEXT,
                bairro TEXT,
                cidade TEXT,
                estado TEXT,
                CEP VARCHAR(8) NOT NULL);""")

        # criar a tabela de produtos
        cursor.execute("""create table if not exists produtos (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                produto VARCHAR(50) NOT NULL,
                codigo VARCHAR(50) NOT NULL UNIQUE,
                valor TEXT NOT NULL,
                quant TEXT);""")

        # fechar a conexão
        conexao.close()
    
    def bd_pedidos(self):
        # criar uma "conexão" com o banco de dados
        con = sqlite3.connect('encomendas.db')
        # criar um curso para manipulação dos dados e tabelas
        cursor = con.cursor()

        # criar a tabela de pedidos
        cursor.execute("""create table if not exists pedidos (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                cliente VARCHAR(50) NOT NULL,
                produto VARCHAR(50) NOT NULL,
                quant TEXT NOT NULL);""")

        # fechar a conexão
        con.close()

class acoes():
    # definir o estado padrão dos objetos.
    def __init__(self, p_nome = str, p_CPF = str, p_RG = str, p_telefone = str, p_celular = str, 
    p_email = str, p_rua = str, p_numero = str, p_bairro = str, p_cidade = str, p_estado = str, 
    p_CEP = str, p_produto = str, p_codigo = str, p_valor = str, p_quant = str):
        self.bd = BancoDados()
        self.p_nome = p_nome, 
        self.p_CPF = p_CPF, 
        self.p_RG = p_RG, 
        self.p_telefone = p_telefone, 
        self.p_celular = p_celular, 
        self.p_email = p_email, 
        self.p_rua = p_rua, 
        self.p_numero = p_numero, 
        self.p_bairro = p_bairro, 
        self.p_cidade = p_cidade, 
        self.p_estado = p_estado, 
        self.p_CEP = p_CEP,
        self.p_produto = p_produto, 
        self.p_codigo = p_codigo, 
        self.p_valor = p_valor, 
        self.p_quant = p_quant

    def inserir_clientes(self, p_nome = str, p_CPF = str, p_RG = str, p_telefone = str, p_celular = str, 
    p_email = str, p_rua = str, p_numero = str, p_bairro = str, p_cidade = str, p_estado = str, p_CEP = str):
        self.bd.criar_tabelas()
        # criar uma "conexão" com o banco de dados
        conexao = sqlite3.connect('sistema.db')
        # criar um curso para manipulação dos dados e tabelas
        cursor = conexao.cursor()

        # inserir dados
        cursor.execute("""
        INSERT INTO clientes (id, nome, CPF, RG, telefone, celular, email, \
        rua, numero, bairro, cidade, estado, CEP)
        VALUES (null,?,?,?,?,?,?,?,?,?,?,?,?)""", (p_nome, p_CPF, p_RG, p_telefone, 
        p_celular, p_email, p_rua, p_numero, p_bairro, p_cidade, p_estado, p_CEP))
        
        print('Dados inseridos com sucesso.')
        
        # confirmar a operação
        conexao.commit()
        # fechar a conexão
        conexao.close()

    def inserir_produtos(self, p_produto = str, p_codigo = str, p_valor = str, p_quant = str):
        self.bd.criar_tabelas()
        # criar uma "conexão" com o banco de dados
        conexao = sqlite3.connect('sistema.db')
        # criar um curso para manipulação dos dados e tabelas
        cursor = conexao.cursor()

        # inserir dados
        cursor.execute("""INSERT INTO produtos (id, produto, codigo, valor, quant)
        VALUES (null,?,?,?,?)""", (p_produto, p_codigo, p_valor, p_quant))

        print('Dados inseridos com sucesso.')

        # confirmar a operação
        conexao.commit()
        # fechar a conexão
        conexao.close()

    def comprar(self, p_nome = str, p_produto = str, p_quant = str):
        self.bd.bd_pedidos()
        # criar uma "conexão" com o banco de dados
        conexao = sqlite3.connect('sistema.db')
        # criar um curso para manipulação dos dados e tabelas
        cursor = conexao.cursor()
        
        # Faz a busca do cliente no banco de dados com o nome especificado
        pessoa = cursor.execute('select * from clientes where nome = ?', 
        (p_nome ,)).fetchone()

        # Verifica se o cliente está cadastrado
        if pessoa is None:
            # O cliente não está cadastrado
            print("Cliente não cadastrado")
        else:
            # Se o cliente estiver cadastrado
            # Faz a busca do produto no banco de dados com o nome especificado
            produto = cursor.execute('select * from produtos where produto = ?', 
            (p_produto ,)).fetchone()

            # Verifica se o produto está cadastrado
            if produto is None:
                # O produto não está cadastrado
                print("Produto não cadastrado")
            else:
                # Se o produto estiver cadastrado
                # Cria uma "conexão" com o banco de dados
                con = sqlite3.connect('encomendas.db')

                # criar um curso para manipulação dos dados e tabelas
                cursor = con.cursor()

                # inserir dados
                cursor.execute("""INSERT INTO pedidos (id, cliente, produto, quant)
                VALUES (null,?,?,?)""", (p_nome, p_produto, p_quant))

                # criar uma "conexão" com o banco de dados
                conexao = sqlite3.connect('sistema.db')

                # criar um curso para manipulação dos dados e tabelas
                cursor = conexao.cursor()

                # Atualiza a quantidade do produto no estoque                
                for i in range(p_quant):
                    cursor.execute("UPDATE produtos SET quant = quant - 1 WHERE produto like ?", 
                    (p_produto + "%",))

                print('Dados inseridos com sucesso.')

                # confirmar a operação
                con.commit()
                # fechar a conexão
                con.close()

                # confirmar a operação
                conexao.commit()
                # fechar a conexão
                conexao.close()

    def buscar(self):
        # criar uma "conexão" com o banco de dados
        con = sqlite3.connect('encomendas.db')
        # criar um curso para manipulação dos dados e tabelas
        cursor = con.cursor()

        # Inserir o id do pedido que deseja buscar
        ID = input("Id do pedido: ")
        # Faz a busca do pedido no banco de dados com o id especificado
        pedido = cursor.execute('select * from pedidos where id = ?', 
        (ID ,)).fetchone()

        # Verifica se o pedido está cadastrado
        if pedido is None:
            # Pedido não está cadastrado
            print("Pedido não cadastrado")
        else: 
            # Se o pedido estiver cadastrado
            # Faz a busca do pedido no banco de dados com o id especificado
            for linha in cursor.execute("select * from pedidos WHERE id like ?" , (ID + "%",)):
                # Imprime a linha da tabela que possui o id especificado
                print(linha)

            # fechar a conexão
            con.close()

    def excluir(self):
        # criar uma "conexão" com o banco de dados
        con = sqlite3.connect('encomendas.db')
        # criar um curso para manipulação dos dados e tabelas
        cursor = con.cursor()

        # Inserir o id do pedido que deseja buscar
        ID = input("Id do pedido: ")

        # Deleta o pedido que possui o mesmo id que foi especificado
        cursor.execute("DELETE from pedidos WHERE id like ?" , (ID + "%",))
        print("Pedido excluído com sucesso")

        # confirmar a operação
        con.commit()
        # fechar a conexão
        con.close()
    
    def alterar(self):
        # criar uma "conexão" com o banco de dados
        con = sqlite3.connect('encomendas.db')

        # criar um curso para manipulação dos dados e tabelas
        cursor = con.cursor()

        # Inserir o id do pedido que deseja buscar
        ID = input('Id do pedido: ')
        # Faz a busca do pedido no banco de dados com o id especificado
        pedido = cursor.execute('select * from pedidos where id = ?', (ID, )).fetchone()

        # Verifica se o pedido está cadastrado
        if pedido is None:
            # Pedido não está cadastrado
            print('Pedido inexistente')
        else:
            # Imprime a linha da tabela de pedidos que possui o id especificado
            print(pedido)
            # Inserir dados atualizados do pedido
            p_nome = input('Nome: ')
            p_produto = input('Produto: ')
            p_quant = int(input('Quantidade: '))

            # criar uma tupla com os valores lidos
            update = (p_nome, p_produto, p_quant, ID)

            #Utuliza as informações da tupla para fazer o update da tabela
            cursor.execute('update pedidos set cliente = ?, produto = ?,\
            quant = ? where id = ?', update)
            print("Dados atualizados com sucesso")

        # confirmar a operação
        con.commit()
        # fechar a conexão
        con.close()

class Menu():
    def __init__(self):
        self.sistema = acoes()

    def imprimir_commandos(self):
        # Imprime as opções das ações que pode-se fazer no programa
        print(" ")
        print("1 - inserir novo cliente")
        print("2 - inserir novo produto")
        print("3 - pedidos")
        print("4 - busca de pedido")
        print("5 - remoção de pedido")
        print("6 - alteração de pedido")

    def main(self):
        self.imprimir_commandos()
        #inserir opção desejada
        opcao = int(input("Digite uma opção acima: "))

        while opcao in [1, 2, 3, 4, 5, 6]:
            if opcao == 1:
                # inserir as informações necessárias para o cadastro de cliente 
                p_nome = input('Nome: ')
                p_CPF = input('CPF: ')
                p_RG = input('RG: ')
                p_telefone = input('Telefone: ')
                p_celular = input('Celular: ')
                p_email = input('Email: ')
                p_rua = input('Rua: ')
                p_numero = input('Numero: ')
                p_bairro = input('Bairro: ')
                p_cidade = input('Cidade: ')
                p_estado = input('Estado: ')
                p_CEP = input('CEP: ')
                # chama o método a ser utilizado para cumprir a tarefa
                self.sistema.inserir_clientes(p_nome, p_CPF, p_RG, p_telefone, 
                p_celular, p_email, p_rua, p_numero, p_bairro, p_cidade, p_estado, p_CEP)

            elif opcao == 2:
                # inserir as informações necessárias para o cadastro de produto
                p_produto = input('Produto: ')
                p_codigo = input('Codigo: ')
                p_valor = input('Valor: ')
                p_quant = int(input('Quantidade: '))
                # chama o método a ser utilizado para cumprir a tarefa
                self.sistema.inserir_produtos(p_produto, p_codigo, p_valor, p_quant)

            elif opcao == 3:
                # inserir as informações necessárias para realizar o pedido
                p_nome = input('Nome: ')
                p_produto = input('Produto: ')
                p_quant = int(input('Quantidade: '))
                # chama o método a ser utilizado para cumprir a tarefa
                self.sistema.comprar(p_nome, p_produto, p_quant)
            
            elif opcao == 4:
                # chama o método a ser utilizado para cumprir a tarefa
                self.sistema.buscar()
            
            elif opcao == 5:
                # chama o método a ser utilizado para cumprir a tarefa
                self.sistema.excluir()

            elif opcao == 6:
                # chama o método a ser utilizado para cumprir a tarefa
                self.sistema.alterar()

            self.imprimir_commandos()
            #inserir opção desejada
            opcao = int(input("Digite uma opção acima: "))

if __name__ == "__main__":
    g = Menu()
    g.main()
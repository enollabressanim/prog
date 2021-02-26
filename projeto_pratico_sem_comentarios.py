import sqlite3

class BancoDados():
    def criar_tabelas(self):
        conexao = sqlite3.connect('sistema.db')
        cursor = conexao.cursor()

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

        cursor.execute("""create table if not exists produtos (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                produto VARCHAR(50) NOT NULL,
                codigo VARCHAR(50) NOT NULL UNIQUE,
                valor TEXT NOT NULL,
                quant TEXT);""")
        conexao.close()

    def bd_pedidos(self):
        con = sqlite3.connect('encomendas.db')
        cursor = con.cursor()

        cursor.execute("""create table if not exists pedidos (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                cliente VARCHAR(50) NOT NULL,
                produto VARCHAR(50) NOT NULL,
                quant TEXT NOT NULL);""")
        con.close()

class acoes():
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
        conexao = sqlite3.connect('sistema.db')
        cursor = conexao.cursor()

        cursor.execute("""
        INSERT INTO clientes (id, nome, CPF, RG, telefone, celular, email, \
        rua, numero, bairro, cidade, estado, CEP)
        VALUES (null,?,?,?,?,?,?,?,?,?,?,?,?)""", (p_nome, p_CPF, p_RG, p_telefone, 
        p_celular, p_email, p_rua, p_numero, p_bairro, p_cidade, p_estado, p_CEP))

        conexao.commit()
        print('Dados inseridos com sucesso.')
        conexao.close()

    def inserir_produtos(self, p_produto = str, p_codigo = str, p_valor = str, p_quant = str):
        self.bd.criar_tabelas()
        conexao = sqlite3.connect('sistema.db')
        cursor = conexao.cursor()

        cursor.execute("""INSERT INTO produtos (id, produto, codigo, valor, quant)
        VALUES (null,?,?,?,?)""", (p_produto, p_codigo, p_valor, p_quant))

        conexao.commit()
        print('Dados inseridos com sucesso.')
        conexao.close()

    def comprar(self, p_nome = str, p_produto = str, p_quant = str):
        self.bd.bd_pedidos()
        conexao = sqlite3.connect('sistema.db')
        cursor = conexao.cursor()

        pessoa = cursor.execute('select * from clientes where nome = ?', 
        (p_nome ,)).fetchone()
        if pessoa is None:
            print("Cliente não cadastrado")
        else:
            produto = cursor.execute('select * from produtos where produto = ?', 
            (p_produto ,)).fetchone()
            if produto is None:
                print("Produto não cadastrado")
            else: 
                con = sqlite3.connect('encomendas.db')
                cursor = con.cursor()
                cursor.execute("""INSERT INTO pedidos (id, cliente, produto, quant)
                VALUES (null,?,?,?)""", (p_nome, p_produto, p_quant))

                conexao = sqlite3.connect('sistema.db')
                cursor = conexao.cursor()

                for i in range(p_quant):
                    cursor.execute("UPDATE produtos SET quant = quant - 1 WHERE produto like ?", 
                    (p_produto + "%",))

                con.commit()
                print('Dados inseridos com sucesso.')
                con.close()

                conexao.commit()
                conexao.close()

    def buscar(self):
        con = sqlite3.connect('encomendas.db')
        cursor = con.cursor()
        ID = input("Id do pedido: ")
        for linha in cursor.execute("select * from pedidos WHERE id like ?" , (ID + "%",)):
            print(linha)
        con.commit()
        con.close()

    def excluir(self):
        con = sqlite3.connect('encomendas.db')
        cursor = con.cursor()
        ID = input("Id do pedido: ")
        cursor.execute("DELETE from pedidos WHERE id like ?" , (ID + "%",))
        print("Pedido excluído com sucesso")
        con.commit()
        con.close()

    def alterar(self):
        con = sqlite3.connect('encomendas.db')
        cursor = con.cursor()

        ID = input('Id do pedido: ')
        pedido = cursor.execute('select * from pedidos where id = ?', (ID, )).fetchone()

        if pedido is None:
            print('Pedido inexistente')
        else:
            print(pedido)
            p_nome = input('Nome: ')
            p_produto = input('Produto: ')
            p_quant = int(input('Quantidade: '))
            update = (p_nome, p_produto, p_quant, ID)
            cursor.execute('update pedidos set cliente = ?, produto = ?,\
            quant = ? where id = ?', update)
            print("Dados atualizados com sucesso")
        con.commit()
        con.close()

class Menu():
    def __init__(self):
        self.sistema = acoes()

    def imprimir_commandos(self):
        print(" ")
        print("1 - inserir novo cliente")
        print("2 - inserir novo produto")
        print("3 - pedidos")
        print("4 - busca de pedido")
        print("5 - remoção de pedido")
        print("6 - alteração de pedido")

    def main(self):
        self.imprimir_commandos()
        opcao = int(input("Digite uma opção acima: "))
        while opcao in [1, 2, 3, 4, 5, 6]:
            if opcao == 1:
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
                self.sistema.inserir_clientes(p_nome, p_CPF, p_RG, p_telefone, 
                p_celular, p_email, p_rua, p_numero, p_bairro, p_cidade, p_estado, p_CEP)

            elif opcao == 2:
                p_produto = input('Produto: ')
                p_codigo = input('Codigo: ')
                p_valor = input('Valor: ')
                p_quant = int(input('Quantidade: '))
                self.sistema.inserir_produtos(p_produto, p_codigo, p_valor, p_quant)

            elif opcao == 3:
                p_nome = input('Nome: ')
                p_produto = input('Produto: ')
                p_quant = int(input('Quantidade: '))
                self.sistema.comprar(p_nome, p_produto, p_quant)

            elif opcao == 4:
                self.sistema.buscar()

            elif opcao == 5:
                self.sistema.excluir()

            elif opcao == 6:
                self.sistema.alterar()

            self.imprimir_commandos()
            opcao = int(input("Digite uma opção acima: "))

if __name__ == "__main__":
    g = Menu()
    g.main() 
import dbConnect


class Clientes:

    def setClient(self, nome_cliente, cpf_cliente):
        try:
            conn = dbConnect.DbConnect.conn(self)
            cursor = conn.cursor()

            comando = f'INSERT INTO clientes (nome, cpf) VALUES ("{nome_cliente}", {cpf_cliente})'
            cursor.execute(comando)
            conn.commit()

            cursor.close()
            conn.close()
        except:
            print("Não foi possível salvar os dados do cliente.")

    def getClient(self, cpf_cliente):
        try:
            conn = dbConnect.DbConnect.conn(self)
            cursor = conn.cursor()

            comando = f'SELECT nome FROM clientes WHERE cpf="{cpf_cliente}"'
            cursor.execute(comando)
            res = cursor.fetchone()

            cursor.close()
            conn.close()

            return res
        except:
            print("Não foi possível recuperar os dados do cliente.")

    def updateClient(self, id_cliente, nome_cliente, cpf_cliente):
        try:
            conn = dbConnect.DbConnect.conn(self)
            cursor = conn.cursor()

            comando = f'UPDATE clientes SET nome="{nome_cliente}", cpf="{cpf_cliente}" WHERE id="{id_cliente}"'
            cursor.execute(comando)
            conn.commit()

            cursor.close()
            conn.close()
        except:
            print("Não foi possível atualizar os dados do cliente.")

    def deleteClient(self, id_cliente):
        try:
            conn = dbConnect.DbConnect.conn(self)
            cursor = conn.cursor()

            comando = f'DELETE clientes WHERE id="{id_cliente}"'
            cursor.execute(comando)
            conn.commit()

            cursor.close()
            conn.close()
        except:
            print("Não foi possível deletar os dados do cliente.")
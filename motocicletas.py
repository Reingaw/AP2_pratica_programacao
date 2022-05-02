import dbConnect


class Motocicletas:

    def setMoto(self, modelo, marca, preco):
        try:
            conn = dbConnect.DbConnect.conn(self)
            cursor = conn.cursor()

            comando = f'INSERT INTO motocicletas (modelo, marca, preco) VALUES ("{modelo}", "{marca}", {preco})'
            cursor.execute(comando)
            conn.commit()

            cursor.close()
            conn.close()
        except:
            print("Não foi possível salvar os dados da motocicleta.")

    def getMoto(self, modelo):
        try:
            conn = dbConnect.DbConnect.conn(self)
            cursor = conn.cursor()

            comando = f'SELECT nome FROM motocicletas WHERE modelo="{modelo}"'
            cursor.execute(comando)
            res = cursor.fetchone()

            cursor.close()
            conn.close()

            return res
        except:
            print("Não foi possível recuperar os dados da motocicleta.")

    def updateMoto(self, id_moto, modelo, marca, preco):
        try:
            conn = dbConnect.DbConnect.conn(self)
            cursor = conn.cursor()

            comando = f'UPDATE motocicletas SET modelo="{modelo}", ' \
                      f'marca="{marca}", preco="{preco}" WHERE id="{id_moto}"'
            cursor.execute(comando)
            conn.commit()

            cursor.close()
            conn.close()
        except:
            print("Não foi possível atualizar os dados da motocicleta.")

    def deleteMoto(self, id_moto):
        try:
            conn = dbConnect.DbConnect.conn(self)
            cursor = conn.cursor()

            comando = f'DELETE motocicletas WHERE id="{id_moto}"'
            cursor.execute(comando)
            conn.commit()

            cursor.close()
            conn.close()
        except:
            print("Não foi possível deletar os dados da motocicleta.")
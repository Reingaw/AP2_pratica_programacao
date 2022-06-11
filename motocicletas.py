import dbConnect


class Motocicletas:

    def setMoto(self, modelo, marca, preco):
        try:
            conn = dbConnect.DbConnect.conn(self)
            cursor = conn.cursor()

            comando = f'INSERT INTO motocicletas ' \
                      f'(modelo, marca, preco) VALUES' \
                      f'("{modelo}", "{marca}", {preco})'
            cursor.execute(comando)
            conn.commit()

            cursor.close()
            conn.close()
        except:
            print("Não foi possível salvar os dados da motocicleta.")

    def getMoto(self, id):
        try:
            conn = dbConnect.DbConnect.conn(self)
            cursor = conn.cursor()

            comando = f'SELECT modelo, marca, preco FROM motocicletas WHERE id={id}'
            cursor.execute(comando)
            res = cursor.fetchone()

            cursor.close()
            conn.close()

            return res
        except:
            print("Não foi possível recuperar os dados da motocicleta.")

    def getAllMotos(self):
        try:
            conn = dbConnect.DbConnect.conn(self)
            cursor = conn.cursor()

            comando = f'SELECT id, modelo, marca, preco FROM motocicletas'
            cursor.execute(comando)
            res = cursor.fetchall()

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

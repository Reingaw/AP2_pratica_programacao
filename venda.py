import dbConnect


class Venda:
    def setSale(self, id_cliente, total):
        try:
            conn = dbConnect.DbConnect.conn(self)
            cursor = conn.cursor()

            comando = f'INSERT INTO venda (id_cliente, total) VALUES ("{id_cliente}", "{total}")'
            cursor.execute(comando)
            conn.commit()

            id_venda = cursor.lastrowid

            cursor.close()
            conn.close()
        except:
            print("Não foi possível salvar os dados da venda.")

    def addToCart(self, cart, id_moto, marca, modelo, preco):
        try:
            new_moto = {
                "id": id_moto,
                "marca": marca,
                "modelo": modelo,
                "preco": preco
            }

            cart.push(new_moto)

            return cart
        except:
            print("Não foi possível adicionar os dados da moto ao carrinho.")

    def setSaleItems(self, id_venda, id_motocicletas):
        try:
            conn = dbConnect.DbConnect.conn(self)
            cursor = conn.cursor()

            comando = f'INSERT INTO venda_items (id_venda, id_motocicletas) ' \
                      f'VALUES ("{id_venda}", "{id_motocicletas}")'
            cursor.execute(comando)
            conn.commit()
        except:
            print("Não foi possível salvar os dados dos items do carrinho.")
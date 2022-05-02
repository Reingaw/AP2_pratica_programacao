import mysql.connector


class DbConnect:
    def conn(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                port='3307',
                user='zao',
                password='zao',
                database='ap2_database'
            )

            return connection
        except:
            print("Não foi possível conectar com o banco de dados.")
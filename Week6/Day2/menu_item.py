import psycopg2

def connect():
    return psycopg2.connect(
        dbname="restaurant",  # 数据库名
        user="postgres",      # 用户名
        password="941125",    # 改成你的
        host="localhost",
        port="5432"
    )

class Menu_Item():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        conn = connect()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)',(self.name,self.price))
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self):
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Menu_Items WHERE item_name = %s", (self.name,))
        conn.commit()
        cursor.close()
        conn.close()

    def update(self,new_name, new_price):
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s", (new_name, new_price, self.name))
        conn.commit()
        cursor.close()
        conn.close()
    
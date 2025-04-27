from menu_item import connect

class MenuManager:

    @classmethod
    def get_by_name(cls, name):
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Menu_Items WHERE item_name = %s", (name,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()

        if row:
            from menu_item import Menu_Item
            return Menu_Item(row[1], row[2])  # name, price
        return None

    @classmethod
    def all_items(cls):
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT item_name, item_price FROM Menu_Items")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

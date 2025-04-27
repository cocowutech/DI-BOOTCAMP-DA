from menu_item import Menu_Item
from menu_manager import MenuManager

def show_user_menu():
    while True:
        print("\n--- Restaurant Menu Manager ---")
        print("View an Item (V)")
        print("Add an Item (A)")
        print("Delete an Item (D)")
        print("Update an Item (U)")
        print("Show the Menu (S)")
        print("Exit (E)")

        choice = input("Enter your choice: ").strip().upper()

        if choice == 'V':
            view_item()
        elif choice == 'A':
            add_item_to_menu()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_from_menu()
        elif choice == 'S':
            show_restaurant_menu()
        elif choice == 'E':
            print("\nFinal Menu:")
            show_restaurant_menu()
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice, try again.")

def add_item_to_menu():
    name = input("Enter item name: ").strip()
    price = input("Enter item price: ").strip()

    try:
        item = Menu_Item(name, int(price))
        item.save()
        print("✅ Item added successfully.")
    except Exception as e:
        print(f"❌ Error adding item: {e}")

def remove_item_from_menu():
    name = input("Enter item name to delete: ").strip()

    try:
        item = Menu_Item(name, 0)  # price doesn't matter for deletion
        item.delete()
        print("✅ Item deleted successfully.")
    except Exception as e:
        print(f"❌ Error deleting item: {e}")

def update_item_from_menu():
    old_name = input("Current item name: ").strip()
    old_price = input("Current item price: ").strip()
    new_name = input("New item name: ").strip()
    new_price = input("New item price: ").strip()

    try:
        item = Menu_Item(old_name, int(old_price))
        item.update(new_name, int(new_price))
        print("✅ Item updated successfully.")
    except Exception as e:
        print(f"❌ Error updating item: {e}")

def view_item():
    name = input("Enter item name to view: ").strip()
    item = MenuManager.get_by_name(name)
    if item:
        print(f"🍽 {item.name} - ${item.price}")
    else:
        print("Item not found.")

def show_restaurant_menu():
    items = MenuManager.all_items()
    print("\n--- Current Menu ---")
    for name, price in items:
        print(f"{name} - ${price}")

# 🔥 程序入口点
if __name__ == "__main__":
    show_user_menu()

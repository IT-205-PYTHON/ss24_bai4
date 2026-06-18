def view_menu(menu_db):
    print("\n--- THỰC ĐƠN RIKKEI COFFEE ---")
    for i, item in enumerate(menu_db, 1):
        selling_price = item.calculate_selling_price()
        print(
            f"{i}. Mã: {item.item_id} | "
            f"Tên: {item.item_name:<18}| "
            f"Trạng thái: {item.get_status():<10}| "
            f"Giá niêm yết: {selling_price:,} VNĐ"
        )
    print()
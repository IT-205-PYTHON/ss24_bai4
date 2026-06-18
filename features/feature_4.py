def update_price(menu_db):
    print("\n--- ĐIỀU CHỈNH GIÁ GỐC CỦA MÓN ---")
    item_id = input("Nhập mã món cần đổi giá: ").strip().upper()

    for item in menu_db:
        if item.item_id == item_id:
            new_price = input("Nhập giá tiền mới: ").strip()
            item.base_price = new_price
            if str(new_price).lstrip("-").isdigit() and int(new_price) > 0:
                print("Cập nhật giá gốc thành công!")
            return

    print("Không tìm thấy món có mã này!")
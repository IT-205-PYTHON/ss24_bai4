def toggle_status(menu_db):
    print("\n--- CẬP NHẬT TRẠNG THÁI MÓN ---")
    item_id = input("Nhập mã món cần cập nhật: ").strip().upper()

    for item in menu_db:
        if item.item_id == item_id:
            item.toggle_availability()
            status = "ĐANG BÁN" if item.is_available else "HẾT HÀNG"
            print(f">> Đã cập nhật {item.item_name} thành {status}!")
            return

    print("Không tìm thấy món có mã này!")
from models.menu_item import MenuItem


def add_item(menu_db):
    print("\n--- THÊM MÓN MỚI VÀO MENU ---")
    item_id = input("Nhập mã món: ").strip()

    if not MenuItem.is_valid_item_id(item_id):
        print("Mã món không hợp lệ!")
        print("Mã món phải gồm 2 chữ cái in hoa và 2 chữ số. Ví dụ: CF01.")
        return

    for item in menu_db:
        if item.item_id == item_id:
            print("Mã món đã tồn tại trong hệ thống!")
            return

    item_name = input("Nhập tên món: ").strip().title()

    price_input = input("Nhập giá gốc: ").strip()

    if not price_input.isdigit() or int(price_input) <= 0:
        print("Giá đồ uống phải lớn hơn 0!")
        return

    new_item = MenuItem(item_id, item_name, int(price_input))
    menu_db.append(new_item)
    print("Thêm món mới thành công!")
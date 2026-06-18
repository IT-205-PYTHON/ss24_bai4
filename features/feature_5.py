from models.menu_item import MenuItem


def update_service_charge():
    print("\n--- CẬP NHẬT PHỤ PHÍ DỊCH VỤ TOÀN HỆ THỐNG ---")
    current = int(MenuItem.service_charge * 100)
    print(f"Phụ phí hiện tại: {current}%")

    rate_input = input("Nhập phụ phí mới. Ví dụ 0.1 tương ứng 10%: ").strip()

    valid = True
    for ch in rate_input:
        if ch not in "0123456789.":
            valid = False
            break

    if not valid or rate_input.count(".") > 1:
        print("Phụ phí không hợp lệ!")
        return

    new_rate = float(rate_input)

    if new_rate < 0:
        print("Phụ phí không được âm!")
        return

    MenuItem.update_service_charge(new_rate)
    print("Cập nhật phụ phí dịch vụ thành công!")
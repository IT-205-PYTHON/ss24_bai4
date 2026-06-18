"""
Class Design Document — MenuItem
Class Attribute:

service_charge = 0.0 — phụ phí dùng chung cho toàn bộ đối tượng

Instance Attributes:

item_id — public
item_name — public
__base_price — private (name mangling)
__is_available — private (name mangling), mặc định True

    Loại                            Tên                                         Mô tả

__init__                (self, item_id, item_name, price)           Khởi tạo, __is_available = True
@propertybase           _priceGetter                                cho __base_price
@base_price.setter      base_price                                  Kiểm tra > 0 trước khi gán
@property               is_available                                Getter cho __is_available
Instance Method         toggle_availability()                       Đảo __is_available
Instance Method         calculate_selling_price()                   __base_price * (1 + service_charge)
@classmethod            update_service_charge(cls, new_rate)        Cập nhật cls.service_charge
@staticmethod           is_valid_item_id(item_code)                 2 chữ hoa + 2 chữ số
"""

from models.menu_item import MenuItem
from features import view_menu, add_item, toggle_status, update_price, update_service_charge

menu_db = [
    MenuItem("CF01", "Cà Phê Đen", 30000),
    MenuItem("CF02", "Bạc Xỉu", 45000),
    MenuItem("TE01", "Trà Đào Cam Sả", 50000),
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE =====")
    print("1. Xem thực đơn & Giá niêm yết")
    print("2. Thêm món mới vào menu")
    print("3. Cập nhật trạng thái (Hết hàng/Còn hàng)")
    print("4. Điều chỉnh giá gốc của món")
    print("5. Cập nhật phụ phí dịch vụ toàn hệ thống")
    print("6. Thoát chương trình")
    print("======================================================")
    choice = input("Chọn chức năng (1-6): ").strip()

    match choice:
        case "1":
            view_menu(menu_db)
        case "2":
            add_item(menu_db)
        case "3":
            toggle_status(menu_db)
        case "4":
            update_price(menu_db)
        case "5":
            update_service_charge()
        case "6":
            print("Cảm ơn bạn đã sử dụng hệ thống Rikkei Coffee!")
            break
        case _:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 6!")
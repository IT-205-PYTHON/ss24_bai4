class MenuItem:
    service_charge = 0.0

    def __init__(self, item_id, item_name, price):
        self.item_id = item_id
        self.item_name = item_name
        self.__base_price = price
        self.__is_available = True

    @property
    def base_price(self):
        return self.__base_price

    @base_price.setter
    def base_price(self, new_price):
        if not str(new_price).lstrip("-").isdigit() or int(new_price) <= 0:
            print("Giá đồ uống phải lớn hơn 0!")
            print("Giá cũ được giữ nguyên.")
            return
        self.__base_price = int(new_price)

    @property
    def is_available(self):
        return self.__is_available

    def toggle_availability(self):
        self.__is_available = not self.__is_available

    def get_status(self):
        return "Đang bán" if self.__is_available else "Hết hàng"

    def calculate_selling_price(self):
        return int(self.__base_price * (1 + MenuItem.service_charge))

    @classmethod
    def update_service_charge(cls, new_rate):
        cls.service_charge = new_rate

    @staticmethod
    def is_valid_item_id(item_code):
        if len(item_code) != 4:
            return False
        return item_code[:2].isupper() and item_code[:2].isalpha() and item_code[2:].isdigit()
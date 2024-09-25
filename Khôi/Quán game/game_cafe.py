from pc import PC
from user import User

class GameCafe:
    def __init__(self):
        self.pcs = []  # Danh sách các máy tính
        self.users = []  # Danh sách người dùng
        self.services = []  # Các dịch vụ mà quán game cung cấp

    def add_pc(self, pc: PC):
        self.pcs.append(pc)
        print(f"Đã thêm PC {pc.pc_id} loại {pc.pc_type} vào quán.")

    def add_user(self, user: User):
        self.users.append(user)
        print(f"Đã thêm người dùng {user.name} vào quán.")

    def add_service(self, service_name, price):
        self.services.append({"service": service_name, "price": price})
        print(f"Dịch vụ {service_name} đã được thêm với giá {price} VND.")

    def show_services(self):
        if not self.services:
            print("Hiện tại không có dịch vụ nào.")
        else:
            print("Danh sách dịch vụ:")
            for service in self.services:
                print(f"Dịch vụ: {service['service']}, Giá: {service['price']} VND")

    def show_available_pcs(self):
        available_pcs = [pc for pc in self.pcs if not pc.is_in_use]
        if available_pcs:
            print("Danh sách PC trống:")
            for pc in available_pcs:
                print(f"PC {pc.pc_id} loại {pc.pc_type}")
        else:
            print("Không có PC trống.")

    def show_user_history(self, user: User):
        print(f"Lịch sử sử dụng của {user.name}:")
        for record in user.usage_history:
            print(record)

    def report(self):
        print("Báo cáo quán game:")
        print(f"Tổng số máy tính: {len(self.pcs)}")
        print(f"Số máy đang sử dụng: {len([pc for pc in self.pcs if pc.is_in_use])}")
        print(f"Tổng số người dùng: {len(self.users)}")
        self.show_services()

from game_cafe import GameCafe
from user import User

class Manager:
    def __init__(self, cafe: GameCafe):
        self.cafe = cafe

    def add_user(self):
        try:
            user_id = int(input("Nhập ID cho người dùng: "))
            name = input("Nhập tên người dùng: ")
            user = User(user_id, name)
            self.cafe.add_user(user)
            print(f"Người dùng {name} đã được thêm với ID {user_id}.")
        except ValueError:
            print("Vui lòng nhập số hợp lệ cho ID.")

    def add_service(self):
        try:
            service_name = input("Nhập tên dịch vụ: ")
            price = float(input("Nhập giá dịch vụ: "))
            self.cafe.add_service(service_name, price)
        except ValueError:
            print("Vui lòng nhập giá hợp lệ.")

    def show_report(self):
        self.cafe.report()

    def show_user_history(self):
        try:
            user_id = int(input("Nhập ID người dùng: "))
            user = self.find_user_by_id(user_id)
            if user:
                self.cafe.show_user_history(user)
            else:
                print(f"Không tìm thấy người dùng với ID {user_id}.")
        except ValueError:
            print("Vui lòng nhập số hợp lệ cho ID.")

    def find_user_by_id(self, user_id):
        for user in self.cafe.users:
            if user.user_id == user_id:
                return user
        return None

    def menu(self):
        while True:
            print("\n--- HỆ THỐNG QUẢN LÝ ---")
            print("1. Thêm người dùng")
            print("2. Thêm dịch vụ")
            print("3. Hiển thị báo cáo")
            print("4. Hiển thị lịch sử người dùng")
            print("5. Thoát")
            choice = input("Vui lòng chọn một tùy chọn: ")

            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.add_service()
            elif choice == '3':
                self.show_report()
            elif choice == '4':
                self.show_user_history()
            elif choice == '5':
                print("Thoát hệ thống.")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

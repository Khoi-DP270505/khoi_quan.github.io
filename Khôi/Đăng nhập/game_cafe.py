from user import User
from pc import PC

class GameCafe:
    def __init__(self):
        self.pcs = []
        self.users = []
        self.services = {"Coffee": 20000, "Snack": 15000}

    def add_pc(self, pc: PC):
        self.pcs.append(pc)
    
    def add_user(self, user: User):
        self.users.append(user)

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def get_user_by_username(self, username):
        # Hàm này sẽ trả về đối tượng User nếu tìm thấy tên đăng nhập
        for user in self.users:
            if user.username == username:
                return user
        return None

    def generate_next_user_id(self):
        if not self.users:
            return 1
        max_id = max(int(user.user_id) for user in self.users)
        return max_id + 1

    def show_services(self):
        print("Dịch vụ có sẵn:")
        for service, price in self.services.items():
            print(f"{service}: {price} VND")
    
    def use_service(self, user_id, service_name):
        user = self.get_user_by_id(user_id)
        if user:
            if service_name in self.services:
                cost = self.services[service_name]
                if user.use_service(service_name, cost):
                    print(f"{user.username} đã sử dụng {service_name}")
                    return True
                else:
                    print(f"{user.username} không đủ tiền để sử dụng {service_name}.")
            else:
                print("Dịch vụ không tồn tại.")
        return False

    def load_data_from_csv(self, users_file, pcs_file):
        self.users = User.load_users_from_csv(users_file)
        self.pcs = PC.load_pcs_from_csv(pcs_file)

    def save_data_to_csv(self, users_file, pcs_file):
        User.save_users_to_csv(users_file, self.users)
        PC.save_pcs_to_csv(pcs_file, self.pcs)

import csv

class User:
    def __init__(self, user_id, username, password, balance=0, is_admin=False):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.balance = balance
        self.is_admin = is_admin
        self.current_pc = None
        self.usage_history = []

    @staticmethod
    def load_users_from_csv(file_path):
        users = []
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:  # Sử dụng mã hóa UTF-8
                reader = csv.DictReader(file)
                for row in reader:
                    user = User(row["user_id"], row["username"], row["password"], float(row["balance"]), row["is_admin"] == 'True')
                    users.append(user)
        except FileNotFoundError:
            print(f"File {file_path} không tồn tại.")
        except UnicodeDecodeError as e:
            print(f"Lỗi giải mã Unicode: {e}")
        return users

    @staticmethod
    def save_users_to_csv(file_path, users):
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:  # Sử dụng mã hóa UTF-8
            writer = csv.DictWriter(file, fieldnames=["user_id", "username", "password", "balance", "is_admin"])
            writer.writeheader()
            for user in users:
                writer.writerow({"user_id": user.user_id, "username": user.username, "password": user.password, "balance": user.balance, "is_admin": user.is_admin})

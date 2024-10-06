import csv

class PC:
    def __init__(self, pc_id, pc_type, is_in_use=False):
        self.pc_id = pc_id
        self.pc_type = pc_type
        self.is_in_use = is_in_use
        self.current_session_start = None

    def start_session(self, start_time):
        self.is_in_use = True
        self.current_session_start = start_time

    def end_session(self, end_time):
        self.is_in_use = False
        if self.current_session_start:
            duration = end_time - self.current_session_start
            self.current_session_start = None
            return duration
        return None

    @staticmethod
    def load_pcs_from_csv(file_path):
        pcs = []
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:  # Sử dụng mã hóa UTF-8
                reader = csv.DictReader(file)
                for row in reader:
                    pc = PC(row["pc_id"], row["pc_type"], row["is_in_use"] == 'True')
                    pcs.append(pc)
        except FileNotFoundError:
            print(f"File {file_path} không tồn tại.")
        except UnicodeDecodeError as e:
            print(f"Lỗi giải mã Unicode: {e}")
        return pcs

    @staticmethod
    def save_pcs_to_csv(file_path, pcs):
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:  # Sử dụng mã hóa UTF-8
            writer = csv.DictWriter(file, fieldnames=["pc_id", "pc_type", "is_in_use"])
            writer.writeheader()
            for pc in pcs:
                writer.writerow({"pc_id": pc.pc_id, "pc_type": pc.pc_type, "is_in_use": pc.is_in_use})

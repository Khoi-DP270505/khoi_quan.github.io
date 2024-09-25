class PC:
    def __init__(self, pc_id, pc_type):
        """
        Khởi tạo một máy tính mới.
        pc_id: ID của máy tính
        pc_type: Loại máy tính (thường 'normal' hoặc 'VIP')
        """
        self.pc_id = pc_id
        self.pc_type = pc_type  # 'normal' hoặc 'VIP'
        self.is_in_use = False  # Trạng thái của máy tính (đang sử dụng hay không)
        self.start_time = None  # Thời gian bắt đầu phiên chơi

    def start_session(self, start_time):
        """
        Bắt đầu phiên chơi trên máy tính.
        start_time: Thời gian bắt đầu phiên chơi
        """
        if self.is_in_use:
            print(f"PC {self.pc_id} đang được sử dụng.")
            return False  # Không thể bắt đầu phiên mới nếu đang sử dụng
        self.is_in_use = True
        self.start_time = start_time
        print(f"Phiên chơi trên PC {self.pc_id} bắt đầu lúc {start_time}.")
        return True

    def end_session(self, end_time):
        """
        Kết thúc phiên chơi.
        end_time: Thời gian kết thúc phiên chơi
        Trả về thời gian chơi (giờ).
        """
        if not self.is_in_use:
            print(f"PC {self.pc_id} không được sử dụng.")
            return None
        self.is_in_use = False
        duration = end_time - self.start_time  # Tính thời gian đã sử dụng
        self.start_time = None
        print(f"Phiên chơi trên PC {self.pc_id} kết thúc sau {duration} giờ.")
        return duration

from pc import PC

class User:
    def __init__(self, user_id, name):
        """
        Khởi tạo người dùng mới.
        user_id: ID của người dùng
        name: Tên người dùng
        """
        self.user_id = user_id
        self.name = name
        self.usage_history = []  # Lịch sử sử dụng máy tính

    def start_use(self, pc: PC, start_time):
        """
        Người dùng bắt đầu phiên chơi trên một máy tính.
        pc: Máy tính đang sử dụng
        start_time: Thời gian bắt đầu sử dụng
        """
        if pc.start_session(start_time):
            self.usage_history.append(f"{self.name} bắt đầu sử dụng PC {pc.pc_id} lúc {start_time}")

    def end_use(self, pc: PC, end_time, rate_per_hour):
        """
        Người dùng kết thúc phiên chơi và thanh toán phí.
        pc: Máy tính đang sử dụng
        end_time: Thời gian kết thúc phiên chơi
        rate_per_hour: Mức giá mỗi giờ
        """
        duration = pc.end_session(end_time)
        if duration is not None:
            cost = duration * rate_per_hour  # Tính phí dựa trên thời gian chơi và giá mỗi giờ
            self.usage_history.append(f"{self.name} kết thúc sử dụng PC {pc.pc_id} sau {duration} giờ. Phí: {cost} VND")
            print(f"Phí sử dụng: {cost} VND")
            return cost
        return 0

import tkinter as tk
from tkinter import messagebox

# Màn hình chính cho người dùng bình thường
def open_main_screen(root, user):
    # Tạo cửa sổ mới cho màn hình chính
    main_window = tk.Toplevel(root)
    main_window.title("Màn hình chính")
    main_window.geometry("400x300")

    # Hiển thị thông tin người dùng
    label_user_info = tk.Label(main_window, text=f"Xin chào, {user.username}!", font=("Arial", 14))
    label_user_info.pack(pady=10)

    label_balance = tk.Label(main_window, text=f"Số dư tài khoản: {user.balance} VND", font=("Arial", 12))
    label_balance.pack(pady=10)

    # Hiển thị các dịch vụ có sẵn
    label_services = tk.Label(main_window, text="Dịch vụ có sẵn:", font=("Arial", 12))
    label_services.pack(pady=10)

    for service, cost in user.cafe.services.items():
        service_button = tk.Button(main_window, text=f"{service} - {cost} VND", command=lambda s=service: use_service(user, s, main_window))
        service_button.pack(pady=5)

    # Nút đăng xuất
    button_logout = tk.Button(main_window, text="Đăng xuất", command=main_window.destroy)
    button_logout.pack(pady=20)

# Hàm sử dụng dịch vụ
def use_service(user, service_name, main_window):
    cost = user.cafe.services[service_name]
    if user.balance >= cost:
        user.use_service(service_name, cost)
        messagebox.showinfo("Thành công", f"Bạn đã sử dụng {service_name}. Số dư còn lại: {user.balance} VND")
    else:
        messagebox.showerror("Lỗi", "Số dư không đủ!")

# Màn hình dành cho quản lý (Admin)
def open_admin_screen(root, admin_user):
    # Tạo cửa sổ mới cho quản lý
    admin_window = tk.Toplevel(root)
    admin_window.title("Giao diện quản lý")
    admin_window.geometry("400x400")

    # Hiển thị thông tin quản lý
    label_admin_info = tk.Label(admin_window, text=f"Xin chào Quản lý, {admin_user.username}!", font=("Arial", 14))
    label_admin_info.pack(pady=10)

    # Quản lý người dùng (ví dụ, thêm, xóa, cập nhật)
    button_manage_users = tk.Button(admin_window, text="Quản lý người dùng", command=lambda: manage_users(admin_user))
    button_manage_users.pack(pady=10)

    # Quản lý máy tính
    button_manage_pcs = tk.Button(admin_window, text="Quản lý máy tính", command=lambda: manage_pcs(admin_user))
    button_manage_pcs.pack(pady=10)

    # Nút đăng xuất
    button_logout = tk.Button(admin_window, text="Đăng xuất", command=admin_window.destroy)
    button_logout.pack(pady=20)

# Hàm quản lý người dùng (dự phòng)
def manage_users(admin_user):
    messagebox.showinfo("Thông báo", "Chức năng quản lý người dùng đang được phát triển.")

# Hàm quản lý máy tính (dự phòng)
def manage_pcs(admin_user):
    messagebox.showinfo("Thông báo", "Chức năng quản lý máy tính đang được phát triển.")

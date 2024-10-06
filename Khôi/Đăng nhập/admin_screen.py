import tkinter as tk
from tkinter import messagebox

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

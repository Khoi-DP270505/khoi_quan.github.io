import tkinter as tk
from tkinter import messagebox
from game_cafe import GameCafe
from user import User
from pc import PC
from main_screen import open_main_screen

# Khởi tạo quán game
cafe = GameCafe()

# Load dữ liệu từ file CSV khi khởi động
cafe.load_data_from_csv("users.csv", "pcs.csv")

# Giao diện đăng nhập
def login(root, entry_username, entry_password):
    username = entry_username.get()
    password = entry_password.get()

    # Kiểm tra thông tin đăng nhập
    user = cafe.get_user_by_username(username)
    if user and user.password == password:
        user.cafe = cafe  # Gán quán game cho người dùng
        open_main_screen(root, user)  # Mở màn hình chính sau khi đăng nhập thành công
    else:
        messagebox.showerror("Lỗi", "Sai tên đăng nhập hoặc mật khẩu!")

# Giao diện đăng ký người dùng mới
def open_register_window():
    register_window = tk.Toplevel(root)
    register_window.title("Đăng ký người dùng")
    register_window.geometry("400x400")
    register_window.configure(bg="#f0f0f0")  # Thêm màu nền

    frame = tk.Frame(register_window, bg="#f0f0f0")
    frame.pack(padx=20, pady=20)

    # Tên đăng nhập
    label_username = tk.Label(frame, text="Tên đăng nhập:", font=("Arial", 12), bg="#f0f0f0")
    label_username.grid(row=0, column=0, pady=10, sticky="w")
    entry_username = tk.Entry(frame, width=30, font=("Arial", 12))
    entry_username.grid(row=0, column=1, pady=10)

    # Mật khẩu
    label_password = tk.Label(frame, text="Mật khẩu:", font=("Arial", 12), bg="#f0f0f0")
    label_password.grid(row=1, column=0, pady=10, sticky="w")
    entry_password = tk.Entry(frame, show="*", width=30, font=("Arial", 12))
    entry_password.grid(row=1, column=1, pady=10)

    # Xác nhận mật khẩu
    label_confirm_password = tk.Label(frame, text="Nhập lại mật khẩu:", font=("Arial", 12), bg="#f0f0f0")
    label_confirm_password.grid(row=2, column=0, pady=10, sticky="w")
    entry_confirm_password = tk.Entry(frame, show="*", width=30, font=("Arial", 12))
    entry_confirm_password.grid(row=2, column=1, pady=10)

    # Nút xác nhận đăng ký
    button_register = tk.Button(frame, text="Xác nhận đăng ký", command=lambda: register_user(entry_username.get(), entry_password.get(), entry_confirm_password.get(), register_window), font=("Arial", 12), bg="#4CAF50", fg="white")
    button_register.grid(row=3, column=0, columnspan=2, pady=20)

# Hàm đăng ký người dùng mới
def register_user(username, password, confirm_password, window):
    if username and password and confirm_password:
        if password != confirm_password:
            messagebox.showerror("Lỗi", "Mật khẩu không khớp!")
        else:
            if cafe.get_user_by_username(username):
                messagebox.showerror("Lỗi", "Tên đăng nhập đã tồn tại!")
            else:
                new_user_id = cafe.generate_next_user_id()
                new_user = User(new_user_id, username, password, 0)
                cafe.add_user(new_user)
                messagebox.showinfo("Thành công", "Đăng ký thành công!")
                window.destroy()
    else:
        messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin.")

# Tạo giao diện chính
root = tk.Tk()
root.title("Đăng nhập")
root.geometry("400x300")
root.configure(bg="#f0f0f0")  # Thêm màu nền

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(padx=20, pady=20)

label_title = tk.Label(frame, text="Quản lý quán game", font=("Arial", 16, "bold"), bg="#f0f0f0")
label_title.grid(row=0, column=0, columnspan=2, pady=10)

label_username = tk.Label(frame, text="Tên đăng nhập:", font=("Arial", 12), bg="#f0f0f0")
label_username.grid(row=1, column=0, pady=10, sticky="w")
entry_username = tk.Entry(frame, width=30, font=("Arial", 12))
entry_username.grid(row=1, column=1, pady=10)

label_password = tk.Label(frame, text="Mật khẩu:", font=("Arial", 12), bg="#f0f0f0")
label_password.grid(row=2, column=0, pady=10, sticky="w")
entry_password = tk.Entry(frame, show="*", width=30, font=("Arial", 12))
entry_password.grid(row=2, column=1, pady=10)

button_login = tk.Button(frame, text="Đăng nhập", command=lambda: login(root, entry_username, entry_password), font=("Arial", 12), bg="#4CAF50", fg="white")
button_login.grid(row=3, column=0, columnspan=2, pady=20)

button_register = tk.Button(frame, text="Đăng ký", command=open_register_window, font=("Arial", 12), bg="#008CBA", fg="white")
button_register.grid(row=4, column=0, columnspan=2, pady=10)

# Khi chương trình kết thúc, lưu lại dữ liệu
def on_closing():
    cafe.save_data_to_csv("users.csv", "pcs.csv")
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()

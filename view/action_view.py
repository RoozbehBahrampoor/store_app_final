import tkinter as tk
from tkinter import messagebox

def show_action_panel(user_role, asset_type):
    window = tk.Tk()
    window.title("انتخاب عملکرد")
    window.geometry("300x300")

    tk.Label(window, text=f"عملیات مربوط به {asset_type}", font=("B Nazanin", 12)).pack(pady=10)

    def not_implemented(action):
        messagebox.showinfo("در حال توسعه", f"عملکرد '{action}' برای {asset_type} هنوز پیاده‌سازی نشده است.")

    if user_role == "admin":
        tk.Button(window, text="ثبت اطلاعات", width=25, command=lambda: not_implemented("ثبت")).pack(pady=5)
        tk.Button(window, text="حذف اطلاعات", width=25, command=lambda: not_implemented("حذف")).pack(pady=5)
        tk.Button(window, text="ویرایش اطلاعات", width=25, command=lambda: not_implemented("ویرایش")).pack(pady=5)

    # مشترک بین admin و customer
    tk.Button(window, text="جستجوی اطلاعات", width=25, command=lambda: not_implemented("جستجو")).pack(pady=5)
    tk.Button(window, text="مشاهده اطلاعات", width=25, command=lambda: not_implemented("مشاهده")).pack(pady=5)

    window.mainloop()

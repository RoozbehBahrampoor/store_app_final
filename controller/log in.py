import tkinter as tk
from tkinter import messagebox
from view.info_view import show_asset_selection

def login_window():
    window = tk.Tk()
    window.title("ورود")
    window.geometry("300x250")

    # مقدار اولیه "none" که به هیچ گزینه‌ای مربوط نیست
    role_var = tk.StringVar(value="none")

    tk.Label(window, text="نام کاربری:").pack()
    username_entry = tk.Entry(window)
    username_entry.pack()

    tk.Label(window, text="رمز عبور:").pack()
    password_entry = tk.Entry(window, show="*")
    password_entry.pack()

    tk.Label(window, text="نقش خود را انتخاب کنید:").pack()

    admin_radio = tk.Radiobutton(window, text="مدیر", variable=role_var, value="admin")
    admin_radio.pack()

    customer_radio = tk.Radiobutton(window, text="مشتری", variable=role_var, value="customer")
    customer_radio.pack()

    def login():
        username = username_entry.get()
        password = password_entry.get()
        role = role_var.get()

        if role == "none" or username == "" or password == "":
            messagebox.showwarning("خطا", "لطفاً همه فیلدها را کامل و نقش را انتخاب کنید.")
            return

        if role == "admin" and username == "mdm" and password == "1234":
            messagebox.showinfo("ورود موفق", "سلام mani عزیز، خوش آمدید.")
            window.destroy()
            show_asset_selection("admin")

        elif role == "customer" and username == "hmn" and password == "5678":
            messagebox.showinfo("ورود موفق", "سلام arman عزیز، خوش آمدید.")
            window.destroy()
            show_asset_selection("customer")

        else:
            messagebox.showerror("خطا", "نام کاربری، رمز عبور یا نقش اشتباه است.")

    tk.Button(window, text="ورود", command=login).pack(pady=10)

    window.mainloop()

# اجرای برنامه
if __name__ == "__main__":
    login_window()


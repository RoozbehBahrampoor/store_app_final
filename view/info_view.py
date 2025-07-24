import tkinter as tk
from view.action_view import show_action_panel  # ایمپورت پنجره عملکرد بعدی

def show_asset_selection(user_role):
    window = tk.Tk()
    window.title("انتخاب نوع دارایی")
    window.geometry("250x200")

    def select_asset(asset_type):
        window.destroy()
        show_action_panel(user_role, asset_type)

    tk.Label(window, text="نوع دارایی مورد نظر را انتخاب کنید:", font=("B Nazanin", 11)).pack(pady=10)

    tk.Button(window, text="خانه", width=20, command=lambda: select_asset("خانه")).pack(pady=10)
    tk.Button(window, text="ماشین", width=20, command=lambda: select_asset("ماشین")).pack(pady=10)

    window.mainloop()


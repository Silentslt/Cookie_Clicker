import tkinter as tk
import functions
import os

window = tk.Tk()
window.title("Cookie Clicker")
window.geometry("500x500")
window.minsize(500, 500)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(BASE_DIR, "Images", "cookie.png")



cookie_img = tk.PhotoImage(file=image_path)

score_label = tk.Label(window, text="Cookies: 0", font=("Arial", 20))
score_label.pack(pady=20)

cookie_button = tk.Button(window,image=cookie_img, command=lambda: functions.click_cookie(score_label),borderwidth=0)
cookie_button.pack(expand=True)
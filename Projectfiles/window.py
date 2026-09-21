import tkinter as tk
import functions
import os
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Cookie Clicker")
window.geometry("500x500")
window.minsize(500, 500)

dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(dir, "Images", "cookie.png")

pil_image = Image.open(image_path)
pil_image = pil_image.resize((200, 200), Image.LANCZOS)
cookie_img = ImageTk.PhotoImage(pil_image)

score_label = tk.Label(window, text="Cookies: 0", font=("Arial", 20))

score_label.pack(pady=20)

level_label = tk.Label(window, text="Level: Crumb", font=("Arial", 12))

level_label.pack(pady=(0, 10))

cookie_button = tk.Button(window, image=cookie_img,command=lambda: functions.click_cookie(score_label, level_label),borderwidth=0)

cookie_button.pack(expand=True)

upgrade_button = tk.Button(window, text="Upgrade Level",command=lambda: functions.upgrade_level(level_label,score_label))

upgrade_button.pack(pady=20)

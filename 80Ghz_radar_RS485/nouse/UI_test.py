import tkinter as tk
from tkinter import ttk, font

    
root = tk.Tk()
root.title("RS485信息")
root.geometry("640x300")

font_style = font.Font(size=40)

dis_t = 310
distance_label = ttk.Label(root, text="當前空距:{}".format(dis_t), font=font_style)
distance_label.pack(pady=10)

initial_alarm_text = 300
alarm_label = ttk.Label(root, text="警示空距: {}".format(initial_alarm_text), font=font_style)
alarm_label.pack(pady=10)

frequency_t = 10
frequency_label = ttk.Label(root, text="回傳頻率: {}".format(frequency_t), font=font_style)
frequency_label.pack(pady=10)

root.mainloop()
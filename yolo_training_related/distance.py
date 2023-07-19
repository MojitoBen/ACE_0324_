'''
計算兩點座標距離(簡易UI介面)
'''
import math
import tkinter as tk
from tkinter import messagebox

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def on_calculate():
    try:
        x1 = float(entry_x1.get())
        y1 = float(entry_y1.get())
        x2 = float(entry_x2.get())
        y2 = float(entry_y2.get())
        
        distance = calculate_distance(x1, y1, x2, y2)
        messagebox.showinfo("結果", f"兩點之間的距離為: {distance}")
    except ValueError:
        messagebox.showerror("錯誤", "請確保輸入的座標是數字")

# 建立主視窗
root = tk.Tk()
root.title("兩點座標距離計算")

# 建立UI元件
label_x1 = tk.Label(root, text="x1:")
label_x1.pack()
entry_x1 = tk.Entry(root)
entry_x1.pack()

label_y1 = tk.Label(root, text="y1:")
label_y1.pack()
entry_y1 = tk.Entry(root)
entry_y1.pack()

label_x2 = tk.Label(root, text="x2:")
label_x2.pack()
entry_x2 = tk.Entry(root)
entry_x2.pack()

label_y2 = tk.Label(root, text="y2:")
label_y2.pack()
entry_y2 = tk.Entry(root)
entry_y2.pack()

btn_calculate = tk.Button(root, text="確定", command=on_calculate)
btn_calculate.pack()

# 開始運行主視窗
root.mainloop()

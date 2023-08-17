from UI_functions_adj import *
import tkinter as tk
from tkinter import ttk, Canvas
from datetime import datetime, timedelta
import logging



# 建立主視窗
root = tk.Tk()
root.title("鋼捲歷史資料查詢系統")
#root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight() - 80)) 
#root.state('zoomed') #視窗最大化
# 獲取螢幕尺寸
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# 計算相對尺寸
window_width_percent = 0.8  # 視窗寬度佔螢幕寬度的百分比
window_height_percent = 0.8  # 視窗高度佔螢幕高度的百分比
window_width = int(screen_width * window_width_percent)
window_height = int(screen_height * window_height_percent)
'''
# 檢查螢幕尺寸是否小於指定尺寸，如果是，使用螢幕尺寸
if screen_width < window_width or screen_height < window_height:
    root.geometry("{0}x{1}+0+0".format(screen_width, screen_height))
    root.state('zoomed') #視窗最大化
else:
    root.geometry("{0}x{1}+0+0".format(window_width, window_height - 80))
    '''
# 設定主視窗的外觀樣式
style = ttk.Style()
style.configure("TFrame", background="gray70")
style.configure("TLabel", background="gray70", font=("Arial", int(window_height * 0.02), "bold"))  # 設定標籤字體大小
style.configure("TButton", font=("Arial", int(window_height * 0.02), "bold"))  # 設定按鈕字體大小
style.configure("Treeview.Heading", font=("Arial", int(window_height * 0.02), "bold"))  # 設定表格標題字體大小
style.configure("Treeview", font=("Arial", int(window_height * 0.02), "bold"))  # 設定表格內文字字體大小
style.configure("Treeview", rowheight=int(window_height * 0.03))
style.map("Treeview", background=[('selected', 'green')], bordercolor=[('selected', 'green')])
style.configure("Treeview.Heading", borderwidth=1, relief="solid")
# 建立主框架
main_frame = ttk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)
# 建立上方查詢欄位框架
query_frame = ttk.Frame(main_frame, padding=int(window_height * 0.01))
query_frame.pack(fill=tk.X)
vcmd = (query_frame.register(validate), '%P')
# 建立查詢欄位元件並使用grid佈局
query_entry = ttk.Entry(query_frame, font=("Arial", int(window_height * 0.02)), validate='key', validatecommand=vcmd)
query_entry.grid(row=0, column=0, padx=int(window_width * 0.01), pady=int(window_height * 0.01))
query_button = ttk.Button(query_frame, text="查詢鋼捲")
query_button.grid(row=0, column=1, padx=5)
# 建立選擇日期按鈕
select_date_button = ttk.Button(query_frame, text="選擇日期")
select_date_button.grid(row=0, column=2, padx=5)
# 建立日期顯示的 Label
selected_date_var = tk.StringVar()
selected_date_label = ttk.Label(query_frame, textvariable=selected_date_var)
selected_date_label.grid(row=0, column=3, padx=5)
# 設定預設日期區間
end_date = datetime.now().date() + timedelta(days=1)
start_date = end_date - timedelta(days=29)
selected_date_var.set(f"{start_date.strftime('%Y/%m/%d')} ~ {end_date.strftime('%Y/%m/%d')}")
# 放大圖片按鈕
enlarge_button = ttk.Button(query_frame, text="放大圖片")
enlarge_button.grid(row=0, column=4, padx=5)
# 建立匯出按鈕
export_button = ttk.Button(query_frame, text="匯出")
export_button.grid(row=0, column=5, padx=5)
# 建立手動更改比對結果按鈕
condition_button = ttk.Button(query_frame, text="更改比對結果")
condition_button.grid(row=0, column=6, padx=5)
# 設定查詢欄位框架的寬度
query_frame.pack(fill=tk.X, pady=10)
# 建立表格框架
table_frame = ttk.Frame(main_frame)
table_frame.pack(fill=tk.BOTH, expand=True)
# 建立表格標題
header = ["編號", "日期", "L1資料", "Cam1號碼", "比對結果"]
widths = [int(window_width * 0.01) * 20, int(window_width * 0.01) * 200, int(window_width * 0.01) * 120, 
          int(window_width * 0.01) * 120, int(window_width * 0.01) * 20]
tree = ttk.Treeview(table_frame, columns=header, show="headings")
for col, width in zip(header, widths):
    tree.heading(col, text=col)
    tree.column(col, width=width, anchor=tk.CENTER)
tree.pack(side=tk.LEFT, padx=int(window_width * 0.01), pady=int(window_height * 0.01), fill=tk.BOTH, expand=True)
# 更新資料表格的欄位顯示順序和高度
tree.column("編號", width=30, anchor=tk.CENTER)
tree.column("日期", width=240, anchor=tk.CENTER)
tree.column("L1資料", width=150, anchor=tk.CENTER)
tree.column("Cam1號碼", width=150, anchor=tk.CENTER)
tree.column("比對結果", width=30, anchor=tk.CENTER)
# 設定比對結果的顏色
tree.tag_configure("OK", foreground="green")
tree.tag_configure("NG", foreground="red")
tree.tag_configure("CHECK", foreground="blue")
# 建立垂直滾動條
scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.configure(yscrollcommand=scrollbar.set)
# 建立底部框架
bottom_frame = ttk.Frame(main_frame, padding=int(window_height * 0.01))
bottom_frame.pack(fill=tk.BOTH)
# 建立翻頁按鈕和頁數標籤
renew_button = ttk.Button(bottom_frame, text="更新")
renew_button.grid(row=0, column=0, padx=int(window_width * 0.01), pady=int(window_height * 0.01))
Now_Page = "當前頁數"
Total_Page = "總頁數"
total_pages_label = ttk.Label(bottom_frame, text= Now_Page + "/" + Total_Page)
total_pages_label.grid(row=0, column=1, padx=int(window_width * 0.01), pady=int(window_height * 0.01))
prev_button = ttk.Button(bottom_frame, text="上一頁")
prev_button.grid(row=0, column=2, padx=int(window_width * 0.01), pady=int(window_height * 0.01))
next_button = ttk.Button(bottom_frame, text="下一頁")
next_button.grid(row=0, column=3, padx=int(window_width * 0.01), pady=int(window_height * 0.01))
bottom_frame.grid_columnconfigure(3, weight=1)
# 調整主視窗的位置
root.update_idletasks()
x_pos = (screen_width - window_width) // 2
y_pos = (screen_height - window_height) // 2 - int(window_height * 0.04)  # 提升視窗位置30個像素(依工具列調整)
root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")
# 建立顯示img的框架 1.隨便放圖 2.現場影像 3.cam1全圖 4.cam1噴字特寫
img_frame1 = Canvas(bottom_frame, width=int(window_width * 0.23), height=int(window_height * 0.32), relief=tk.RAISED, borderwidth=1)
img_frame1.grid(row=1, column=0, padx=int(window_width * 0.01), pady=int(window_height * 0.01))
img_frame2 = Canvas(bottom_frame, width=int(window_width * 0.23), height=int(window_height * 0.32), relief=tk.RAISED, borderwidth=1)
img_frame2.grid(row=1, column=1, padx=int(window_width * 0.01), pady=int(window_height * 0.01))
img_frame3 = Canvas(bottom_frame, width=int(window_width * 0.23), height=int(window_height * 0.32), relief=tk.RAISED, borderwidth=1)
img_frame3.grid(row=1, column=2, padx=int(window_width * 0.01), pady=int(window_height * 0.01))
img_frame4 = Canvas(bottom_frame, width=int(window_width * 0.23), height=int(window_height * 0.32), relief=tk.RAISED, borderwidth=1)
img_frame4.grid(row=1, column=3, padx=int(window_width * 0.01), pady=int(window_height * 0.01))
# 建立顯示img的標籤 1.固定顯示文字 2.固定顯示文字 3.L1資料 4.cam1噴字
var_frame1 = ttk.Frame(bottom_frame, width=450, height=100, relief=tk.RAISED, borderwidth=1)
var_frame1.grid(row=2, column=0, padx=10, pady=(0, 10))
var_label1 = ttk.Label(var_frame1, text="鋼捲噴字辨識")
var_label1.pack()
var_frame2 = ttk.Frame(bottom_frame, width=450, height=100, relief=tk.RAISED, borderwidth=1)
var_frame2.grid(row=2, column=1, padx=10, pady=(0, 10))
var_label2 = ttk.Label(var_frame2, text="產線 LV.1 鋼捲資料：")
var_label2.pack()
var_frame3 = ttk.Frame(bottom_frame, width=450, height=100, relief=tk.RAISED, borderwidth=1)
var_frame3.grid(row=2, column=2, padx=10, pady=(0, 10))
var_label3 = ttk.Label(var_frame3, text="LV.1")
var_label3.pack()
var_frame4 = ttk.Frame(bottom_frame, width=450, height=50, relief=tk.RAISED, borderwidth=1)
var_frame4.grid(row=2, column=3, padx=10, pady=(0, 10))
var_label4 = ttk.Label(var_frame4, text="Cam1辨識資料")
var_label4.pack()
# 設定查詢欄位框架的寬度
query_frame.grid_columnconfigure(0, weight=1)
# 在程式開始運行時建立 image_label2
image_label2 = ttk.Label(img_frame2)
image_label2.pack()
#把按鈕加上功能
query_button.configure( command=lambda: query(query_entry,selected_date_var,tree,total_pages_label))
renew_button.configure( command=lambda: renew(selected_date_var,query_entry,total_pages_label,tree, img_frame1, img_frame2, img_frame3, img_frame4, var_label2, var_label3, var_label4, image_label2))
select_date_button.configure( command=lambda: select_date(selected_date_var, root, query_entry,total_pages_label,tree, img_frame1, img_frame2, img_frame3, img_frame4, var_label2, var_label3, var_label4, image_label2))
next_button.configure( command=lambda: next_page(total_pages_label,tree,selected_date_var))
prev_button.configure( command=lambda: previous_page(total_pages_label,tree,selected_date_var))
export_button.configure( command=lambda: export_data_to_excel(selected_date_var))
enlarge_button.configure( command=lambda: show_enlarge_view(img_frame3, img_frame4, tree))
condition_button.configure( command=lambda: update_result(root,selected_date_var,query_entry,total_pages_label,tree, img_frame1, img_frame2, img_frame3, img_frame4, var_label2, var_label3, var_label4, image_label2))
#condition_button
tree.bind("<<TreeviewSelect>>", lambda event: select_row(tree, event, img_frame1, img_frame2, img_frame3, img_frame4, var_label2, var_label3, var_label4, window_width, window_height))
def update_frame2():
            ret, frame = cap.read()
            if ret:
                # 調整串流畫面大小為與影像顯示區域相同
                width=int(window_width * 0.23)
                height=int(window_height * 0.32)
                frame = cv2.resize(frame, (width, height))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(frame)
                photo = ImageTk.PhotoImage(image)
                image_label2.configure(image=photo)
                image_label2.image = photo
            image_label2.after(10, update_frame2)
def initialize():   
    renew(selected_date_var, query_entry, total_pages_label, tree, img_frame1, img_frame2, img_frame3, img_frame4, var_label2, var_label3, var_label4, image_label2)

notification = False  
original_result_count = 0

if __name__ == "__main__":

    logname = 'UI_log/'
    logname = logname+"{:%Y-%m-%d}".format(datetime.now())+'.log'
    FORMAT = '%(asctime)s %(levelname)s: %(message)s'
    #logging.getLogger("requests").setLevel(logging.WARNING)
    #logging.getLogger("urllib3").setLevel(logging.WARNING)  
    logging.basicConfig(level=logging.INFO, filename=logname, filemode='a', format=FORMAT)
    image_path = "chong.png"
    display_image_on_canvas(img_frame1, image_path, window_width, window_height)
    stream_url1 = 'rtsp://admin:Admin1234@192.168.1.145:554/cam/realmonitor?channel=1&subtype=0' #cam1
    #stream_url2 = 'rtsp://admin:Admin1234@192.168.1.151:554/Streaming/Channels/101' #cam2
    cap = cv2.VideoCapture(stream_url1)
    update_frame2()
    initialize()
    root.after(1000, lambda: update(selected_date_var,tree,total_pages_label,root,query_entry, img_frame1, img_frame2, img_frame3, img_frame4, var_label2, var_label3, var_label4, image_label2))

    # 開始主迴圈
    root.mainloop()



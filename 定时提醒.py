import datetime
import time
import tkinter as tk
import tkinter.messagebox
target_time="2026-3-26 15:30:00"
now_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
while True:
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if now_time >= target_time:
        root=tk.Tk()
        root.withdraw()
        messagebox.showinfo("提醒","现在是下午15点30分")
        break
    else:
        time.sleep(1)
print("运行完毕")
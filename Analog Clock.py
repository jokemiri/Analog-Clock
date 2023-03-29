import tkinter as tk
from math import cos, sin, pi
from datetime import datetime
from tkinter import ttk
from PIL import Image, ImageTk


class AnalogClock(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.size = min(self.winfo_reqwidth(), self.winfo_reqheight())
        self.configure(width=self.size, height=self.size)
        self.update_time()
        
    def update_time(self):
        now = datetime.now()
        hour = now.hour % 12
        minute = now.minute
        second = now.second
        
        self.delete("all")
        
        # Draw clock face
        self.create_oval(10, 10, self.size-10, self.size-10, fill='#eeeee4')
        for i in range(12):
            x1 = self.size/2 + (self.size/2 - 30) * cos((i-3) * pi / 6)
            y1 = self.size/2 + (self.size/2 - 30) * sin((i-3) * pi / 6)
            x2 = self.size/2 + (self.size/2 - 15) * cos((i-3) * pi / 6)
            y2 = self.size/2 + (self.size/2 - 15) * sin((i-3) * pi / 6)
            self.create_line(x1, y1, x2, y2, fill='#154c79')
        
        # Draw hour hand
        xh = self.size/2 + 0.5*(self.size/2 - 60)*cos((hour + minute/60)*pi/6)
        yh = self.size/2 + 0.5*(self.size/2 - 60)*sin((hour + minute/60)*pi/6)
        self.create_line(self.size/2, self.size/2, xh, yh, width=4, fill="#154c79")
        
        # Draw minute hand
        xm = self.size/2 + 0.8*(self.size/2 - 30)*cos(minute*pi/30)
        ym = self.size/2 + 0.8*(self.size/2 - 30)*sin(minute*pi/30)
        self.create_line(self.size/2, self.size/2, xm, ym, width=3, fill="#154c79")
        
        # Draw second hand
        xs = self.size/2 + 0.9*(self.size/2 - 15)*cos(second*pi/30)
        ys = self.size/2 + 0.9*(self.size/2 - 15)*sin(second*pi/30)
        self.create_line(self.size/2, self.size/2, xs, ys, width=2, fill="red")
        
        self.after(1000, self.update_time)

root = tk.Tk()
clock = AnalogClock(root)
root.configure(bg='#eeeee4') #background
root.title("Analog Clock")
root.geometry('400x400')
root.resizable(0, 0) #resizability

icon = ImageTk.PhotoImage(Image.open('icon.png'))
root.iconphoto(False, icon)

clock.pack()

# logo = tk.PhotoImage(file='logo.png')
# tk.Label(root, image=logo, bg='#2596be').place(x=20, y=10)        

hour_label = ttk.Label(root, text="Hour:")
hour_label.pack(side="left", padx=10, pady=10)

hour_box = ttk.Combobox(root, width=5, values=[str(i).zfill(2) for i in range(1, 13)])
hour_box.current(0)
hour_box.pack(side="left", padx=10, pady=10)

minute_label = ttk.Label(root, text="Minute:")
minute_label.pack(side="left", padx=10, pady=10)

minute_box = ttk.Combobox(root, width=5, values=[str(i).zfill(2) for i in range(0, 60)])
minute_box.current(0)
minute_box.pack(side="left", padx=10, pady=10)

second_label = ttk.Label(root, text="Second:")
second_label.pack(side="left", padx=10, pady=10)

second_box = ttk.Combobox(root, width=5, values=[str(i).zfill(2) for i in range(0, 60)])
second_box.current(0)
second_box.pack(side="left", padx=10, pady=10)



def set_clock_time(hour_box, minute_box, second_box, clock):
    hour = int(hour_box.get())
    minute = int(minute_box.get())
    second = int(second_box.get())
    now = datetime.now()
    current_hour = now.hour
    current_minute = now.minute
    current_second = now.second
    diff_seconds = (hour - current_hour) * 3600 + (minute - current_minute) * 60 + (second - current_second)
    clock.after(1000, set_clock_time, hour_box, minute_box, second_box, clock)
    clock.set_clock_time(diff_seconds)

set_button = tk.Button(root, text="Set Time", command=lambda: set_clock_time(hour_box, minute_box, second_box, clock))
set_button.place(x=10, y=10)        

root.mainloop()
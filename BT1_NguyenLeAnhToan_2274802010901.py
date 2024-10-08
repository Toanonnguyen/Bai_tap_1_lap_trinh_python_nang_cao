import tkinter as tk
from tkinter import ttk,messagebox
import matplotlib.pyplot as plt
import numpy as np
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Máy Tính")
        self.geometry("400x300")

        # Tạo menu
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        #Tạo file menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.file_menu.add_command(label="Exit", command=self.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # tạo about menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.help_menu.add_command(label="About", command=self.show_about)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        # tạo tab
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # tạo frame cho tab
        self.tab1_frame = ttk.Frame(self.notebook)
        self.tab2_frame = ttk.Frame(self.notebook)

        # thêm frame
        self.notebook.add(self.tab1_frame, text="Tính Toán")
        self.notebook.add(self.tab2_frame, text="Đồ Thị")

        # tạo nhập cho tab 1
        self.label1 = tk.Label(self.tab1_frame, text="Nhập số thứ nhất:")
        self.label1.grid(row=0, column=0, columnspan=2)
        self.so1 = tk.Entry(self.tab1_frame)
        self.so1.grid(row=0, column=2, columnspan=2)
        self.label2 = tk.Label(self.tab1_frame, text="Nhập số thứ hai:")
        self.label2.grid(row=1, column=0, columnspan=2)
        self.so2 = tk.Entry(self.tab1_frame)
        self.so2.grid(row=1, column=2, columnspan=2)
        #tạo nhập cho tab 2
        self.label1 = tk.Label(self.tab2_frame, text="Nhập x max:")
        self.label1.grid(row=0, column=0, columnspan=2)
        self.a = tk.Entry(self.tab2_frame)
        self.a.grid(row=0, column=2, columnspan=2)
        self.label2 = tk.Label(self.tab2_frame, text="Nhập x min:")
        self.label2.grid(row=1, column=0, columnspan=2)
        self.b = tk.Entry(self.tab2_frame)
        self.b.grid(row=1, column=2, columnspan=2)
        #tạo nút tab1
        self.button1 = tk.Button(self.tab1_frame, text="Tính", command=self.Tinh)
        self.button1.grid(row=5, column=3, columnspan=2)
        #chọn phép tính tab 1
        self.operation_menu0= tk.StringVar(self.tab1_frame)
        self.operation_menu= tk.Label(self.tab1_frame, text="Chọn phép tính:")
        self.operation_menu.grid(row=4, column=0, columnspan=2)
        self.operation_menu_option = tk.OptionMenu(self.tab1_frame,self.operation_menu0 ,"+", "-", "*", "/")
        self.operation_menu_option.grid(row=4, column=2, columnspan=2)
        #tạo nút tab 2
        self.button2 = tk.Button(self.tab2_frame, text="Đồ Thị", command=self.DoThi)
        self.button2.grid(row=5, column=3, columnspan=2)
        #chọn phép tính tab 2
        self.operation_menu1= tk.StringVar(self.tab2_frame)
        self.operation_menu= tk.Label(self.tab2_frame, text="Chọn phép tính:")
        self.operation_menu.grid(row=4, column=0, columnspan=2)
        self.operation_menu_option = tk.OptionMenu(self.tab2_frame,self.operation_menu1 ,"sin", "cos")
        self.operation_menu_option.grid(row=4, column=2, columnspan=2)
        # Tạo frame lịch sử
        self.history_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.history_frame, text="Lịch sử")

        # Tạo danh sách lịch sử
        self.history_listbox = tk.Listbox(self.history_frame, height=10)
        self.history_listbox.pack(fill=tk.BOTH, expand=True)
        #Tạo Lịch sử của tab 1
        self.button1.bind("<Button-1>", lambda event: self.add_to_history(f"{self.so1.get()} {self.operation_menu0.get()} {self.so2.get()}")) 
        #Tạo Lịch sử của tab 2
        self.button2.bind("<Button-1>", lambda event: self.add_to_history(f"({self.a.get()},{self.b.get()})"))

    def add_to_history(self, expression):
        try:
            result = eval(expression)
            history_item = f"{expression} = {result}"
            self.history_listbox.insert(0, history_item)
            self.history_listbox.see(0)  # Scroll to the top
        except Exception as e:
            self.history_listbox.insert(0, f"Error: {e}")
    def show_about(self):
        self.about_window = tk.Toplevel(self)
        self.about_window.title("About")

        self.about_window.geometry("300x200")
        self.label = tk.Label(self.about_window, text="Máy tính toán\nTạo bởi Nguyễn Lê Anh Toàn\nVersion 1.0")
        self.label.pack(pady=20)

        self.close_button = tk.Button(self.about_window, text="Close", command=self.about_window.destroy)
        self.close_button.pack(pady=10)
    def Tinh(self):
        so1=float(self.so1.get())
        so2=float(self.so2.get())
        # Thực hiện phép tính
        operation = self.operation_menu0.get()
        if operation == "+":
            ketqua = so1 + so2
        elif operation == "-":
            ketqua = so1 - so2
        elif operation == "*":
            ketqua = so1 * so2
        elif operation == "/":
            ketqua = so1 / so2
        messagebox.showinfo("Kết quả",f"Phép tính {so1} {operation} {so2} = {ketqua}")
    def DoThi(self):
        x=np.linspace(float(self.a.get()),float(self.b.get()),100)
        # Thực hiện đồ thị
        operation = self.operation_menu1.get()
        if operation == "sin":
            y=np.sin(x)
        elif operation == "cos":
            y=np.cos(x)
        plt.plot(x,y)
        plt.show()
if __name__ == "__main__":
        app = MainWindow()
        app.mainloop()
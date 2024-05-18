import tkinter as tk
from Interface.TextInterface.TextInterface import TextInterface
from Interface.ImageInterface.ImageInterface import ImageInterface
class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Steago Tool")
        
        # Tạo navbar
        self.navbar = Navbar(self)
        self.navbar.pack(side="left", fill="y")

        # Tạo container để chứa các giao diện
        self.container = tk.Frame(self)
        self.container.pack(side="right", fill="both", expand=True)

        # Hiển thị giao diện mặc định
        self.show_interface(TextInterface)

    def show_interface(self, interface):
        # Xóa bỏ các giao diện hiện tại trong container
        for widget in self.container.winfo_children():
            widget.destroy()

        # Hiển thị giao diện mới
        interface_instance = interface(self.container, self)
        interface_instance.pack(fill="both", expand=True)

class Navbar(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="gray", width=100)
        
        # Tạo các nút trên navbar
        self.txt_btn = tk.Button(self, text="Text Steganography", command=lambda: master.show_interface(TextInterface))
        self.txt_btn.pack(pady=10)
        
        self.img_btn = tk.Button(self, text="Image Steganography", command=lambda: master.show_interface(ImageInterface))
        self.img_btn.pack(pady=10)
        
        self.audio_btn = tk.Button(self, text="Audio Steganography", command=lambda: master.show_interface(Interface3))
        self.audio_btn.pack(pady=10)

        self.video_btn = tk.Button(self, text="Video Steganography", command=lambda: master.show_interface(Interface4))
        self.video_btn.pack(pady=10)

class Interface3(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="white")
        
        # Hiển thị nội dung của giao diện 3
        label = tk.Label(self, text="Interface 3", font=("Arial", 18))
        label.pack(pady=50)
class Interface4(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="white")
        
        # Hiển thị nội dung của giao diện 1
        label = tk.Label(self, text="Interface 4", font=("Arial", 18))
        label.pack(pady=50)

if __name__ == "__main__":
    app = MainApplication()
    app.geometry("800x400+300+200")

    app.mainloop()

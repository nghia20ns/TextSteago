import tkinter as tk
from Interface.ImageInterface.EncodeComponent import EncodeComponent
from Interface.ImageInterface.DecodeComponent import DecodeComponent

class ImageInterface(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="white")
        
        # Biến trạng thái
        self.current_state = "Encode"  # Mặc định là Encode

        # Header
        self.header_frame = tk.Frame(self, bg="lightgray")
        self.header_frame.pack(fill="x")
        # Nút Encode
        self.encode_btn = tk.Button(self.header_frame, text="Encode", command=self.switch_to_encode)
        self.encode_btn.pack(side="left", padx=10)

        # Nút Decode
        self.decode_btn = tk.Button(self.header_frame, text="Decode", command=self.switch_to_decode)
        self.decode_btn.pack(side="left", padx=10)

        # Component cho Encode
        self.encode_component = EncodeComponent(self)
        # Hiển thị mặc định
        self.encode_component.pack(pady=20)

        # Component cho Decode
        self.decode_component = DecodeComponent(self)

    def switch_to_encode(self):
        if self.current_state != "Encode":
            self.current_state = "Encode"
            self.encode_btn.config(state=tk.DISABLED)
            self.decode_btn.config(state=tk.NORMAL)
            self.decode_component.pack_forget()
            self.encode_component.pack(pady=20)

    def switch_to_decode(self):
        if self.current_state != "Decode":
            self.current_state = "Decode"
            self.encode_btn.config(state=tk.NORMAL)
            self.decode_btn.config(state=tk.DISABLED)
            self.encode_component.pack_forget()
            self.decode_component.pack(pady=20)

# class EncodeComponent(tk.Frame):
#     def __init__(self, master):
#         super().__init__(master, bg="lightblue")
#         label = tk.Label(self, text="Encode Component", font=("Arial", 14), bg="lightblue")
#         label.pack(padx=20, pady=20)
# class DecodeComponent(tk.Frame):
#     def __init__(self, master):
#         super().__init__(master, bg="lightblue")
#         label = tk.Label(self, text="Decode Component", font=("Arial", 14), bg="lightblue")
#         label.pack(padx=20, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    text_interface = ImageInterface(root, None)
    text_interface.pack(fill="both", expand=True)
    root.mainloop()

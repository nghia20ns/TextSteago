import tkinter as tk
from tkinter import filedialog
from binary import *
from matplotlib import pyplot as plt
import cv2

class EncodeComponent(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="lightblue")

        # Tiêu đề
        label = tk.Label(self, text="Encode Component", font=("Arial", 14), bg="lightblue")
        label.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        # Label và Entry cho văn bản cần giải mã
        lbl_text = tk.Label(self, text="Text to encode:", bg="lightblue")
        lbl_text.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.edit_entry = tk.Entry(self, width=30)
        self.edit_entry.grid(row=1, column=1, pady=5, sticky="we")
        self.edit_entry.grid_columnconfigure(1, weight=1)  # Đảm bảo ô nhập văn bản mở rộng theo chiều ngang

        # Button "Browse File" và Entry "File Path"
        lbl_file = tk.Label(self, text="Browse File:", bg="lightblue")
        lbl_file.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        browse_button = tk.Button(self, text="Browse", command=self.browse_file)
        browse_button.grid(row=2, column=2, padx=10, sticky="e")
        self.file_path_entry = tk.Entry(self, width=50)
        self.file_path_entry.grid(row=2, column=1, pady=5, sticky="we")
        self.file_path_entry.grid_columnconfigure(1, weight=1)  # Đảm bảo ô nhập văn bản mở rộng theo chiều ngang

        # Button "Browse Folder Save" và Entry "Folder Path Save"
        lbl_folder = tk.Label(self, text="Browse Folder Save:", bg="lightblue")
        lbl_folder.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.folder_path_entry_save = tk.Entry(self, width=50)
        self.folder_path_entry_save.grid(row=3, column=1, pady=5, sticky="we")
        self.folder_path_entry_save.grid_columnconfigure(1, weight=1)  # Đảm bảo ô nhập văn bản mở rộng theo chiều ngang

        browse_button_save = tk.Button(self, text="Browse", command=self.browse_folder)
        browse_button_save.grid(row=3, column=2, padx=10, pady=5, sticky="e")

        # Label và Entry cho tên ảnh mới
        lbl_image = tk.Label(self, text="New image name:", bg="lightblue")
        lbl_image.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.new_image = tk.Entry(self, width=30)
        self.new_image.grid(row=4, column=1, pady=5, sticky="we")

        # Button "Submit"
        submit_button = tk.Button(self, text="Submit", command=self.submit)
        submit_button.grid(row=6, column=2, padx=10, pady=5, sticky="e")

    def browse_file(self):
        filename = filedialog.askopenfilename(defaultextension=".png", filetypes=[("All Image files", "*.jpeg;*.jpg;*.png"), ("JPEG files", "*.jpeg"), ("JPG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")])
        
        self.file_path_entry.delete(0, tk.END)
        self.file_path_entry.insert(0, filename)

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        self.folder_path_entry_save.delete(0, tk.END)  # Xóa nội dung trong entry trước khi cập nhật
        self.folder_path_entry_save.insert(0, folder_path)  # Thêm đường dẫn thư mục đã chọn vào entry

    def submit(self):
        #su ly path luu
        full_image_path = self.folder_path_entry_save.get() + "/" + self.new_image.get()
        if not full_image_path.endswith(".png"):
            full_image_path += ".png"

        print("Full image path:", full_image_path)

        image = cv2.imread(self.file_path_entry.get())
        output_path = full_image_path 
        self.encode_img_data(image,output_path)
        lbl_log = tk.Label(self, text="create img successful:", bg="lightblue")
        lbl_log.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        lbl_log = tk.Label(self, text=full_image_path, bg="lightblue")
        lbl_log.grid(row=5, column=1, padx=10, pady=5, sticky="e")

    def encode_img_data(self,img, output_path):
        data = self.edit_entry.get()
        if len(data) == 0: 
            raise ValueError('Data entered to be encoded is empty')

        no_of_bytes = (img.shape[0] * img.shape[1] * 3) // 8

        print("\t\nMaximum bytes to encode in Image:", no_of_bytes)

        if len(data) > no_of_bytes:
            raise ValueError("Insufficient bytes Error, Need Bigger Image or give Less Data !!")

        data += '*^*^*'    

        binary_data = binary.msgtobinary(data)
        print("\nBinary Data:")
        print(binary_data)

        length_data = len(binary_data)
        print("\nThe Length of Binary data:", length_data)

        index_data = 0

        for i in img:
            for pixel in i:
                r, g, b = binary.msgtobinary(pixel)
                if index_data < length_data:
                    pixel[0] = int(r[:-1] + binary_data[index_data], 2) 
                    index_data += 1
                if index_data < length_data:
                    pixel[1] = int(g[:-1] + binary_data[index_data], 2) 
                    index_data += 1
                if index_data < length_data:
                    pixel[2] = int(b[:-1] + binary_data[index_data], 2) 
                    index_data += 1
                if index_data >= length_data:
                    break

        cv2.imwrite(output_path, img)
        print("\nEncoded the data successfully in the Image and the image is successfully saved at:", output_path)


# Kiểm tra
if __name__ == "__main__":
    root = tk.Tk()
    decode_component = EncodeComponent(root)
    decode_component.pack(fill="both", expand=True)
    root.mainloop()

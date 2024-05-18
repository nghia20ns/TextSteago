import tkinter as tk
from tkinter import filedialog
from binary import *
from matplotlib import pyplot as plt
import cv2

class DecodeComponent(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="lightblue")
        # Tiêu đề
        label = tk.Label(self, text="Decode Component", font=("Arial", 14), bg="lightblue")
        label.grid(row=0, column=0, columnspan=3, padx=20, pady=20)
        # Button "Browse File" và Entry "File Path"
        browse_button = tk.Button(self, text="Browse File", command=self.browse_file)
        browse_button.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.file_path_entry = tk.Entry(self, width=50)
        self.file_path_entry.grid(row=1, column=1, pady=5, padx=(0, 10), sticky="we")
        # Button "Submit"
        submit_button = tk.Button(self, text="Submit", command=self.submit)
        submit_button.grid(row=3, column=2, padx=10, pady=5, sticky="e")

    def browse_file(self):
        filename = filedialog.askopenfilename(defaultextension=".png", filetypes=[("All Image files", "*.jpeg;*.jpg;*.png"), ("JPEG files", "*.jpeg"), ("JPG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")])
        
        self.file_path_entry.delete(0, tk.END)
        self.file_path_entry.insert(0, filename)
    def submit(self):
        image = cv2.imread(self.file_path_entry.get())
        self.decode_img_data(image)

    def decode_img_data(self,img):
        data_binary = ""
    
        for i in img:
            for pixel in i:
                r, g, b = binary.msgtobinary(pixel) 
                data_binary += r[-1]  
                data_binary += g[-1]  
                data_binary += b[-1]  
                total_bytes = [ data_binary[i: i+8] for i in range(0, len(data_binary), 8) ]
                decoded_data = ""
                for byte in total_bytes:
                    decoded_data += chr(int(byte, 2))
                    if decoded_data[-5:] == "*^*^*": 
                        # hien thi kq
                        label = tk.Label(self, text="Ket Qua: ", font=("Arial", 11), bg="lightblue")
                        label.grid(row=2, column=0, columnspan=1, padx=10, pady=10)
                        label = tk.Label(self, text=decoded_data[:-5], font=("Arial", 11), bg="lightblue")
                        label.grid(row=2, column=1, columnspan=3, padx=20, pady=20)

                        #print("\n\nThe Encoded data which was hidden in the Image was :--  ",decoded_data[:-5])
                        return 


import tkinter as tk
from tkinter import filedialog
from binary import *
from matplotlib import pyplot as plt
import cv2
import os

class EncodeComponent(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="lightblue")

        # Tiêu đề
        label = tk.Label(self, text="Encode", font=("Arial", 14), bg="lightblue")
        label.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        # Label và Entry cho văn bản cần giải mã
        lbl_text = tk.Label(self, text="Text to encode:", bg="lightblue")
        lbl_text.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.edit_entry = tk.Entry(self, width=30)
        self.edit_entry.grid(row=1, column=1, pady=5, sticky="we")
        self.edit_entry.grid_columnconfigure(1, weight=1)  # Đảm bảo ô nhập văn bản mở rộng theo chiều ngang

                # Button "Browse File" và Entry "File Path"
        lbl_browser_file = tk.Label(self, text="File Encode:", bg="lightblue")
        lbl_browser_file.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.file_path_entry = tk.Entry(self, width=50)
        self.file_path_entry.grid(row=2, column=1, pady=5, sticky="we")
        self.file_path_entry.grid_columnconfigure(1, weight=1)  # Đảm bảo ô nhập văn bản mở rộng theo chiều ngang
        
        browse_button = tk.Button(self, text="...", command=self.browse_file, width=5)  # Đặt width thành 10 ký tự
        browse_button.grid(row=2, column=2, padx=10, pady=5, sticky="e")

        # Button "Browse Folder Save" và Entry "Folder Path Save"
        lbl_browser_folder = tk.Label(self, text="Folder Path Save:", bg="lightblue")
        lbl_browser_folder.grid(row=3, column=0, padx=10, pady=5, sticky="e")

        self.folder_path_entry_save = tk.Entry(self, width=50)
        self.folder_path_entry_save.grid(row=3, column=1, pady=5, sticky="we")
        self.folder_path_entry_save.grid_columnconfigure(1, weight=1)  # Đảm bảo ô nhập văn bản mở rộng theo chiều ngang

        browse_button_save = tk.Button(self, text="...", command=self.browse_folder,width=5)
        browse_button_save.grid(row=3, column=2, padx=10, pady=5, sticky="e")

        # Label và Entry cho tên ảnh mới
        lbl_txt = tk.Label(self, text="Name New File:", bg="lightblue")
        lbl_txt.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.new_txt = tk.Entry(self, width=30)
        self.new_txt.grid(row=4, column=1, pady=5, sticky="we")

        # Button "Submit"
        submit_button = tk.Button(self, text="Encode", command=self.submit,width=50)
        submit_button.grid(row=5, column=1, padx=10, pady=5, sticky="e")
    def browse_file(self):
        filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        self.file_path_entry.delete(0, tk.END)
        self.file_path_entry.insert(0, filename)

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        self.folder_path_entry_save.delete(0, tk.END)  # Xóa nội dung trong entry trước khi cập nhật
        self.folder_path_entry_save.insert(0, folder_path)  # Thêm đường dẫn thư mục đã chọn vào entry

    def submit(self):
        check = self.encode_txt_data()
        log_success = "----create successful! ----"
        fullname_new_file = self.folder_path_entry_save.get() + "/" + self.new_txt.get()
        if not fullname_new_file.endswith(".txt"):
            fullname_new_file += ".txt"
        if (check != 0) :
            self.log(log_success+fullname_new_file)

    def log(self, message):
            lbl_log = tk.Label(self, text=message, bg="lightblue")
            lbl_log.grid(row=6, column=1, padx=10, pady=5, sticky="e")



    def encode_txt_data(self):
        count2=0
        file1 = open(self.file_path_entry.get(),"r",encoding="utf-8")
        for line in file1: 
            for word in line.split():
                count2=count2+1
        file1.close()       
        bt=int(count2)
        print("Maximum number of words that can be inserted :- ",int(bt/6))
        text1=self.edit_entry.get()
        l=len(text1)
        if(l<=bt):
            print("\nInputed message can be hidden in the cover file\n")
            self.txt_encode(text1)
        else:
            self.log("-----Create Failed!---- String is too big please reduce string size")
            return 0

    def txt_encode(self,text):
        l=len(text)
        i=0
        add=''
        while i<l:
            t=ord(text[i])
            if(t>=32 and t<=64):
                t1=t+48
                t2=t1^170       #170: 10101010
                res = bin(t2)[2:].zfill(8)
                add+="0011"+res
            
            else:
                t1=t-48
                t2=t1^170
                res = bin(t2)[2:].zfill(8)
                add+="0110"+res
            i+=1
        res1=add+"111111111111"
        print("The string after binary conversion appyling all the transformation :- " + (res1))   
        length = len(res1)
        print("Length of binary after conversion:- ",length)
        HM_SK=""
        ZWC={"00":u'\u200C',"01":u'\u202C',"11":u'\u202D',"10":u'\u200E'}      
        file1 = open(self.file_path_entry.get(),"r+")
        nameoffile = self.folder_path_entry_save.get() + "/" + self.new_txt.get()
        if not nameoffile.endswith(".txt"):
            nameoffile += ".txt"
        if os.path.exists(nameoffile):
            # Tên tệp đã tồn tại, thông báo cho người dùng
            self.log("File name already exists. Please choose another name.")
            return 0
        file3= open(nameoffile,"w+", encoding="utf-8")
        word=[]
        for line in file1: 
            word+=line.split()
        i=0
        while(i<len(res1)):  
            s=word[int(i/12)]
            j=0
            x=""
            HM_SK=""
            while(j<12):
                x=res1[j+i]+res1[i+j+1]
                HM_SK+=ZWC[x]
                j+=2
            s1=s+HM_SK
            file3.write(s1)
            file3.write(" ")
            i+=12
        t=int(len(res1)/12)     
        while t<len(word): 
            file3.write(word[t])
            file3.write(" ")
            t+=1
        file3.close()  
        file1.close()
        print("\nStego file has successfully generated")


if __name__ == "__main__":
    root = tk.Tk()
    encode_component = EncodeComponent(root, None)
    encode_component.pack(fill="both", expand=True)
    root.mainloop()
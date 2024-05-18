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
        filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        
        self.file_path_entry.delete(0, tk.END)
        self.file_path_entry.insert(0, filename)
    def submit(self):
        self.decode_txt_data(self.file_path_entry.get())

    def log(self, message):
            lbl_log = tk.Label(self, text=message, bg="lightblue")
            lbl_log.grid(row=2, column=1, sticky="e")

    #-----------------------------    
    def decode_txt_data(self,filename):
        ZWC_reverse={u'\u200C':"00",u'\u202C':"01",u'\u202D':"11",u'\u200E':"10"}
        stego=filename
        file4= open(stego,"r", encoding="utf-8")
        temp=''
        for line in file4: 
            for words in line.split():
                T1=words
                binary_extract=""
                for letter in T1:
                    if(letter in ZWC_reverse):
                        binary_extract+=ZWC_reverse[letter]
                if binary_extract=="111111111111":
                    break
                else:
                    temp+=binary_extract
        print("\nEncrypted message presented in code bits:",temp) 
        lengthd = len(temp)
        print("\nLength of encoded bits:- ",lengthd)
        i=0
        a=0
        b=4
        c=4
        d=12
        final=''
        while i<len(temp):
            t3=temp[a:b]
            a+=12
            b+=12
            i+=12
            t4=temp[c:d]
            c+=12
            d+=12
            if(t3=='0110'):
                decimal_data = binary.BinaryToDecimal(t4)
                final+=chr((decimal_data ^ 170) + 48)
            elif(t3=='0011'):
                decimal_data = binary.BinaryToDecimal(t4)
                final+=chr((decimal_data ^ 170) - 48)
        self.log("\nMessage after decoding from the stego file:- "+final)


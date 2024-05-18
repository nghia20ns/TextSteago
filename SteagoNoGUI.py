import numpy as np
import pandas as pand
import os
import cv2
from matplotlib import pyplot as plt

# Hàm mã hóa văn bản thành chuỗi nhị phân và giấu thông tin
def txt_encode(text):
    l = len(text)  # Lấy độ dài của văn bản
    i = 0
    add = ''
    while i < l:
        t = ord(text[i])  # Lấy mã ASCII của ký tự hiện tại
        if 32 <= t <= 64:  # Nếu mã ASCII nằm trong khoảng 32 đến 64
            t1 = t + 48
            t2 = t1 ^ 170  # XOR với 170 (10101010)
            res = bin(t2)[2:].zfill(8)  # Chuyển sang nhị phân và điền số 0 vào đầu để đủ 8 bit
            add += "0011" + res  # Thêm tiền tố "0011"
        else:
            t1 = t - 48
            t2 = t1 ^ 170  # XOR với 170 (10101010)
            res = bin(t2)[2:].zfill(8)  # Chuyển sang nhị phân và điền số 0 vào đầu để đủ 8 bit
            add += "0110" + res  # Thêm tiền tố "0110"
        i += 1
    res1 = add + "111111111111"  # Thêm chuỗi đánh dấu kết thúc "111111111111"
    print("The string after binary conversion appyling all the transformation :- " + res1)
    length = len(res1)
    print("Length of binary after conversion:- ", length)
    
    HM_SK = ""
    # Bản đồ ký tự Zero-Width
    ZWC = {"00": u'\u200C', "01": u'\u202C', "11": u'\u202D', "10": u'\u200E'}
    file1 = open("cover_text.txt", "r+")
    nameoffile = input("\nEnter the name of the Stego file after Encoding(with extension):- ")
    file3 = open(nameoffile, "w+", encoding="utf-8")
    
    word = []
    for line in file1:
        word += line.split()  # Chia các dòng thành các từ và thêm vào danh sách

    i = 0
    while i < len(res1):
        s = word[int(i / 12)]
        j = 0
        x = ""
        HM_SK = ""
        while j < 12:
            x = res1[j + i] + res1[i + j + 1]  # Lấy 2 bit nhị phân
            HM_SK += ZWC[x]  # Ánh xạ 2 bit nhị phân sang ký tự Zero-Width
            j += 2
        s1 = s + HM_SK  # Ghép từ gốc với ký tự Zero-Width
        file3.write(s1)
        file3.write(" ")
        i += 12
    
    t = int(len(res1) / 12)
    while t < len(word):
        file3.write(word[t])
        file3.write(" ")
        t += 1
    
    file3.close()
    file1.close()
    print("\nStego file has successfully generated")

# Hàm kiểm tra khả năng mã hóa và thực hiện mã hóa
def encode_txt_data():
    count2 = 0
    file1 = open("cover_text.txt", "r")
    for line in file1:
        for word in line.split():
            count2 += 1  # Đếm số lượng từ trong văn bản gốc
    file1.close()
    bt = int(count2)
    print("Maximum number of words that can be inserted :- ", int(bt / 6))
    text1 = input("\nEnter data to be encoded:- ")
    l = len(text1)
    if l <= bt:
        print("\nInputed message can be hidden in the cover file\n")
        txt_encode(text1)  # Mã hóa văn bản
    else:
        print("\nString is too big please reduce string size")
        encode_txt_data()  # Yêu cầu người dùng nhập lại nếu văn bản quá lớn

# Hàm chuyển đổi từ nhị phân sang thập phân
def BinaryToDecimal(binary):
    string = int(binary, 2)  # Chuyển chuỗi nhị phân sang số thập phân
    return string

# Hàm giải mã thông tin từ văn bản "Stego"
def decode_txt_data():
    ZWC_reverse = {u'\u200C': "00", u'\u202C': "01", u'\u202D': "11", u'\u200E': "10"}  # Bản đồ ngược của Zero-Width
    stego = input("\nPlease enter the stego file name(with extension) to decode the message:- ")
    file4 = open(stego, "r", encoding="utf-8")
    temp = ''
    for line in file4:
        for words in line.split():
            T1 = words
            binary_extract = ""
            for letter in T1:
                if letter in ZWC_reverse:
                    binary_extract += ZWC_reverse[letter]  # Trích xuất các bit nhị phân từ ký tự Zero-Width
            if binary_extract == "111111111111":
                break
            else:
                temp += binary_extract
    print("\nEncrypted message presented in code bits:", temp)
    lengthd = len(temp)
    print("\nLength of encoded bits:- ", lengthd)
    
    i = 0
    a = 0
    b = 4
    c = 4
    d = 12
    final = ''
    while i < len(temp):
        t3 = temp[a:b]
        a += 12
        b += 12
        i += 12
        t4 = temp[c:d]
        c += 12
        d += 12
        if t3 == '0110':
            decimal_data = BinaryToDecimal(t4)
            final += chr((decimal_data ^ 170) + 48)  # Chuyển đổi nhị phân về ký tự ASCII gốc
        elif t3 == '0011':
            decimal_data = BinaryToDecimal(t4)
            final += chr((decimal_data ^ 170) - 48)
    print("\nMessage after decoding from the stego file:- ", final)

# Giao diện người dùng chính cho chương trình Steganography
def txt_steg():
    while True:
        print("\n\t\tTEXT STEGANOGRAPHY OPERATIONS")
        print("1. Encode the Text message")
        print("2. Decode the Text message")
        print("3. Exit")
        choice1 = int(input("Enter the Choice:"))
        if choice1 == 1:
            encode_txt_data()  # Gọi hàm mã hóa
        elif choice1 == 2:
            decrypted = decode_txt_data()  # Gọi hàm giải mã
        elif choice1 == 3:
            break  # Thoát chương trình
        else:
            print("Incorrect Choice")
        print("\n")

# Hàm chính để chạy chương trình
def main():
    print("\t\t      STEGANOGRAPHY")
    txt_steg()  # Gọi giao diện người dùng chính

if __name__ == "__main__":
    main()  # Chạy chương trình nếu đây là file chính

import os

# Hàm mã hóa văn bản thành chuỗi nhị phân và giấu thông tin
def txt_encode(text, key):
    l = len(text)
    i = 0
    add = ''
    while i < l:
        t = ord(text[i])
        if 32 <= t <= 64:
            t1 = t + 48
            t2 = t1 ^ key
            res = bin(t2)[2:].zfill(8)
            add += "0011" + res
        else:
            t1 = t - 48
            t2 = t1 ^ key
            res = bin(t2)[2:].zfill(8)
            add += "0110" + res
        i += 1
    res1 = add + "111111111111"
    print("The string after binary conversion appyling all the transformation :- " + res1)
    length = len(res1)
    print("Length of binary after conversion:- ", length)
    HM_SK = ""
    ZWC = {"00": u'\u200C', "01": u'\u202C', "11": u'\u202D', "10": u'\u200E'}
    file1 = open("cover_text.txt", "r+")
    nameoffile = input("\nEnter the name of the Stego file after Encoding(with extension):- ")
    file3 = open(nameoffile, "w+", encoding="utf-8")
    word = []
    for line in file1:
        word += line.split()
    i = 0
    while i < len(res1):
        s = word[int(i / 12)]
        j = 0
        x = ""
        HM_SK = ""
        while j < 12 and i + j < len(res1):
            x = res1[j + i] + res1[i + j + 1]
            HM_SK += ZWC[x]
            j += 2
        s1 = s + HM_SK
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
            count2 += 1
    file1.close()
    bt = int(count2)
    print("Maximum number of words that can be inserted :- ", int(bt / 6))
    text1 = input("\nEnter data to be encoded:- ")
    key = int(input("Enter the encryption key: "))
    l = len(text1)
    if l <= bt:
        print("\nInputed message can be hidden in the cover file\n")
        txt_encode(text1, key)
    else:
        print("\nString is too big please reduce string size")
        encode_txt_data()

# Hàm chuyển đổi từ nhị phân sang thập phân
def BinaryToDecimal(binary):
    string = int(binary, 2)
    return string

# Hàm giải mã thông tin từ văn bản "Stego"
def decode_txt_data():
    ZWC_reverse = {u'\u200C': "00", u'\u202C': "01", u'\u202D': "11", u'\u200E': "10"}
    stego = input("\nPlease enter the stego file name(with extension) to decode the message:- ")
    key = int(input("\n Please enter key -:"))
    file4 = open(stego, "r", encoding="utf-8")
    temp = ''
    for line in file4:
        for words in line.split():
            T1 = words
            binary_extract = ""
            for letter in T1:
                if letter in ZWC_reverse:
                    binary_extract += ZWC_reverse[letter]
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
            final += chr((decimal_data ^ key) + 48)
        elif t3 == '0011':
            decimal_data = BinaryToDecimal(t4)
            final += chr((decimal_data ^ key) - 48)
    
    # Ghi kết quả vào một tệp văn bản mới
    with open("decoded_message.txt", "w", encoding="utf-8") as output_file:
        output_file.write(final)
    print("\nMessage after decoding from the stego file has been saved in 'decoded_message.txt'")

# Giao diện người dùng chính cho chương trình Steganography
def txt_steg():
    while True:
        print("\n\t\tTEXT STEGANOGRAPHY OPERATIONS")
        print("1. Encode the Text message")
        print("2. Decode the Text message")
        print("3. Exit")
        choice1 = int(input("Enter the Choice:"))
        if choice1 == 1:
            encode_txt_data()
        elif choice1 == 2:
            decrypted = decode_txt_data()
        elif choice1 == 3:
            break
        else:
            print("Incorrect Choice")
        print("\n")

# Hàm chính để chạy chương trình
def main():
    print("\t\t      STEGANOGRAPHY")
    txt_steg()

if __name__ == "__main__":
    main()

# đọc 1 file văn bản gồm nhiều dòng
# ghi ra mà hình thứ tự ngược lại của các dòng
import sys


file_path = "test.txt"
with open(file_path, "r") as file:
    
    lines = file.readlines()

for line in reversed(lines):
    print(line.strip())

file.close()


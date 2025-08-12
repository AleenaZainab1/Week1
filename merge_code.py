# merge_code.py
# Ye code file1.txt aur file2.txt ko merge karega

# File1 ka content lena
with open("file1.txt", "r", encoding="utf-8") as f1:
    data1 = f1.read()

# File2 ka content lena
with open("file2.txt", "r", encoding="utf-8") as f2:
    data2 = f2.read()

# Dono ka content merged.txt me likhna
with open("merged.txt", "w", encoding="utf-8") as mf:
    mf.write(data1 + "\n" + data2)

print("✅ Files are merged-> merged.txt")

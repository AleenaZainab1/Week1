import os     # files check karne ke liye
import sys    # command line arguments lene ke liye

#  Part 1: List .py files & sizes 
print("Python files in this folder:\n")
for file in os.listdir():         # folder ke saare files ka naam lena
    if file.endswith(".py"):      # agar file ka naam .py par end hota hai
        size = os.path.getsize(file)  # file ka size lena
        print(file, "-", size, "bytes")

print("\n------------------\n")

#  Part 2: Read filename from argv 
# argv[0] = program ka naam hota hai
# argv[1] = jo filename tum run time par doge
if len(sys.argv) > 1:
    fname = sys.argv[1]
    print("Filename from argument:", fname)

    # file exist hai ya nahi check karo
    if os.path.exists(fname):
        f = open(fname, "r")      # file read mode me open karo
        data = f.read()           # pura content read karo
        f.close()
        print("\nFile content:\n", data)
    else:
        print("File not found.")
else:
    print("No filename given.")

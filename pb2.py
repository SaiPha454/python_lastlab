import os.path
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

filename = input("Enter a filename : ")
old_string = input("The old string to be replaced : ")
new_string = input("Enter a new string : ")

try:
    if not os.path.isfile(filename) :
        raise IOError(f"File : {filename} not exist!")

    if old_string == new_string :
        raise RuntimeError("The old and new string are the same")
    open_file = open(filename, "r")
    contents = ""
    for line in open_file.readlines() :
        new_str = line.replace(old_string, new_string)
        contents += new_str
    open_file.close()
    print(contents)
    save_file = open(filename, "w")
    save_file.write(contents)
    save_file.close()

except IOError as err :
    print("Error : ", err)
except RuntimeError as err:
    print("Get runtime error : ", err)

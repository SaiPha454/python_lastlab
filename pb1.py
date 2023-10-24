import os.path
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

phonebook = {}
while True : 

    print("Press + to add a new contact.")
    print("Press - to delete a contact.")
    print("Press f to find a contact")
    print("Press p to print out all contacts in the phonebook.", end= " : ")
    char = input()

    if char == "+" :
        name = input("Enter name : ")
        no = input("Enter phone number : ")

        try:
            for i in name :
                if i.isalpha() == False :
                    raise RuntimeError("Name must be alphabet!")
            phonebook[name] = no
        except RuntimeError as ex:
            print("Contact input error : ", ex)
        
    elif char == "-" :
        name = input("Enter name that you want to delete : ")
        if not name in phonebook :
            print("No ", name)
            continue
        del phonebook[name]
    elif char == "f" :
        name = input("Find a contact : ")
        if name in phonebook :

            print("Name : ", name)
            print("Contact : ", phonebook[name])
        else : 
            print("No such contact")
    elif char == "p" :
        print("\n\n")
        print("======================= Contacts =========================")
        for i in phonebook :
            print("Name : ", i, " , contact : ", phonebook[i])
        
        print("\n\\n")
    elif char == "q" :
        break
    elif char == "s" :
        
        try :

            save_filename = asksaveasfilename()

            if os.path.isfile(save_filename) :
                raise IOError("File already exist")
            save_file = open(save_filename, "w")
            for c in phonebook:
                
                contact = str(c) + "," + str(phonebook[c]) + "\n"
                save_file.write(contact)
            save_file.close()
            
        except IOError as ex:
            print("Error : ", ex)
    
    elif char == "l" :
        
        try :

            open_filename = askopenfilename()
            open_file = open(open_filename, "r")
            
            for line in open_file.readlines() :
                [person, contact ] = line.split(",")
                print(person, " => ", contact, end="")
            open_file.close()
            
        except IOError as ex:
            print("Error : ", ex)



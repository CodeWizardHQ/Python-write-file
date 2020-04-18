import os

#Define file extension. Append this to the name entered by user
file_format='.txt'

print("Hello, welcome")

file_name=input('Plese enter a file name to proceed. Please note that if the file does not exist we shall proceed to create a file with new content: ')
#List=[]

try:
    file = open(file_name+file_format)
except IOError:
    print(file_name, " FILE DOES NOT EXIST")
    
    file = open(file_name+file_format, 'w')
    
    info=input("PLEASE ENTER INFORMATION: ")
    #List.append(info)
    file.write(str(info))
    file.write('\n')

    file.close()
    print(file_name, " FILE HAS BEEN CREATED")

else:
    print(file_name, " FILE HAS BEEN FOUND")
    
    #Put potetial user actions in a reusable function
    def ask(file):
        #global file
        print("What do you want to do with the file Read/Delete/Append to the file: ")
        print("A. Read the file")
        print("B. Delete the file")
        print("C. Append to the file")
        print("D. Change a line in the file")
        print("E. Quit")
        choice=input("TYPE HERE: ")

        #Read the file
        if choice == "A" or choice == 'a':
            file=open(file_name+file_format, 'r')
            content=file.read()
            print("FILE CONTENT")
            print("------------")
            print(content)
            file.close()
            ask(file)
            

        #Delete the file
        elif choice == "B" or choice == 'b':
            
            file.close()
            os.remove(file_name+file_format)
            print(file_name, "FILE HAS BEEN DELETED")

        #Append to the file
        elif choice == "C" or choice == 'c':
            file=open(file_name+file_format, 'a')
            info2=input("What do you want to append to the file: ")
            file.write(str(info2))
            file.write('\n')
            file.close()
            print(info2, " has been appended")
            ask(file)

        #Change a line in the file
        elif choice == "D" or choice == 'd':
            f1 = open(file_name+file_format, 'r+')

            file=f1.readlines()
            print(len(file))
            line=input("Enter line number: ")
            try:
                int(line)
            except ValueError:
                print("ERROR: Enter a number not a string")
                print('\n')
                ask(file)

            #Check the input against the length of the list 
            if int(line) > len(file):
                print('Line does not exist')
                ask(file)

            line=int(line)
            
            new_line=(line-1)
            new_input=input("Enter new string: ")
            
            file2=str(file).strip('[]')
            file[new_line] = file[new_line].replace('\n', '\\n')
            x = file2.replace(file[new_line], new_input).split(", ")
            new_list=[]
            
            for element in x:
                mun=element.replace('\\n', '')
            with open(file_name+file_format, 'w', -1, 'utf-8') as new_file:
                for element in x:
                    mun=element.replace('\\n', '')
                    num=mun.strip("'")
                    new_file.writelines(str(num))
                    new_file.write('\n')
            f1.close()
            ask(file)

        #Kill and exit the programme
        elif choice == "E" or choice == 'e':
            exit()
    ask(file)

#WELCOME TO THE BEST CLI BASED FILE MANAGER
import time
import os
import pickle
import csv


#PRINT WITH TYPING
def Print(a):
    for i in str(a):
        print(i,end='',flush=True)
        time.sleep(0.01)


#ASK TO CONTINUE
def ask_continue():
    Print("Do you want to continue ? (Yes/No)")
    print('\n')
    Print("Input: ")
    ask=input()
    if ask.lower()=='yes':
        return True
    elif ask.lower()=='no':
        return False
    else:
        Print("Invalid input")
    print('\n')
    

#LIST OF ALL FILES
def list_files():
    cwd=os.getcwd()
    files=os.listdir(cwd)
    c=0
    for i in files:
        if os.path.isfile(os.path.join(cwd, i)):
            c+=1
    if c==0:
        Print("No files available")
    else:
        print('\n')
        Print("Available files: ")
        print('\n')
        for i in files:
            if os.path.isfile(os.path.join(cwd, i)):
                Print(f"{i}")
                print('\n')
        print('\n')
        Print("Number of files: ")
        Print(c)
    print('\n')


#CREATE FILE
def create_file():
    Print("Enter the name of the file you want to create: ")
    name=input()
    print('\n')
    Print('''Enter the extension (type) of file:
          Write *.txt* for text file
          *.dat* for Binary File
          *.csv* for CSV file
          
          Your input: ''')
    extn=input()
    if extn in [".csv",".dat",".txt"]:
        file=name+extn
        print('\n')
        if os.path.exists(file):
            Print(f"File {file} already exists. Please enter a different name or extension")
            print('\n')
        else:
            if file[-4:]=='.csv' or file[-4:]=='.txt':
                F=open(file,'w')
                Print(f"File {file} successfuly created")
            elif file[-4:]=='.dat':
                F=open(file,'wb')
                Print(f"File {file} successfuly created")
            else:
                Print("Some error occured. Please try again.. If the issue still persists, please validate your input")
            F.close()
            print('\n')
    else:
        Print("Invalid input. Please enter correct file extension.")    
        print('\n')
    
    
#RENAME FILE
def rename_file():
    Print("Enter the name of the file you want to rename: ")
    name=input()
    print('\n')
    if os.path.exists(name):
        Print("Enter the new name of the file: ")
        Name=input()
        file=Name+str(name[-4:])
        print('\n')
        try:
            os.rename(name,file)
            Print(f"File renamed from {name} to {file} succesfully")
            print('\n')
        except Exception as e:
            Print("Some error occured.. Details as follows: ")
            print('\n')
            Print(Exception)
    else:
        Print(f"File {name} does not exist.. Please check your input")
        print('\n')


#WRITE IN FILE
def write_file():
    Print("Enter the name of the file you want to write information in: ")
    name=input()
    print('\n')
    if os.path.exists(name):
        Print(f"File {name} loaded successfully")
        print('\n')
        if name[-4:]=='.txt':
            Print("Enter the type of information you want to enter.. (String/List/Tuple): ")
            F=open(name,'a')
            IN1=input()
            print('\n')
            if IN1.lower()=='string':
                Print('''Enter the string: ''')
                print('\n')
                IN=input()
                print('\n')
                F.write(IN)
                F.write('\n')
                F.flush()
                F.close()
                Print("Content added successfully")
            elif IN1.lower()=='list':
                Print("Enter the length of list: ")
                IN=int(input())
                L=[]
                print('\n')
                for i in range(IN):
                    Print("Enter the element: ")
                    ele=eval(input())
                    L.append(ele)
                F.write(str(L))
                F.write('\n')
                print('\n')
                F.flush()
                F.close()
                Print("Content added successfully")
            elif IN1.lower()=='tuple':
                Print("Enter the length of tuple: ")
                IN=int(input())
                T=()
                print('\n')
                for i in range(IN):
                    Print("Enter the element: ")
                    ele=eval(input())
                    T+=(ele,)
                F.write(str(T))
                F.write('\n')
                F.flush()
                F.close()
                Print("Content added successfully")
            else:
                Print("Invalid input")
        elif name[-4:]=='.dat':
            Print("Enter the type of information you want to enter (String/List/Tuple)")
            IN1=input()
            F=open(name,'ab')
            print('\n')
            if IN1.lower()=='string':
                Print("Enter the string: ")
                print('\n')
                IN=input()
                pickle.dump(IN,F)
                pickle.dump('\n',F)
                F.flush()
                F.close()
                Print("Content added successfully")
            elif IN1.lower()=='list':
                Print("Enter the length of list: ")
                IN=int(input())
                L=[]
                print('\n')
                for i in range(IN):
                    Print("Enter the element ")
                    ele=eval(input())
                    L.append(ele)
                pickle.dump(L,F)
                pickle.dump('\n',F)
                F.flush()
                F.close()
                Print("Content added successfully")
            elif IN1.lower()=='tuple':
                Print("Enter the length of tuple: ")
                IN=int(input())
                T=()
                print('\n')
                for i in range(IN):
                    Print("Enter the element: ")
                    ele=eval(input())
                    T+=(ele,)
                pickle.dump(T,F)
                pickle.dump('\n',F)
                F.flush()
                F.close()
                Print("Content added successfully")
            else:
                Print("Invalid input")
        elif name[-4:]=='.csv':
            Print("Enter the type of information you want to enter (String/List/Tuple)")
            IN1=input()
            F=open(name,'a')
            W=csv.writer(F)
            print('\n')
            if IN1.lower()=='string':
                Print("Enter the string: ")
                print('\n')
                IN=input()
                W.writerow(IN)
                F.flush()
                F.close()
                Print("Content added successfully")
            elif IN1.lower()=='list':
                Print("Enter the length of list: ")
                IN=int(input())
                L=[]
                print('\n')
                for i in range(IN):
                    Print("Enter the element: ")
                    ele=eval(input())
                    L.append(ele)
                W.writerow(L)
                F.flush()
                F.close()
                Print("Content added successfully")
            elif IN1.lower()=='tuple':
                Print("Enter the length of tuple: ")
                IN=int(input())
                T=()
                print('\n')
                for i in range(IN):
                    Print("Enter the element: ")
                    ele=eval(input())
                    T+=(ele,)
                W.writerow(T)
                F.flush()
                F.close()
                Print("Content added successfully")
            else:
                Print("Invalid input")
    else:
        Print(f"File {name} does not exist.. Please check your input.")
    print('\n')


#VIEW FILE
def view_file():
    Print("Enter the name of the file you want to view: ")
    name=input()
    print('\n')
    if os.path.exists(name):
        if name[-4:]=='.txt':
            F=open(name,'r')
            F.seek(0)
            L=F.read()
            if L:
                Print(L)
            else:
                Print("Empty file")
            F.close()
            print('\n')
        elif name[-4:]=='.dat':
            F=open(name,'rb')
            F.seek(0,2)
            if F.tell()==0:
                Print("Empty file")
                print('\n')
            else:
                F.seek(0)
                if F: 
                    try:
                        while True:
                            L=pickle.load(F)
                            Print(L)
                    except EOFError:
                        pass
            F.close()     
            print('\n')
        elif name[-4:]=='.csv':
            F=open(name,'r')
            F.seek(0)
            R=csv.reader(F)
            for i in R:
                Print(i)
            else:
                Print("Empty file")  
            F.close()          
    else:
        Print(f"File {name} does not exist.. Please check your input")
        print('\n')    
    

#EMPTY FILE
def empty():
    Print("Enter the name of the file you want to empty (erase the content): ")
    name=input()
    print('\n')
    if os.path.exists(name):
        if name[-4:]=='.dat':
            F=open(name,'rb')
            F.seek(0)
            c=0
            L=pickle.load(F)
            while L:
                try:
                    L=pickle.load(F)
                    c+=len(str(L))
                except EOFError:
                    pass                
            F.close()
            F=open(name,'wb')
            F.close()
            Print("File content erased successfully")
            print('\n')
            Print(f"Erased {c} character(s)")
        elif name[-4:]=='.txt':
            F=open(name,'r')
            F.seek(0)
            L=F.read()
            F.close()
            F=open(name,'w')
            F.close()
            Print("File content erased successfully")
            print('\n')
            Print(f"Erased {len(L)} character(s)")
        elif name[-4:]=='.csv':
            F=open(name,'r')
            F.seek(0)
            R=csv.reader(F)
            c=len(str(list(R)))
            F.close()
            F=open(name,'w')
            F.close()
            Print("File content erased successfully")
            print('\n')
            Print(f"Erased {c} character(s)")
    else:
        Print(f"File {name} does not exist... Please check your input.")
    print('\n')
    
        
#DELETE FILE
def del_file():
    Print("Enter the name of the file you want to delete: ")
    name=input()
    try:
        os.remove(name)
        Print(f"File with name {name} successfully deleted")
        print('\n')
    except FileNotFoundError:
        Print(f"File with name {name} does not exist. Please enter a valid name and try again..")
        print('\n')


#MAIN PROGRAM
y=True
Print('''Welcome to the Main Menu.. 
        1. Show all files available
        2. Create a new file
        3. Rename a file
        4. Write information in a file
        5. View all contents of file
        6. Empty file
        7. Delete a file
        8. Delete os (Not Recommended)
        9. Exit.  ''')       
        
while y:
    print('\n')
    Print('''Please enter your choice for the menu: ''')
    try:
        IN=int(input())
        if IN==1:
            Print("You have selected *Show all Files* Option")
            print('\n')
            list_files()
            print('\n')
            y=ask_continue()
        elif IN==2:
            Print("You have selected *Create a new File* option:")
            print('\n')
            create_file()
            print('\n')
            y=ask_continue()
        elif IN==3:
            Print("You have selected *Rename a File* option")
            print('\n')
            rename_file()
            print('\n')
            y=ask_continue()
        elif IN==4:
            Print("You have selected *Write in File* option:")
            print('\n')
            write_file()
            print('\n')
            y=ask_continue()
        elif IN==5:
            Print("You have selected *View File* option")
            print('\n')
            view_file()
            print('\n')
            y=ask_continue()
        elif IN==6:
            Print("You have selected *Empty File* option")
            print('\n')
            empty()
            print('\n')
            y=ask_continue()
        elif IN==7:
            Print("You have selected *Delete File* option")
            print('\n')
            del_file()
            print('\n')
            y=ask_continue()
        elif IN==8:
            Print("You have selected *Delete OS* option")
            print('\n')
            time.sleep(2)
            Print("Nuh uh.. Not today..")
            time.sleep(2)
            print('\n')
            Print("WAIT.... SOMETHING IS HAPPENING")
            print('\n')
            time.sleep(2)
            Print("NaHBrO.. LOL")
            break
        elif IN==9:
            Print("Thank you.. Session terminated")
            break
        else:
            Print("Invalid input")
            break
    except ValueError:
        Print("Please enter a valid option")

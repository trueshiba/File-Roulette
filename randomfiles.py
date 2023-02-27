#Cooper Sullivan
#CS 021 - Intro To Python
#randomfiles.py will prompt for admin privledges and then allow a user to enter an int so it can go through random directories starting at the root in search of a random file to then display its name and size in bytes for the user
import os, random, ctypes, sys

#random_file() intakes a starting path (the root directory) and then continuously chooses random directories (goes 1 layer deeper each run through) until it comes across a file and returns its path.
def random_file(pathdir):
    origindir = pathdir

    while os.path.isdir(pathdir) == True: 
        try:
            name = random.choice(os.listdir(pathdir))
            pathdir = os.path.join(pathdir,name)
        except:
            pathdir = origindir # if directory has no files // is a dead end: resets pathdir to the starting directory to start a new rand file search from beginning

    return pathdir
    
#list_files() intakes the number of files that the user wants to discover before calling random_file() and appending the result to the filelist. It repeats this for num times and prints out the formatted info about each file.
def list_files(num):
    filelist = []

    for x in range(num):
        filelist.append(random_file("C:/"))# <-------------------------- CHANGE IF COMPUTER UTILIZES DIFFERENT BASE DIRECTORY --------------------------
        fsize = os.path.getsize(str(filelist[x]))
        fname = os.path.basename(str(filelist[x]))
        print (f"{x}] {fname} with size of {fsize} Bytes")

# ///////////////////////// PREFACE: THESE ARE NOT MY ORIGINAL FUNCTIONS. THEY WERE ORIGINALLY WRITTEN BY 'MARTIN DE LA FUENTE' ON STACK OVEFFLOW ///////////////////////// #
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def rerun():
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
# ////////////////////////////////////////////////////// I DO NOT DOCUMENT THEM BECAUSE I DON'T FULLY UNDERSTAND THEM ////////////////////////////////////////////////////// #

def main():   
    numfiles = "initialize"

    if is_admin():
        blank = input("Please close this window")
    else:
        rerun()
    
    while numfiles.isdigit() == False:
        choice = input("How many files do you want to discover? (This must be an integer >/= 0)\n")
        try:
            numfiles = int(choice)
        except:
            print(f"That was a {type(choice)} not an int")
        
        numfiles = str(choice)

    list_files(int(numfiles))

main()
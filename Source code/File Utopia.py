#FileUtopia is a silent file manager that works in the background to arrange your files in Downloads folder
#according to their extensions. For example, all image files will be automatically be moved to the Pictures folder
#in Library section. Similar for video files, they will be automatically moved to the Videos folder in library
#section.
#Feel free to edit the code, just dont forget to give credit. Open Source all the Way !!
#Coded by Muhammad Khizar Khan.
# Email: khizer.khan1899@protonmail.com  |  Instagram: @khizarcodes  |  Github: github.com/khizarcodes  |  DEV.TO: dev.to/khizarcodes

import os
import shutil
import time

path_of_script = os.path.realpath(__file__)
dir_of_script = os.path.dirname(str(path_of_script))
#Hardcoding the main directory for all future refferences as middle point, for further navigation.
main_dir = dir_of_script #Remember to chdir(main_dir) in the end of every function definition that changes directories for internal reasons.
os.chdir(str(main_dir))
#creating a folder 'app_data' and moving extension files to it.
path_of_app_data = dir_of_script + str("\\app_data")

if os.path.isdir(path_of_app_data) == False:
    os.mkdir(path_of_app_data)
    shutil.move(dir_of_script+"\\audio_extensions.txt",path_of_app_data)
    shutil.move(dir_of_script+"\\video_extensions.txt",path_of_app_data)
    shutil.move(dir_of_script+"\\picture_extensions.txt",path_of_app_data)
    shutil.move(dir_of_script+"\\document_extensions.txt",path_of_app_data)
elif os.path.isdir(path_of_app_data) == True:
    pass


def df_init():
    #df_init checks if the user is using the application for the first time or not. If not,
    #it prompts user to enter the path to the downloads folder. Else, it try's to open the text file
    #containing the path to the users entered downloads folder.

    #os.chdir("..") #changing the directory to one step up from the current working directory.
    directory_to_work_with = str(os.getcwd()+"\\app_data") #this is the directory in which the file containing path files should exist.

    file_presence = False #Flag to identify the presence of path file in the directory

    try:
        f = open(directory_to_work_with+"\\df_path.txt","r")
        #this part of code tries to open the file containing the path. If the file opens, it sets the file_presence flag to True, indicating that file is present and the user has entered his download folder path before.
        file_presence = True #set the flag to True
        f.close()
    except:
        file_presence = False #indicating file not found. Now proceed to prompt the user to enter the path to download folder.

    if file_presence == False:
        #Taking input from user for path. Also verifying if the path is True or not. Won't execute if file is already found.

        #Also note that the path_verify function will be called to verify the entered path.
        print("Enter the path to Downloads folder (ex. C:\\Users\\XYZ\\Downloads). This is only needed once. \n")
        usr_input = str(input())
        
        flag = False
        while flag == False:

            if directory_verify(usr_input)==True:
                flag = True
            else:
                flag = False
                print("The PATH you entered doesn't exist. Re-enter the path to Downloads folder. \n")
                usr_input = str(input())

        download_folder_location = str(usr_input)
        #Writing the path to the text file in the app_data folder in src directory
        with open(directory_to_work_with+"\\df_path.txt","w") as f:
            f.write(download_folder_location)
    os.chdir(main_dir)
    #End of df_init function


def lf_init():
    #lf_init() initialises the path to Library folders PICTURES, VIDEOS, MUSIC and DOCUMENTS.
    #It reads from the path specified in the df_path.txt file and works on that to get the path of other library
    #folders.

    #os.chdir("..")
    df_path = open(str(os.getcwd())+"\\app_data\\df_path.txt","r")
    path2 = df_path.read() #path of Downloads folder i.e df_path
    df_path.close()

    libraries = ['Pictures','Videos','Documents','Music']
    path1 = str(os.getcwd()) #path of src folder, the parent of main.

    for lib_folder in libraries:

        os.chdir(str(path2)) #changing directory to the Downloads folder of the user, in the library.
        os.chdir("..") #changing directory to the parent of Download folder.
        path3 = str(os.getcwd()) + "\\" + str(lib_folder) #path to the Pictures/Videos/Music/Documents folder based on the element of the libraries.

        file_presence = False

        try: #checking if the file already exists. If it exists, set the presence flag to True.
            fr = open(path1 + "\\app_data\\lf_path.txt","r")
            file_presence = True
            fr.close()
        except: #if it doesn't exist, set the flag to False.
            file_presence = False
            
        if file_presence == True:
            
            fa = open(path1 + "\\app_data\\lf_path.txt","a") #tries to append after checking that the file exists.
            fa.write(str(path3))
            fa.write("\n")
            fa.close()

        elif file_presence == False:
            
            fw = open(path1 + "\\app_data\\lf_path.txt","w") #if it doesn't exist, it creates it and writes the path to it. Next time, the try statement will be met and executed as the file now exists.
            fw.write(str(path3))
            fw.write("\n")
            fw.close()

    os.chdir(main_dir)    
    #end of lf_init() function.

def directory_verify(path):
    #directory_verify() checks wheather the path exists or not. If it exists, it return True, else False.
    truth_flag = False
    try:
        #tries to change the directory to the one passed as argument. If the operation is successfull, it sets the truth_flag to True.
        os.chdir(str(path))
        truth_flag = True
    except:
        #Else if it is unable to change the directory, it sets the truth_flag to False.
        truth_flag = False
    #finally it returns the truth_flag.
    return truth_flag

    os.chdir(main_dir)
    #end of directory_verify function


def detect_and_move():
    #detect_and_move() detects the file extension of all file in the downloads folder directory, and hen decides on where to move the detected file based on their extension.

    #reading the df_path.txt for download folder path
    #os.chdir("..")
    with open(str(os.getcwd())+"\\app_data\\df_path.txt","r") as df:
        df_path = df.read() #df_path is the path of the download folder.

    #reading audio_extensions.txt and placing extensions in a list.
    with open(str(os.getcwd())+"\\app_data\\audio_extensions.txt","r") as ax:
        extensions = ax.read()
        audio_extensions = extensions.split("\n")

    #reading video_extensions.txt and placing extensions in a list.        
    with open(str(os.getcwd())+"\\app_data\\video_extensions.txt","r") as vx:
        extensions = vx.read()
        video_extensions = extensions.split("\n")

    #reading document_extensions.txt and placing extensions in a list.
    with open(str(os.getcwd())+"\\app_data\\document_extensions.txt","r") as dx:
        extensions = dx.read()
        document_extensions = extensions.split("\n")

    #reading picture_extensions.txt and placing extensions in a list.    
    with open(str(os.getcwd())+"\\app_data\\picture_extensions.txt","r") as px:
        extensions = px.read()
        picture_extensions = extensions.split("\n")
    
    #reading the lf_path.txt for library folder paths
    with open(str(os.getcwd())+"\\app_data\\lf_path.txt","r") as lf:
        lf_paths = lf.read() #lf_paths are the library folder paths.
    
    lf_list = lf_paths.split("\n") #lf_list in the list of library folder paths obtained by spliting the lf_paths variable for "\n". Now we have a list that can be iterated in any way desired for any library folder path required.
    #the order of lf_list is the same as the order in which the library folders were written into the text file in lf_init() function.
    #the order is : Pictures, Videos, Documents, Music
    #the order can be changed if desired.
    #just change the list 'libraries' in lf_init() function to the order of desire, and the library folders will be written in the same order.
    #remember the order is very important.
    #due to the current order, if a statement lf_list[2] is executed for example, the output will be 'Documents' folder path.

    df_contents = [] #this is list that will contain the contents of the download folder after the scanning is performed.

    with os.scandir(df_path) as src:
        #os.scandir(df_path) scans the downlaod folder path and returns a list of contents encountered.
        #by iterating throught the returned list of contents, we check if the contents are files by item.is_file().
        #the output of is_file() is in BOOLEAN format. If it is a file, we append the file in the df_content list.
        for item in src:
            if item.is_file():
                df_contents.append(item)

    for content in df_contents:
        #iterating through contents in df_contents list, we split the file into file names and file extensions.
        #os.path.splitext(content) splits the content into name and extension. extension is of interest.
        content_name , content_extension = os.path.splitext(content)
        #content_extension contains the extension of the detected content.
        extension_identifier = ''
        detected_extension = content_extension

        for ext in picture_extensions:
            #testing each extension in picture_extensions against detected_extension.
            if detected_extension == ext or detected_extension == str(ext).upper():
                extension_identifier = 'Picture'

        for ext in video_extensions:
            #testing each extension in video_extensions against detected_extension.
            if detected_extension == ext or detected_extension == str(ext).upper():
                extension_identifier = 'Video'
        
        for ext in document_extensions:
            #testing each extension in document_extensions against detected_extension.
            if detected_extension == ext or detected_extension == str(ext).upper():
                extension_identifier = 'Document'

        for ext in audio_extensions:
            #testing each extension in audio_extensions against detected_extension.
            if detected_extension == ext or detected_extension == str(ext).upper():
                extension_identifier = 'Music'
        
        #performing moving of files based on the extension_identifier value
        #lf_list order is kept in mind. 0 for picture, 1 for video, 2 for document and 3 for music.
        if extension_identifier == 'Picture':
            print("Moving ",str(content_name))
            shutil.move(str(content_name)+str(content_extension),lf_list[0])
        elif extension_identifier == 'Video':
            print("Moving ",str(content_name))
            shutil.move(str(content_name)+str(content_extension),lf_list[1])
        elif extension_identifier == 'Document':
            print("Moving ",str(content_name))
            shutil.move(str(content_name)+str(content_extension),lf_list[2])
        elif extension_identifier == 'Music':
            print("Moving ",str(content_name))
            shutil.move(str(content_name)+str(content_extension),lf_list[3])
    
    os.chdir(main_dir)

    #end of detect_and_move()
    

print("File Utopia Tester Preview v1.0.")
print("Program will automatically detect and move files from your download folder so that it doesn't get cluttered.")
print("\nRunning now...")
df_init()
time.sleep(2)
lf_init()
time.sleep(2)
while True:
    detect_and_move()

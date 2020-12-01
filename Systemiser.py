from pathlib import Path
from pathlib import Path
import shutil, os



if __name__ == "__main__":
   #Asking user prompt for pursuing the task
   if(int(input("Enter 1 to continue: "))==1):
      #identifing current working path
      current_path = os.getcwd()

      #providing destination path
      destination_path = "D:/Systemised files/"

      #identifing the types of files in the current working directory
      basepath = Path(current_path)
      files_in_basepath = basepath.iterdir()

      #dictionaries datatype for storing file types and adding files corresponding to the file types
      #file_dict["File_type"]=[list of corresponding files]   
      file_dict = {}

      #Extracting file types and files and storing it in file_dict   
      for item in files_in_basepath:
          if item.is_file():
             #Extracting file types 
             temp = ""
             for i in range(len(item.name)-1,0,-1):
                 if item.name[i]=='.':
                    break
                 else:
                    temp += item.name[i]
             temp = temp[::-1]
             #saving file types and correspond files in the file dict
             if temp != "py":
                try:
                  file_dict[temp].append(item.name)
                except KeyError:
                  file_dict[temp]=[]
                  file_dict[temp].append(item.name)
      #Creating folders in the destination path and moving files it into the folder            
      for x, y in file_dict.items():
          try:  
             os.mkdir(destination_path+x)
          #if the file already created
          except OSError as error:  
             print(error)
          for i in y:
          #moving or replacing the file in current source to destination
              try:
                 src = current_path
                 dst = destination_path+x
                 shutil.move(os.path.join(src,i), os.path.join(dst,i))
                 print(i," || ",x)
              except OSError as error:            
                 print(error)


      print("Sytemized")
   else:
      print("process denied")
       
   
   

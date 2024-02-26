import shutil
 
def copy_to_png_file(filename): 
  try: 
    shutil.copy(filename, 'lab1zad1.png') 
    print("File has been copied to lab1zad1.png") 
  except FileNotFoundError: 
    print("File does not exist") 
 
if __name__ == '__main__': 
  filename = input("Give a filename ") 
  copy_to_png_file(filename) 

 

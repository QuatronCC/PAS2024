def copy_to_file(filename): 
try: 
  with pen(filename, 'r') as input_file: 
   contents = input_file.read() 
   with open('lab1zad1.txt', 'w') as output_file: 
    output_file.write(contents) 
  print("File has been copied to lab1zad1.txt") 
except FileNotFoundError: 
   print("File does not exist") 
 
if __name__ == '__main__': 
filename = input("Give a filename") 
copy_to_file(filename) 

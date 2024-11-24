# 9) Write a Python program to handle file exceptions and use the finally block for closing the file. 
import os
os.chdir("D:\\paras\\Assignment\\Python\\Module-8 Advance Python Programming")

def handle_file_exceptions(file_path, mode):
    try:
        file = open(file_path, mode)
        print(f"File '{file_path}' opened successfully in {mode} mode.")
        
        if mode == 'r':
            content = file.read()
            print("File Content:")
            print(content)
        elif mode == 'w':
            file.write("This is a test write operation.\n")
            print("Data written to the file successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        print(f"Error: An I/O error occurred while handling the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    finally:
        try:
            file.close()
            print(f"File '{file_path}' closed successfully.")
        except NameError:
            print("File was not opened, so no need to close.")
        except Exception as e:
            print(f"Error while closing the file: {e}")

handle_file_exceptions("test.txt", 'r')  
handle_file_exceptions("9.txt", 'w')  




# ----------------------------------------------------- #

try:
    file = open("example.txt", "r")
    # Simulate an exception during file processing
    raise ValueError("An error occurred!")
except Exception as e:
    print(f"Error: {e}")
finally:
    try:
        file.close()
        print("File closed.")
    except NameError:
        print("File was not opened, so no need to close.")
    except Exception as e:
        print(f"Error while closing file: {e}")

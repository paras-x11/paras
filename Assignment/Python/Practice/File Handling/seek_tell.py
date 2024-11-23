import os
os.chdir("D:\\paras\\Assignment\\Python\\Practice\\File Handling")

with open("seek_tell.txt", "r") as f:
    # Move to the 10th byte in the file
    f.seek(10)  # Sets the file pointer to byte position 10

    # Print current position after seek
    print(f.tell())  # Outputs 10, since f.seek(10) moved the pointer to the 10th byte

    # Read the next 7 bytes from byte position 10
    data = f.read(7)  
    print(f.tell())
    print(data)  # Prints the 7 bytes starting from the 10th byte

print("\n")

with open("seek_tell.txt", "r") as f:
    # Read the next 7 bytes
    data = f.read(7)  # Reads 7 bytes from the start
    print(f.tell())  # Outputs 7, as it has moved 7 bytes from the start
    print(data)  # Prints the 7 bytes read

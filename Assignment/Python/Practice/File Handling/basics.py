import os
os.chdir("D:\\paras\\Assignment\\Python\\Practice\\File Handling")

# READ MODE:
f = open('b_r_file.txt', 'r')
text = f.read()
print(text)
f.close()

# WRITE MODE:
f = open('b_w_file.txt', 'w')
f.write("writing file \nhello, how are you")
f.close()

# APPEND MODE:
f = open('b_w_file.txt', 'a')
f.write('\n\nI am from append')
f.close()

# READING APPENDED FILE:
f = open('b_w_file.txt', 'r')
text = f.read()
print(text)
f.close()


# 'with' statement we dont need to close file in this way:
with open('b_with_keyword.txt', 'a') as f:
    f.write('hello there, i am from with statement...')

    
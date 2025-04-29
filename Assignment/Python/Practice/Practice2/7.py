# ### 📌 File Handling

import os
os.chdir("D:\\paras\\Assignment\\Python\\Practice\\Practice2\\txt")


# 36. Read from a file and count word frequency.
data = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# with open('example.txt', 'w') as f:
#     f.write(data)

# from collections import Counter
# import re

# with open('example.txt', 'r') as f:
#     text = f.read()

#     print(text)

#     words = re.findall(r"\b\w+\b", text.lower())

#     print(words)

#     word_counts = Counter(words)

#     for key, val in word_counts.items():
#         print(f"{key}: {val}")

# import os
# import datetime

# class LogWriter:
#     def __init__(self, file_path):
#         self._file_path = file_path
#         open(self._file_path, 'a').close()

#     def write_log(self, message):
#         timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
#         with open(self._file_path, 'a') as file:
#             file.write(f"{timestamp} {message}\n")

#     def read_logs(self):
#         with open(self._file_path, 'r') as file:
#             return [line.strip() for line in file.readlines()]

# 37. Append new lines to an existing file.
# with open('example.txt', 'a') as f:
#     line = "\n\nthis is line to be appended"
#     f.write(line)


# 38. Merge two text files into one.
# with open('example.txt', 'r') as f1, open('example2.txt', 'r') as f2:
#     data1 = f1.read()
#     data2 = f2.read()

# with open("merged_examples.txt", 'w') as f3:
#     f3.write(data1 + data2)

# 39. Read a CSV file and display content.
# import csv

# with open('data.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)




# 40. Remove blank lines from a file.
with open('merged_examples.txt', 'r') as f:
    lines = f.readlines()
    print(lines)

with open('output.txt', 'w') as f2:
    for line in lines:
        if line.strip():
            f2.write(line.strip() + '\n')

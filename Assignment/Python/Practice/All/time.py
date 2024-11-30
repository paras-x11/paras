import time

# print(time.strftime("%H : %M : %S"))

def usingFor():
    for i in range(1, 50001):
        print(i)

def usingWhile():
    i = 0
    while i < 50000:
        i = i + 1
        print(i)


init1 = time.time()
for_started = time.strftime("%H : %M : %S")
# usingFor()
for_ended = time.strftime("%H : %M : %S")
t1 = time.time() - init1

init2 = time.time()
while_started = time.strftime("%H : %M : %S")
# usingWhile()
while_ended = time.strftime("%H : %M : %S")
print(time.strftime("%H : %M : %S"))
t2 = time.time() - init2

print("Finished For loop:", t1)
print("Finished While loop:", t2)

print(f"for started at: {for_started} || for ended at: {for_ended}.")
print(f"while started at: {while_started} || while ended at: {while_ended}.")

print("now prg will sleep for 10 sec.", time.strftime("%H : %M : %S"))
time.sleep(10)
print("10 sec complete.", time.strftime("%H : %M : %S"))


        
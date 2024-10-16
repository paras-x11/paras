# 8. Write a Python program to test whether a passed letter is a vowel or not. 


c = input("Enter one letter: ")

vowels = ['a', 'e', 'i', 'o', 'u']

if len(c) != 1:
    print("-> Enter only one letter.")

else:
    if c.lower() in vowels:
        print(c, "is vowel.")
    else:
        print(c, "is an alphabet.")

    





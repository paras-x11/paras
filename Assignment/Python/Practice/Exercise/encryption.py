# coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
# now append three random characters at the starting and the end

# else:
# simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it

# else:
# remove 3 random characters from start and end. Now remove the last letter and append it to the beginning


import random as r
import string

def generate_random_string():
    return "".join(r.choice(string.ascii_letters) for _ in range(6))

s = input("Enter your message to encrypt: ")
# s = "paras rana. hello world"

e_words = s.split()
e_li = []
es = ""

for word in e_words:
    
    if len(word) <= 2:
        e_li.append(word[::-1])

    else:
        rs = generate_random_string()
        e_li.append( rs[:2] + word[1:] + word[0] + rs[3:]) 
    
for word in e_li:
    es += word + " " 

print("Your encrypted string is:", es)


# ------------------------------------------------------------------------------- #


ps = int(input("Now enter password to decrypt the message: "))
if ps == 123:
    d_words = es.split()
    d_li = []
    ds = ""

    for word in d_words:
        if len(word) <= 2:
            d_li.append(word[::-1])
        else:
            d_li.append(word[-4] + word[2:-4])
    
    ds = " ".join(d_li)
    
    print(ds)

else:
    print("wrong password.")









# ascii values letter range: 65 = A .. 90 = Z // 97 = a .. 122 = z

# generating random string of 3 letters:
# c1 = r.randint(97, 122)
# c2 = r.randint(97, 122)
# c3 = r.randint(97, 122)
# rs1 = f"{chr(c1)+chr(c2)+chr(c3)}"

# c1 = r.randint(97, 122)
# c2 = r.randint(97, 122)
# c3 = r.randint(97, 122)
# rs2 = f"{chr(c1)+chr(c2)+chr(c3)}"
# what is the use of finally block:
# -> when we returns in function, if we opened some file and we want to close it, clean resources etc. 



def func1():
    l = [45,67,89,34,90]
    try: 
        p = int(input("Enter position: "))
        print(l[p])
        return 1

    except Exception as e:
        print("input is not an integer.")
        return 0
    
    finally:
        print("i am finally.")
    
    print("last line out of finnaly")

print(func1())


# here, last line will printed but in function its not bcoz of returns
l = [45,67,89,34,90]
try: 
        p = int(input("Enter position: "))
        print(l[p])
except Exception as e:
        print("input is not an integer.")
    
finally:
        print("i am finally.")
    
print("last line out of finnaly")
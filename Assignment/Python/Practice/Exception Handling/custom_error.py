


n = input("Enter number between 5 to 9: ")

if n != 'quit':
    
    try:
        num = int(n)
        if num >= 5 and num <= 9:
            print("ok")
        else:
            raise Exception("custom errors")
            
    except ValueError:
        raise Exception("custom errors: invalid input")
    
else:
    print("quit.")


       
    
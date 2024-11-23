


n = input("Enter number between 5 to 9: ")

if n != 'quit':
    
    try:
        if int(n) >= 5 and int(n) <= 9:
            print("ok")
        else:
            raise Exception("custom errors")
            
    except:
        raise Exception("custom errors")
    
else:
    print("quit.")


       
    
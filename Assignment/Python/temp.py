# n = int(input("Enter: ").strip())
    
# if n % 2 != 0:
#          print("weird")
    
# elif n % 2 == 0 and 2 <= n <= 5:
#         print("Not Weird")
    
# elif n % 2 == 0 and 6 <= n <= 20:
#         print("Weird")
    
# else:
#         print("Not Weird")

class person:
        clg = "UCC"

        def __init__(self, id=0, name="your-name"):
                self.id = id
                self.name = name
                print("-> constructor\n")
        
        def show_info(self):
                print(self.id, self.name, self.clg)

        @staticmethod
        def dispaly():
                print("Displaying...")


p = person(1, "paras")
p.clg = "DRB"
p.show_info()

p1 = person()
p1.show_info()

person.show_info(p)

person.dispaly()
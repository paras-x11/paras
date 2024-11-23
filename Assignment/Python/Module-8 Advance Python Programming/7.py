# 7. Write a Python program to handle exceptions in a calculator.

class Calculator:

    def __init__(self, a, b):
        self._a = a
        self._b = b

    def add(self):
        return self._a + self._b

    def subtraction(self):
        return self._a - self._b

    def multiply(self):
        return self._a * self._b

    def division(self):
        if self._b == 0:
            raise ZeroDivisionError("Error: Division by zero is not allowed.")
        return self._a / self._b


if __name__ == '__main__':

    choices = [1, 2, 3, 4, 0]
    flag = True

    while flag:
        try:
            print(
                "\n1. for add \t         2. for subtraction \n3. for multiply \t 4. for division \t 0. for Exit")
            ch = int(input("\nEnter your choice: "))

            if ch not in choices:
                raise ValueError("\n-> Enter a valid choice.")

            elif ch == 0:
                print("\n-> Exited")
                break

            else:
                try:
                    a = int(input("\nEnter a: "))
                    b = int(input("Enter b: "))
                except ValueError:
                    print("-> Enter valid integers for a and b.")
                    continue

                calc = Calculator(a, b)

                match ch:
                    case 1:
                        print(f"\n-> {calc._a} + {calc._b} = {calc.add()}")

                    case 2:
                        print(
                            f"\n-> {calc._a} - {calc._b} = {calc.subtraction()}")

                    case 3:
                        print(
                            f"\n-> {calc._a} * {calc._b} = {calc.multiply()}")

                    case 4:
                        try:
                            print(
                                f"\n-> {calc._a} / {calc._b} = {calc.division()}")
                        except ZeroDivisionError as e:
                            print(e)

        except ValueError as e:
            print("-> Enter valid input.\n", e)

        except Exception as e:
            print("An unexpected error occurred:", e)

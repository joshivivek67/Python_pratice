def even_odd(number):
    if (int(number) % 2)  == 0 and (int(number) %4) ==0:
        print(f"{number} is Even and multiple of 4")
    elif (int(number) %2) == 0:
        print(f"{number} is Even Only")
    else:
        print("Number is odd")

def user_input():
    number =input("Please Enter the Number: ")
    if int(number) < 0 and not type(number) is int:
        raise Exception("Sorry, Number is below zero")
    else:
        even_odd(number)

def main():
    user_input()

if __name__ == "__main__":
    main()


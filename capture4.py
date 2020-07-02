def devisors(number):
    numbers = [num for num in range(1,int(number)+1) if int(number) % num == 0 ]
    return numbers
    


def user_input():

    number = int(input("Please enter the number for which you want all the devisors: "))
    print(devisors(number))
    

def main():
    user_input()

if __name__ == "__main__":
    main()

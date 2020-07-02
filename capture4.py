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

    """
    python3.7 capture4.py 
Please enter the number for which you want all the devisors: 100000000
[1, 2, 4, 5, 8, 10, 16, 20, 25, 32, 40, 50, 64, 80, 100, 125, 128, 160, 200, 250, 256, 320, 400, 500, 625, 640, 800, 1000, 1250, 1280, 1600, 2000, 2500, 3125, 3200, 4000, 5000, 6250, 6400, 8000, 10000, 12500, 15625, 16000, 20000, 25000, 31250, 32000, 40000, 50000, 62500, 78125, 80000, 100000, 125000, 156250, 160000, 200000, 250000, 312500, 390625, 400000, 500000, 625000, 781250, 800000, 1000000, 1250000, 1562500, 2000000, 2500000, 3125000, 4000000, 5000000, 6250000, 10000000, 12500000, 20000000, 25000000, 50000000, 100000000]
    """

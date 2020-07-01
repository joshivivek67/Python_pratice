import  datetime

def name_age(name , age, number):
    """
    This Function Will year the person when he turn 100
    
    Args:
      name: Name of the person.
      age: Age of the person.
      number. Number of time message will get print 

    Return:
        Year when the person Turn 100

    """
    year = datetime.date.today().year 
    Year_in_100 = (year - age)  + 100
    print(number * f" Hey {name}  you will be 100 in  {Year_in_100} \n")

def Take_the_detail():
    """
        Take all the require input
    """
    Name = input(" Please Enter Your name: ")
    print("Age should be only positive interger")
    Age  = int(input("Please Enter your age:"))
    Number_of_print = int(input("Please enter the number: "))
    name_age(Name , Age,Number_of_print)
    

def main():
    Take_the_detail()

if __name__ == "__main__":
    main()
import random

def comman_list_elements(list_1, list_2):
    return (set(list_1) & set(list_2))

def return_random_list(number_of_element):
    list_of_ran = []
    for i in range(0 ,int(number_of_element)):
        ran = random.randint(0,50)
        list_of_ran.append(ran)
    return list_of_ran

def random_list():
    list_one_no_of_element =random.randint(10,20)
    list_two_no_of_element = random.randint(10,20)
    list_one = return_random_list(list_one_no_of_element)
    list_two = return_random_list(list_two_no_of_element)
    print(list_one)
    print(list_two)
    print(list(comman_list_elements(list_one,list_two)))
   


def main():
    random_list()

if __name__ == "__main__":
    main()



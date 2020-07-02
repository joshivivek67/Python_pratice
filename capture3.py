def sort_and_print_the_data(list_with_10_number,lower_than_this):
    modified_list = [int(x) for x in list_with_10_number]
    #sorted_list = sorted(modified_list)
    list_less_then_ten = [number_in_list for number_in_list in modified_list if number_in_list < int(lower_than_this)]
    return list_less_then_ten


def input_the_number():
    my_list= []
    i = 1
    while len(my_list) !=3:
        number = input(f"Please enter the  {i} number: ")
        my_list.append(number)
        i += 1
    lower = input("Please enter the number that will compare with the and print the lower value: ")
    print(sort_and_print_the_data(my_list,lower))



def main():
    input_the_number()
    

if __name__  == '__main__':
    main()
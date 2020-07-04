def palindrome(string):
    len_of_string= int((len(string))/2)
    for i in range(0, len_of_string):
        j = -1
        k=0
        if string[k] == string[j]:
            j -= 1
            k += 1
            return str(f"The word {string} is a palindrome")
        else:
            return str("not a palindrome")



def string_input():
    palindrome_string = input("please input the string: ")
    print(palindrome(palindrome_string))

def  main():
    string_input()

if __name__ =="__main__":
    main()
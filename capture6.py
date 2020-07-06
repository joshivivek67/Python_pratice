def palindrome(string):
    if string == string[::-1]:
        return str(f"The Word {string} is Palindrome")
    else:
        return str(f"The Word {string} is not Palindrome")

def string_input():
    palindrome_string = input("please input the string: ")
    print(palindrome(palindrome_string))

def  main():
    string_input()

if __name__ =="__main__":
    main()

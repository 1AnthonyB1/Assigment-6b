def main():
     
    s = (0)
    n = (0)
    k = (input("\nWhat is the number you would like to iterate PI?\nEnter your number here: "))

    if k.isnumeric() == True:
        for n in range(int(k)):
            s += (((-1)**int(n))*4)/(2*int(n)+1)
        print("\nYour final Iterated PI is:",s)
    elif k.isnumeric != True:
         print("\nYou silly goose, next time please type in a number")

    while True:
            r = input("\nWould you like another question or Quit?\nYes or No: ")

            capr = str.upper(r)
            if capr == "YES" or capr == "Y":
                main()
            elif capr == "NO" or capr == "N":
                print("\nThank you for using Assigment6b!, have a good one!\n")
                exit()
            
            else:
                print("\nPlease answer with yes or No")
main()
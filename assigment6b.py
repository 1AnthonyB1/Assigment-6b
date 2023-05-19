def main():
     
    s = int(0)
    n = int(0)
    k = int(input("\nWhat is the number you would like to iterate PI?\nEnter your number here: "))

    for n in range(k):
        s += (((-1)**n)*4)/(2*n+1)
    print("\nYour final Iterated PI is:",s)

    while True:
            r = input("\nWould you like another question or Quit?\nYes or No: ")

            capr = str.upper(r)
            if capr == "YES" or capr == "Y":
                main()
            elif capr == "NO" or capr == "N":
                print("\nThank you for using Assigment6b!, have a good one!\n")
                exit()
            
            else:
                print("\nPlease answer with yes or Quit\n")
                main()
main()
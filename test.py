a=int(input("Enter a number:"))
ns=str(a)

# To check whether the number is palindrome or not
if ns == ns[::-1]:
    print("The number is palindrome")
else:
    print("The number is not palindrome")
